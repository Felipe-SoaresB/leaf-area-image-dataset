#!/usr/bin/env python3
"""Validação reproduzível do dataset de área foliar v1.0.

Não altera nenhum arquivo original. Os relatórios e o manifesto SHA-256,
quando solicitado, são gravados somente em --output-dir.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

FILE_NAMES = {
    "master": "tabela_mestre_v1.csv",
    "images": "imagens_drive.csv",
    "imagej": "referencias_imagej.csv",
    "split": "divisao_experimental_v1.csv",
}
REQUIRED = {
    "master": {"image_id", "filename", "sample_group_id", "sheet_row", "mapping_status",
               "qc_status", "area_status", "area_referencia_cm2", "exclude_from_analysis",
               "exclusion_reason", "substrato_normalizado", "percentual", "bandeja_repeticao", "coleto"},
    "images": {"filename", "drive_file_count", "canonical_drive_id", "size_bytes",
               "duplicate_suspected", "all_drive_ids"},
    "imagej": {"sheet_row", "substrato_normalizado", "percentual", "bandeja_repeticao",
               "coleto", "area", "area_status"},
    "split": {"sample_group_id", "canonical_image_id", "canonical_filename",
              "area_referencia_cm2", "n_images", "extra_retake_images", "stratum", "split"},
}
PROFILE = {"master": 205, "images": 205, "imagej": 291, "split": 177,
           "groups": 181, "eligible": 177, "positive_imagej": 245, "zero_imagej": 45,
           "text_imagej": 1, "source_files": 271, "duplicate_names": 66,
           "development": 44, "final_test": 133}


def number(value: str) -> Decimal | None:
    try:
        d = Decimal(value.strip())
        return d if d.is_finite() else None
    except (InvalidOperation, AttributeError):
        return None


def same_number(x: str, y: str) -> bool:
    a, b = number(x), number(y)
    return (a == b) if (a is not None and b is not None) else x.strip() == y.strip()


def get_rows(path: Path) -> tuple[list[dict[str, str]], set[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        cols = set(reader.fieldnames or [])
        return [dict(row) for row in reader], cols


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


class Audit:
    def __init__(self) -> None:
        self.issues: list[dict[str, Any]] = []
        self.metrics: dict[str, Any] = {}
        self.checked: dict[str, str] = {"metadata": "pending", "image_files": "not_checked",
                                        "duplicate_binaries": "not_checked"}

    def issue(self, severity: str, code: str, message: str, record: str = "") -> None:
        self.issues.append({"severity": severity, "code": code, "record": record, "message": message})

    def check(self, ok: bool, code: str, message: str, record: str = "") -> None:
        if not ok:
            self.issue("ERROR", code, message, record)


def check_unique(audit: Audit, rows: list[dict[str, str]], field: str, name: str,
                 allow_empty: bool = False) -> None:
    vals = [r.get(field, "").strip() for r in rows]
    repeated = [k for k, v in Counter(vals).items() if v > 1 and k]
    audit.check(not repeated, "DUPLICATE_ID", f"{name}.{field}: {len(repeated)} valores repetidos", name)
    if not allow_empty:
        audit.check("" not in vals, "EMPTY_ID", f"{name}.{field} contém valores vazios", name)


def validate_metadata(audit: Audit, tables: dict[str, list[dict[str, str]]],
                      *, enforce_profile: bool) -> None:
    m, ims, refs, split = (tables[k] for k in ("master", "images", "imagej", "split"))
    for name, records in tables.items():
        audit.metrics[f"rows_{name}"] = len(records)
        if enforce_profile:
            audit.check(len(records) == PROFILE[name], "COUNT", f"{name}: {len(records)} linhas, esperado {PROFILE[name]}")

    for name, field in (("master", "image_id"), ("master", "filename"),
                        ("images", "filename"), ("imagej", "sheet_row"),
                        ("split", "sample_group_id"), ("split", "canonical_image_id")):
        check_unique(audit, tables[name], field, name)

    source_names = {x["filename"] for x in ims}
    master_names = {x["filename"] for x in m}
    audit.check(source_names == master_names, "MANIFEST_SET",
                f"Imagens sem mestre: {len(source_names-master_names)}; no mestre sem manifesto: {len(master_names-source_names)}")
    byref = {r["sheet_row"]: r for r in refs}
    byimage = {r["filename"]: r for r in m}
    byid = {r["image_id"]: r for r in m}
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in m:
        group = r["sample_group_id"].strip()
        if group:
            groups[group].append(r)
        else:
            audit.check(r["qc_status"] in ("non_sample", "invalid_capture"),
                        "UNASSIGNED_IMAGE", "Imagem sem grupo deve estar documentada como não amostra ou inválida", r["image_id"])
        excluded = r["exclude_from_analysis"]
        audit.check(excluded in {"yes", "no"}, "EXCLUDE_FLAG", "Flag de exclusão inválida", r["image_id"])
        if excluded == "yes":
            audit.check(bool(r["exclusion_reason"].strip()), "MISSING_REASON", "Exclusão sem justificativa", r["image_id"])
        if r["mapping_status"] == "confirmed":
            audit.check(bool(group and r["sheet_row"]), "CONFIRMED_MISSING_LINK", "Ligação confirmada sem grupo/linha", r["image_id"])
        area = number(r["area_referencia_cm2"])
        if excluded == "no":
            audit.check(r["mapping_status"] == "confirmed" and area is not None and area > 0,
                        "INELIGIBLE_INCLUDED", "Incluído na análise sem identidade confirmada e área positiva", r["image_id"])
        if r["sheet_row"]:
            ref = byref.get(r["sheet_row"])
            if ref is None:
                audit.issue("ERROR", "UNKNOWN_SHEET_ROW", "Linha ImageJ referenciada não existe", r["image_id"])
            else:
                if not same_number(r["area_referencia_cm2"], ref["area"]):
                    audit.issue("ERROR", "AREA_DISAGREEMENT", "Área mestre difere da planilha ImageJ", r["image_id"])
                for field in ("substrato_normalizado", "percentual", "bandeja_repeticao"):
                    if r[field] != ref[field]:
                        audit.issue("ERROR", "REFERENCE_MISMATCH", f"Divergência no campo {field}", r["image_id"])

    for group, records in groups.items():
        for field in ("substrato_normalizado", "percentual", "bandeja_repeticao", "sheet_row",
                      "area_referencia_cm2", "mapping_status", "exclude_from_analysis"):
            if len({r[field] for r in records}) > 1:
                audit.issue("ERROR", "GROUP_DISAGREEMENT", f"Retakes divergem em {field}", group)
    audit.metrics["biological_groups"] = len(groups)
    eligible = {k for k, records in groups.items() if all(
        r["mapping_status"] == "confirmed" and r["exclude_from_analysis"] == "no"
        and (number(r["area_referencia_cm2"]) or Decimal(0)) > 0 for r in records)}
    audit.metrics["eligible_groups"] = len(eligible)
    if enforce_profile:
        for field, actual in (("groups", len(groups)), ("eligible", len(eligible))):
            audit.check(actual == PROFILE[field], "GROUP_COUNT", f"{field}: {actual}; esperado {PROFILE[field]}")

    # Divergências no Coleto são relatadas por grupo e não sobrescrevem a evidência original.
    coleto_by_group: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in m:
        if r["sheet_row"] and r["sample_group_id"]:
            other = byref.get(r["sheet_row"])
            if other and not same_number(r.get("coleto", ""), other.get("coleto", "")):
                coleto_by_group[r["sample_group_id"]].append(r)
    audit.metrics["coleto_disagreement_groups"] = len(coleto_by_group)
    for group, rows in sorted(coleto_by_group.items()):
        first = rows[0]
        audit.issue("WARNING", "COLETO_DIFFERENCE",
                    f"Coleto foto/mestre={first['coleto']} e planilha={byref[first['sheet_row']]['coleto']}; manter justificativa documental",
                    group)

    positive, zero, non_numeric = 0, 0, 0
    for r in refs:
        value = number(r["area"])
        if value is None:
            non_numeric += 1
            audit.check(r["area_status"] in ("text", "missing"), "AREA_STATUS", "Área não numérica com status incompatível", r["sheet_row"])
        elif value > 0:
            positive += 1
            audit.check(r["area_status"] == "positive", "AREA_STATUS", "Área positiva com status incorreto", r["sheet_row"])
        elif value == 0:
            zero += 1
            audit.check(r["area_status"] == "zero", "AREA_STATUS", "Área zero com status incorreto", r["sheet_row"])
        else:
            audit.issue("ERROR", "NEGATIVE_AREA", "Área negativa não permitida", r["sheet_row"])
    audit.metrics["reference_positive"] = positive
    audit.metrics["reference_zero"] = zero
    audit.metrics["reference_non_numeric"] = non_numeric
    if enforce_profile:
        for k, n in (("positive_imagej", positive), ("zero_imagej", zero), ("text_imagej", non_numeric)):
            audit.check(n == PROFILE[k], "REFERENCE_COUNT", f"{k}: {n}, esperado {PROFILE[k]}")

    split_counts = Counter(r["split"] for r in split)
    audit.metrics["split_counts"] = dict(split_counts)
    audit.check(set(split_counts) <= {"development", "final_test"}, "UNKNOWN_SPLIT", "Split não reconhecido")
    audit.check({r["sample_group_id"] for r in split} == eligible, "SPLIT_COVERAGE",
                "A divisão experimental deve conter todos e apenas os grupos elegíveis")
    if enforce_profile:
        for key in ("development", "final_test"):
            audit.check(split_counts[key] == PROFILE[key], "SPLIT_COUNT", f"{key}: {split_counts[key]} em vez de {PROFILE[key]}")
    for row in split:
        group = row["sample_group_id"]
        records = groups.get(group, [])
        if not records:
            audit.issue("ERROR", "UNKNOWN_GROUP", "Grupo da divisão não existe", group)
            continue
        ordered = sorted(records, key=lambda r: (r.get("capture_date", ""), r.get("capture_time", ""), r["filename"]))
        first = ordered[0]
        if row["canonical_image_id"] != first["image_id"] or row["canonical_filename"] != first["filename"]:
            audit.issue("ERROR", "CANONICAL_IMAGE", "Foto canônica não é a primeira cronológica", group)
        if row["canonical_image_id"] not in byid or row["canonical_filename"] not in byimage:
            audit.issue("ERROR", "UNKNOWN_CANONICAL", "Foto canônica não encontrada no mestre", group)
        if not same_number(row["area_referencia_cm2"], first["area_referencia_cm2"]):
            audit.issue("ERROR", "SPLIT_AREA", "Área do split difere da tabela mestre", group)
        if row["stratum"] != f"{first['substrato_normalizado']}|{first['percentual']}":
            audit.issue("ERROR", "SPLIT_STRATUM", "Estrato não coincide com o mestre", group)
        if number(row["n_images"]) != len(records) or number(row["extra_retake_images"]) != len(records)-1:
            audit.issue("ERROR", "SPLIT_RETAKES", "Quantidade de capturas/retakes difere do mestre", group)
    audit.metrics["eligible_image_rows"] = sum(len(groups[k]) for k in eligible)
    audit.metrics["extra_retakes_eligible"] = audit.metrics["eligible_image_rows"] - len(eligible)
    audit.metrics["qc_status"] = dict(Counter(r["qc_status"] for r in m))
    if audit.metrics["qc_status"].get("pending"):
        audit.issue("WARNING", "PENDING_QC", f"{audit.metrics['qc_status']['pending']} fotografias com qc_status=pending; esclarecer significado antes da publicação")

    source_count, doubles, repeated_rows = 0, 0, set()
    for r in ims:
        name = r["filename"]
        val = number(r["drive_file_count"])
        if val is None or val < 1 or val != val.to_integral_value():
            audit.issue("ERROR", "INVALID_SOURCE_COUNT", "drive_file_count não é inteiro positivo", name)
            continue
        copies = int(val)
        source_count += copies
        doubles += copies == 2
        declared = [x.strip() for x in re.split(r"[|;]", r["all_drive_ids"]) if x.strip()]
        audit.check(len(declared) == copies, "SOURCE_ID_COUNT", "IDs do Drive não correspondem ao número de cópias", name)
        audit.check(len(set(declared)) == len(declared), "DUPLICATE_SOURCE_ID", "ID repetido na origem", name)
        audit.check(r["canonical_drive_id"] in declared, "CANONICAL_DRIVE_ID", "ID canônico não aparece no manifesto", name)
        audit.check(r["duplicate_suspected"] == ("yes" if copies > 1 else "no"), "DUPLICATE_FLAG", "Flag de duplicação incorreta", name)
    audit.metrics["source_file_count_from_manifest"] = source_count
    audit.metrics["duplicate_names_from_manifest"] = doubles
    if enforce_profile:
        audit.check(source_count == PROFILE["source_files"], "SOURCE_COUNT", "Número de arquivos origem divergente")
        audit.check(doubles == PROFILE["duplicate_names"], "SOURCE_DUPLICATES", "Número de duplas divergente")

    audit.checked["metadata"] = "pass" if not any(x["severity"] == "ERROR" for x in audit.issues) else "fail"


def validate_images(audit: Audit, tables: dict[str, list[dict[str, str]]], images_dir: Path,
                    checksums: Path | None, write_checksums: bool, output_dir: Path) -> None:
    try:
        from PIL import Image, UnidentifiedImageError
    except ImportError:
        audit.issue("ERROR", "PILLOW_MISSING", "Instale Pillow: python -m pip install Pillow")
        audit.checked["image_files"] = "fail"
        return
    indexed = {r["filename"]: r for r in tables["images"]}
    expected_hashes: dict[str, str] = {}
    if checksums is not None:
        if not checksums.is_file():
            audit.issue("ERROR", "CHECKSUM_FILE_MISSING", f"Manifesto inexistente: {checksums}")
        else:
            for raw in checksums.read_text(encoding="utf-8").splitlines():
                if not raw.strip():
                    continue
                match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", raw.strip())
                if not match:
                    audit.issue("ERROR", "BAD_CHECKSUM_LINE", "Linha SHA-256 inválida", raw[:120])
                else:
                    expected_hashes[Path(match[2]).name] = match[1].lower()
    measured: dict[str, str] = {}
    status_counts: Counter[str] = Counter()
    hash_to_names: dict[str, list[str]] = defaultdict(list)
    for name, record in sorted(indexed.items()):
        path = images_dir / name
        if not path.is_file():
            audit.issue("ERROR", "MISSING_IMAGE", "Fotografia não encontrada", name)
            status_counts["missing"] += 1
            continue
        try:
            actual_size = path.stat().st_size
            declared_size = number(record["size_bytes"])
            if declared_size is None or actual_size != declared_size:
                audit.issue("ERROR", "SIZE_MISMATCH", f"Tamanho: {actual_size} bytes; manifesto: {record['size_bytes']}", name)
            with Image.open(path) as img:
                img.verify()
            with Image.open(path) as img:
                if img.format != "JPEG":
                    audit.issue("ERROR", "IMAGE_FORMAT", f"Formato {img.format} em vez de JPEG", name)
                if img.mode != "RGB":
                    audit.issue("ERROR", "IMAGE_COLOR", f"Modo {img.mode} em vez de RGB", name)
                if img.size not in {(4000, 3000), (3000, 4000)}:
                    audit.issue("ERROR", "IMAGE_RESOLUTION", f"Resolução inesperada: {img.size}", name)
                exif = img.getexif()
                make, model = str(exif.get(271, "")).lower(), str(exif.get(272, "")).lower()
                if make != "motorola" or model != "moto g(20)":
                    audit.issue("WARNING", "CAMERA_METADATA", "EXIF fabricante/modelo diferente do histórico", name)
                img.load()
            hashed = sha256_file(path)
            measured[name] = hashed
            hash_to_names[hashed].append(name)
            if checksums is not None:
                if name not in expected_hashes:
                    audit.issue("ERROR", "NO_EXPECTED_CHECKSUM", "SHA-256 ausente do manifesto fornecido", name)
                elif hashed != expected_hashes[name]:
                    audit.issue("ERROR", "CHECKSUM_MISMATCH", "SHA-256 difere do valor publicado", name)
            status_counts["verified"] += 1
        except Exception as exc:
            audit.issue("ERROR", "UNREADABLE_IMAGE", f"Falha na leitura/verificação: {exc}", name)
            status_counts["unreadable"] += 1
    for hashed, names in hash_to_names.items():
        if len(names) > 1:
            audit.issue("WARNING", "IDENTICAL_CONTENT", f"Conteúdo SHA-256 idêntico entre nomes distintos: {', '.join(names)}")
    extras = {p.name for p in images_dir.iterdir() if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg"}} - set(indexed)
    if extras:
        audit.issue("WARNING", "EXTRA_JPEGS", f"Há {len(extras)} JPEGs fora do manifesto; exemplo: {', '.join(sorted(extras)[:5])}")
    audit.metrics["image_file_checks"] = dict(status_counts)
    audit.metrics["distinct_sha256"] = len(hash_to_names)
    if write_checksums:
        path = output_dir / "SHA256SUMS.txt"
        path.write_text("".join(f"{digest}  {name}\n" for name, digest in sorted(measured.items())), encoding="utf-8")
        audit.metrics["new_checksum_manifest"] = str(path)
    audit.checked["image_files"] = "pass" if status_counts["verified"] == len(indexed) and not any(
        x["severity"] == "ERROR" and x["code"] in {"MISSING_IMAGE", "SIZE_MISMATCH", "IMAGE_FORMAT", "IMAGE_COLOR", "IMAGE_RESOLUTION", "UNREADABLE_IMAGE", "CHECKSUM_MISMATCH", "NO_EXPECTED_CHECKSUM"}
        for x in audit.issues) else "fail"


def verify_source_copies(audit: Audit, originals_inventory: Path, expected_names: set[str]) -> None:
    """CSV opcional: filename,path. path é relativo à localização deste CSV."""
    records, cols = get_rows(originals_inventory)
    if not {"filename", "path"} <= cols:
        audit.issue("ERROR", "INVENTORY_COLUMNS", "Inventário de cópias exige filename,path")
        audit.checked["duplicate_binaries"] = "fail"
        return
    files: dict[str, list[Path]] = defaultdict(list)
    for row in records:
        path = Path(row["path"])
        if not path.is_absolute():
            path = originals_inventory.parent / path
        files[row["filename"]].append(path)
    audit.check(set(files) == expected_names, "COPY_NAMES", "Nomes no inventário de cópias diferem do dataset")
    expected_source = audit.metrics.get("source_file_count_from_manifest")
    audit.check(len(records) == expected_source, "COPY_RECORD_COUNT",
                f"Inventário contém {len(records)} cópias, manifesto registra {expected_source}")
    declared_pairs = audit.metrics.get("duplicate_names_from_manifest")
    actual_pairs = sum(len(paths) == 2 for paths in files.values())
    audit.check(actual_pairs == declared_pairs, "COPY_PAIR_COUNT",
                f"Inventário contém {actual_pairs} pares, manifesto registra {declared_pairs}")
    compared, unequal, missing = 0, 0, 0
    for name, paths in files.items():
        hashes = []
        for path in paths:
            if not path.is_file():
                audit.issue("ERROR", "COPY_NOT_FOUND", f"Cópia de origem não existe: {path}", name)
                missing += 1
                continue
            hashes.append(sha256_file(path))
        if len(paths) > 1 and len(hashes) == len(paths):
            compared += 1
            if len(set(hashes)) != 1:
                unequal += 1
                audit.issue("ERROR", "COPIES_NOT_IDENTICAL", "Arquivos de mesmo nome com conteúdo diferente", name)
    audit.metrics["original_source_copy_checks"] = {"listed_files": len(records), "groups_compared": compared,
                                                    "different_content": unequal, "missing_files": missing}
    audit.checked["duplicate_binaries"] = "pass" if (
        missing == 0 and unequal == 0 and compared == declared_pairs
        and len(records) == expected_source and set(files) == expected_names
    ) else "fail"


def write_reports(audit: Audit, output_dir: Path) -> tuple[Path, Path]:
    errors = sum(x["severity"] == "ERROR" for x in audit.issues)
    warnings = sum(x["severity"] == "WARNING" for x in audit.issues)
    if errors:
        state = "FAIL"
    elif audit.checked["image_files"] != "pass" or audit.checked["duplicate_binaries"] != "pass":
        state = "PARTIAL_PASS_PENDING_BINARY_CHECKS"
    else:
        state = "PASS"
    report = {"generated_utc": datetime.now(timezone.utc).isoformat(), "status": state,
              "checks": audit.checked, "metrics": audit.metrics,
              "error_count": errors, "warning_count": warnings, "issues": audit.issues}
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "validation_report.json"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    markdown = ["# Relatório de validação — dataset de área foliar", "",
                f"**Estado:** {state}", f"**Gerado (UTC):** {report['generated_utc']}",
                f"**Erros:** {errors} | **Avisos:** {warnings}", "", "## Camadas verificadas", ""]
    markdown += [f"- **{k}:** {v}" for k, v in audit.checked.items()]
    markdown += ["", "## Métricas", "", "```json", json.dumps(audit.metrics, ensure_ascii=False, indent=2), "```", "", "## Ocorrências", ""]
    if audit.issues:
        markdown += [f"- **{i['severity']} · {i['code']}** {i['record']}: {i['message']}" for i in audit.issues]
    else:
        markdown.append("Nenhuma ocorrência.")
    markdown += ["", "**Observação:** o status parcial NÃO comprova integridade binária das imagens. Além disso, a validação técnica não substitui autorizações, créditos ou licenciamento científico.", ""]
    md_path = output_dir / "validation_report.md"
    md_path.write_text("\n".join(markdown), encoding="utf-8")
    return json_path, md_path


def main() -> int:
    p = argparse.ArgumentParser(description="Validação do dataset científico de área foliar, sem alterar fontes")
    p.add_argument("--metadata-dir", type=Path, required=True, help="Pasta com os quatro arquivos CSV originais")
    p.add_argument("--images-dir", type=Path, help="Pasta com os 205 JPEGs canônicos, sem duplicações")
    p.add_argument("--output-dir", type=Path, default=Path("validation_output"))
    p.add_argument("--check-checksums", type=Path, help="Manifesto SHA256SUMS.txt previamente publicado")
    p.add_argument("--write-checksums", action="store_true", help="Gera SHA256SUMS.txt no diretório de saída")
    p.add_argument("--originals-inventory", type=Path, help="CSV opcional filename,path com 271 originais para comparar as 66 duplas")
    p.add_argument("--no-v1-counts", action="store_true", help="Desliga contagens congeladas da versão v1")
    args = p.parse_args()
    audit = Audit()
    tables = {}
    for key, file_name in FILE_NAMES.items():
        path = args.metadata_dir / file_name
        if not path.is_file():
            print(f"ERRO: CSV obrigatório não encontrado: {path}", file=sys.stderr)
            return 2
        records, cols = get_rows(path)
        lacking = REQUIRED[key] - cols
        if lacking:
            print(f"ERRO: {path.name} sem colunas: {sorted(lacking)}", file=sys.stderr)
            return 2
        tables[key] = records
    audit.metrics["metadata_sha256"] = {
        key: sha256_file(args.metadata_dir / fname)
        for key, fname in FILE_NAMES.items()
    }
    validate_metadata(audit, tables, enforce_profile=not args.no_v1_counts)
    if args.images_dir:
        if not args.images_dir.is_dir():
            audit.issue("ERROR", "IMAGE_DIR_MISSING", f"Pasta não encontrada: {args.images_dir}")
            audit.checked["image_files"] = "fail"
        else:
            args.output_dir.mkdir(parents=True, exist_ok=True)
            validate_images(audit, tables, args.images_dir, args.check_checksums, args.write_checksums, args.output_dir)
    elif args.write_checksums or args.check_checksums:
        audit.issue("ERROR", "IMAGES_REQUIRED", "--write-checksums e --check-checksums exigem --images-dir")
    if args.originals_inventory:
        if args.originals_inventory.is_file():
            verify_source_copies(audit, args.originals_inventory, {r["filename"] for r in tables["images"]})
        else:
            audit.issue("ERROR", "INVENTORY_MISSING", f"Inventário de cópias inexistente: {args.originals_inventory}")
    paths = write_reports(audit, args.output_dir)
    print(f"Relatórios: {paths[0]}, {paths[1]}")
    print(f"Camadas: {audit.checked}")
    print(f"Ocorrências: {len(audit.issues)} (erros: {sum(x['severity']=='ERROR' for x in audit.issues)})")
    return 1 if any(x["severity"] == "ERROR" for x in audit.issues) else 0


if __name__ == "__main__":
    raise SystemExit(main())