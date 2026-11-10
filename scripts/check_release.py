#!/usr/bin/env python3
"""Compara projeção de distribuição v1.0.0 com metadados originais, sem reclassificar registros."""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def load(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

master = load(ROOT / "metadata" / "tabela_mestre_v1.csv")
groups = load(ROOT / "metadata" / "divisao_experimental_v1.csv")
release_images = load(ROOT / "release" / "images_v1.csv")
release_groups = load(ROOT / "release" / "area_groups_v1.csv")

assert len(master) == len(release_images) == 205, "Contagem de imagens inesperada"
assert len(groups) == len(release_groups) == 177, "Contagem de grupos inesperada"
assert len({r["image_id"] for r in release_images}) == 205, "image_id duplicado"
assert len({r["filename"] for r in release_images}) == 205, "filename duplicado"
assert len({r["sample_group_id"] for r in release_groups}) == 177, "grupo duplicado"

byid = {r["image_id"]: r for r in master}
for row in release_images:
    original = byid[row["image_id"]]
    rules = {
        "filename": "filename",
        "capture_date": "capture_date",
        "capture_time": "capture_time",
        "sample_group_id": "sample_group_id",
        "substrate_code": "substrato_normalizado",
        "treatment_percent": "percentual",
        "replicate_id": "bandeja_repeticao",
        "imagej_sheet_row": "sheet_row",
        "imagej_area_cm2": "area_referencia_cm2",
        "reference_status": "area_status",
        "mapping_status": "mapping_status",
        "qc_status_source": "qc_status",
            }
    for pub, src in rules.items():
        assert row[pub] == original[src], f"{row['image_id']}: diferença em {pub}"
    assert row["include_for_area_evaluation"] == ("yes" if original["exclude_from_analysis"] == "no" else "no"), f"{row['image_id']}: inclusão invertida"
assert sum(r["include_for_area_evaluation"] == "yes" for r in release_images) == 191
assert sum(r["include_for_area_evaluation"] == "no" for r in release_images) == 14
src_groups = {r["sample_group_id"]: r for r in groups}
for r in release_groups:
    s = src_groups[r["sample_group_id"]]
    fields = {
        "canonical_image_id": "canonical_image_id",
        "canonical_filename": "canonical_filename",
        "substrate_code": "substrato",
        "treatment_percent": "percentual",
        "imagej_area_cm2": "area_referencia_cm2",
        "n_images": "n_images",
        "extra_retake_images": "extra_retake_images",
        "stratum": "stratum",
        "split": "split",
        "selection_rule": "selection_rule",
    }
    for k, v in fields.items():
        assert r[k] == s[v], f"{r['sample_group_id']}: diferença em {k}"
    assert r["canonical_image_id"] in byid
    assert byid[r["canonical_image_id"]]["sample_group_id"] == r["sample_group_id"]
    assert float(r["imagej_area_cm2"]) > 0
    assert byid[r["canonical_image_id"]]["exclude_from_analysis"] == "no"
assert sum(r["split"] == "development" for r in release_groups) == 44
assert sum(r["split"] == "final_test" for r in release_groups) == 133
for path in (ROOT / "release" / "images_v1.csv", ROOT / "release" / "area_groups_v1.csv"):
    for blocked in ("drive_id", "canonical_drive_id", "all_drive_ids"):
        assert blocked not in path.read_text(encoding="utf-8-sig").lower(), f"ID de Drive em {path}"
print("PASS: 205 imagens, 177 grupos, 191 imagens elegíveis, 44/133 grupos; projeção equivalente à origem.")
