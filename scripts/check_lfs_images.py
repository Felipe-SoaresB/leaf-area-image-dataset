#!/usr/bin/env python3
"""Valida arquivos JPEG reais baixados via Git LFS com o manifesto da distribuição.

Não modifica imagens nem metadados. Use após 'git lfs pull'.
"""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path

from PIL import Image, UnidentifiedImageError

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_IMAGES = 198
IMAGE_DIR = ROOT / "images" / "data"
MANIFEST = ROOT / "checksums" / "SHA256_RELEASE_NO_EXIF.txt"
INDEX = ROOT / "release" / "images_v1.csv"


def sha256_file(path: Path) -> str:
    sha = hashlib.sha256()
    with path.open("rb") as stream:
        for data in iter(lambda: stream.read(1024 * 1024), b""):
            sha.update(data)
    return sha.hexdigest()


def main() -> None:
    manifest: dict[str, str] = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, filename = line.strip().split(None, 1)
        filename = filename.strip()
        assert len(digest) == 64 and all(c in "0123456789abcdef" for c in digest), f"Hash inválido: {filename}"
        assert filename not in manifest, f"Nome duplicado no manifesto: {filename}"
        assert "/" not in filename and chr(92) not in filename, f"Nome inseguro: {filename}"
        manifest[filename] = digest
    assert len(manifest) == EXPECTED_IMAGES, f"Manifesto contém {len(manifest)} imagens, esperadas {EXPECTED_IMAGES}"

    with INDEX.open("r", encoding="utf-8-sig", newline="") as f:
        idx = list(csv.DictReader(f))
    indexed = [r["filename"] for r in idx]
    assert len(indexed) == EXPECTED_IMAGES and set(indexed) == set(manifest), "Índice de imagens difere do manifesto"

    jpeg_files = list(IMAGE_DIR.glob("*.jpg"))
    available = {p.name for p in jpeg_files}
    assert len(jpeg_files) == EXPECTED_IMAGES and available == set(manifest), (
        f"Imagens reais: {len(jpeg_files)}, ausentes: {sorted(set(manifest)-available)}, "
        f"extras: {sorted(available-set(manifest))}"
    )

    for i, (filename, expected) in enumerate(sorted(manifest.items()), start=1):
        path = IMAGE_DIR / filename
        with path.open("rb") as f:
            header = f.read(80)
        assert header.startswith(bytes.fromhex("ffd8")), (
            f"{filename}: não é JPEG real. Execute 'git lfs pull' (ponteiro LFS detectado?)."
        )
        actual = sha256_file(path)
        assert actual == expected, f"{filename}: SHA-256 divergente"
        try:
            with Image.open(path) as image:
                assert image.format == "JPEG" and image.mode == "RGB", f"{filename}: formato/cor inesperados"
                assert not image.info.get("exif"), f"{filename}: EXIF ainda incorporado"
                assert not image.getexif().get(34853), f"{filename}: GPS presente"
                assert image.size in ((4000, 3000), (3000, 4000)), f"{filename}: resolução inesperada"
                image.verify()
        except (OSError, UnidentifiedImageError) as exc:
            raise AssertionError(f"{filename}: JPEG inválido: {exc}") from exc
        if i % 50 == 0 or i == EXPECTED_IMAGES:
            print(f"Verificados: {i}/{EXPECTED_IMAGES}", flush=True)
    print("PASS: 198 JPEGs reais, correspondentes aos metadados, SHA-256 correto e sem EXIF/GPS.")


if __name__ == "__main__":
    main()
