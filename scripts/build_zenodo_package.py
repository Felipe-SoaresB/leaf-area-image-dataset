#!/usr/bin/env python3
"""Build and audit the privacy-corrected public edition without uploading it."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, UnidentifiedImageError

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = 198


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def git_csv(commit: str, path: str) -> list[dict[str, str]]:
    data = subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)
    text = data.decode("utf-8-sig")
    return list(csv.DictReader(text.splitlines()))


def check_frozen_science(baseline: str, excluded: set[str]) -> dict[str, int]:
    old = git_csv(baseline, "release/images_v1.csv")
    new = csv_rows(ROOT / "release/images_v1.csv")
    old_by_name = {r["filename"]: r for r in old}
    assert len(old_by_name) == 205
    assert set(old_by_name) - set(r["filename"] for r in new) == excluded
    for row in new:
        assert row == old_by_name[row["filename"]], f"Campo de índice mudou: {row['filename']}"
    old_groups = git_csv(baseline, "release/area_groups_v1.csv")
    new_groups = csv_rows(ROOT / "release/area_groups_v1.csv")
    assert new_groups == old_groups, "Valores ou partição de grupos foram alterados"
    source_equivalence = {}
    for path in ["metadata/tabela_mestre_v1.csv", "metadata/imagens_drive.csv"]:
        old_source = git_csv(baseline, path)
        new_source = csv_rows(ROOT / path)
        key = "filename"
        old_map = {r[key]: r for r in old_source}
        new_map = {r[key]: r for r in new_source}
        assert set(old_map) - set(new_map) == excluded and len(new_map) == 198
        assert all(r == old_map[n] for n, r in new_map.items()), f"Campo de fonte mudou: {path}"
        source_equivalence[path] = len(new_source)
    for path in ["metadata/referencias_imagej.csv", "metadata/divisao_experimental_v1.csv"]:
        assert csv_rows(ROOT / path) == git_csv(baseline, path), f"Referência/split alterado: {path}"
    return {"historical_images": len(old), "removed_non_samples": len(excluded), "public_images": len(new), "unchanged_group_rows": len(new_groups), "unchanged_source_rows": source_equivalence, "unchanged_reference_and_split": True}


def verify_images(image_dir: Path, index: list[dict[str, str]], hashes: dict[str, str]) -> dict[str, int]:
    names = {r["filename"] for r in index}
    files = {p.name for p in image_dir.glob("*.jpg")}
    assert len(names) == EXPECTED and names == files == set(hashes), "Imagens, índice e manifesto não correspondem"
    exif_count = gps_count = decoded = 0
    for name in sorted(names):
        p = image_dir / name
        assert sha256(p) == hashes[name], f"SHA-256 divergente: {name}"
        try:
            with Image.open(p) as im:
                assert im.format == "JPEG" and im.mode == "RGB", f"Formato/cor: {name}"
                exif = im.getexif()
                exif_count += bool(exif)
                gps_count += bool(exif.get(34853))
                im.verify()
            decoded += 1
        except (OSError, UnidentifiedImageError) as exc:
            raise AssertionError(f"JPEG ilegível: {name}: {exc}") from exc
    assert exif_count == 0 and gps_count == 0, "EXIF/GPS detectado"
    return {"image_count": len(names), "decoded_images": decoded, "images_with_exif": exif_count, "images_with_gps": gps_count}


def write_zip(source: Path, archive: Path) -> None:
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_STORED, allowZip64=True) as z:
        for p in sorted(source.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(source).as_posix())


def verify_zip(archive: Path, extract_dir: Path) -> int:
    with zipfile.ZipFile(archive) as z:
        bad = z.testzip()
        assert bad is None, f"CRC do ZIP inválido: {bad}"
        z.extractall(extract_dir)
    return sum(1 for p in extract_dir.rglob("*") if p.is_file())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", type=Path, required=True)
    ap.add_argument("--private-audit", type=Path, required=True, help="JSON local privado com lista de exclusões; não será copiado")
    ap.add_argument("--baseline-commit", required=True, help="Commit da coleção histórica de 205 imagens")
    args = ap.parse_args()
    out = args.output_dir.resolve()
    if out.exists() and any(out.iterdir()):
        raise SystemExit(f"Diretório de saída não está vazio: {out}")
    out.mkdir(parents=True, exist_ok=True)
    audit = json.loads(args.private_audit.read_text(encoding="utf-8-sig"))
    excluded = {r["filename"] for r in audit}
    assert len(excluded) == 7

    idx = csv_rows(ROOT / "release/images_v1.csv")
    groups = csv_rows(ROOT / "release/area_groups_v1.csv")
    assert len(idx) == EXPECTED and len({r["image_id"] for r in idx}) == EXPECTED
    assert len({r["sample_group_id"] for r in idx if r["sample_group_id"]}) == 181
    assert sum(r["include_for_area_evaluation"] == "yes" for r in idx) == 191
    assert sum(r["include_for_area_evaluation"] == "no" for r in idx) == 7
    assert len(groups) == 177 and len({r["sample_group_id"] for r in groups}) == 177
    assert sum(r["split"] == "development" for r in groups) == 44
    assert sum(r["split"] == "final_test" for r in groups) == 133
    assert {r["filename"] for r in idx}.isdisjoint(excluded)

    hashes = {}
    for line in (ROOT / "checksums/SHA256_RELEASE_NO_EXIF.txt").read_text(encoding="utf-8-sig").splitlines():
        if line.strip():
            digest, name = line.split(None, 1)
            hashes[name.strip()] = digest.lower()
    science = check_frozen_science(args.baseline_commit, excluded)
    image_result = verify_images(ROOT / "images/data", idx, hashes)

    stage = out / "stage"
    if stage.exists():
        shutil.rmtree(stage)
    combined = stage / "leaf_area_dataset_v1.0.3"
    (combined / "images/data").mkdir(parents=True)
    (combined / "release").mkdir(parents=True)
    (combined / "checksums").mkdir(parents=True)
    (combined / "docs").mkdir(parents=True)
    for row in idx:
        shutil.copy2(ROOT / "images/data" / row["filename"], combined / "images/data" / row["filename"])
    shutil.copy2(ROOT / "release/images_v1.csv", combined / "release/images_v1.0.3.csv")
    shutil.copy2(ROOT / "release/area_groups_v1.csv", combined / "release/area_groups_v1.0.3.csv")
    shutil.copy2(ROOT / "checksums/SHA256_RELEASE_NO_EXIF.txt", combined / "checksums/SHA256_RELEASE_NO_EXIF.txt")
    for rel in ["README.md", "LICENSE-DATA.md", "CITATION.cff", "VERSION"]:
        shutil.copy2(ROOT / rel, combined / rel)
    for rel in ["DATASET_CARD.md", "DATA_DICTIONARY.md", "EXCLUSIONS_AND_LIMITATIONS.md", "TREATMENT_CODES.md", "PROVENANCE.md"]:
        shutil.copy2(ROOT / "docs" / rel, combined / "docs" / rel)
    shutil.copy2(ROOT / "reports/PRIVACY_CORRECTION_2026-11-11.md", combined / "docs/PRIVACY_CORRECTION.md")

    data_tree = stage / "data_zip"
    (data_tree / "images").mkdir(parents=True)
    for row in idx:
        shutil.copy2(ROOT / "images/data" / row["filename"], data_tree / "images" / row["filename"])
    shutil.copy2(ROOT / "checksums/SHA256_RELEASE_NO_EXIF.txt", data_tree / "SHA256_RELEASE_NO_EXIF.txt")
    doc_tree = stage / "documentation_zip"
    shutil.copytree(combined, doc_tree, ignore=shutil.ignore_patterns("images"))
    for p in [out / "images_v1.0.3.csv", out / "area_groups_v1.0.3.csv"]:
        shutil.copy2(ROOT / "release" / p.name.replace(".0.3", ""), p)

    archives = {
        "leaf_area_images_v1.0.3.zip": data_tree,
        "leaf_area_dataset_documentation_v1.0.3.zip": doc_tree,
        "Zenodo_leaf_area_dataset_v1.0.3_privacy_corrected.zip": combined,
    }
    zip_files = {}
    for name, tree in archives.items():
        archive = out / name
        write_zip(tree, archive)
        extracted = out / (name.replace(".zip", "_extracted"))
        count = verify_zip(archive, extracted)
        zip_files[name] = {"sha256": sha256(archive), "bytes": archive.stat().st_size, "files_extracted": count}

    combo_extract = out / "combined_check"
    with zipfile.ZipFile(out / "Zenodo_leaf_area_dataset_v1.0.3_privacy_corrected.zip") as z:
        z.extractall(combo_extract)
    extracted_root = combo_extract
    extracted_hashes = {p.name: sha256(p) for p in (extracted_root / "images/data").glob("*.jpg")}
    assert extracted_hashes == {n: hashes[n] for n in hashes}
    for name in excluded:
        assert not any(name in str(p) for p in out.rglob("*")), f"Exclusão presente no pacote: {name}"

    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "edition": "1.0.3 privacy-corrected; not uploaded",
        "counts": {"public_jpegs": len(idx), "sample_groups": 181, "valid_imagej_groups": len(groups), "quantitatively_eligible_images": 191, "excluded_non_samples": len(excluded), "development_groups": 44, "final_test_groups": 133},
        "baseline_commit": args.baseline_commit,
        "science_equivalence": science,
        "image_checks": image_result,
        "excluded_names_absent": True,
        "zip_integrity_and_extraction": zip_files,
        "status": "PASS_LOCAL_PACKAGE_VALIDATION",
        "note": "Technical validation does not certify rights or remove historical GitHub/Zenodo copies."
    }
    (out / "validation_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    deliverables = {k: v["sha256"] for k, v in zip_files.items()}
    deliverables.update({p.name: sha256(p) for p in out.glob("*.csv")})
    (out / "SHA256_PACKAGE.txt").write_text("".join(f"{digest}  {name}\n" for name, digest in sorted(deliverables.items())), encoding="utf-8")
    shutil.rmtree(stage)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
