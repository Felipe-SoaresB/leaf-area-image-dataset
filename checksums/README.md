# Manifestos de integridade

`SHA256SUMS.txt` será criado a partir dos JPEGs reais por `scripts/validate_dataset.py --images-dir ... --write-checksums`. Ainda não existe manifesto verificado para as 205 fotos.
Nenhum SHA-256 de JPEG deve ser fabricado a partir de nomes, IDs ou tamanhos registrados.


## Auditoria de 22/10/2026

Os 205 hashes SHA-256 dos arquivos canônicos já foram calculados; as 66 duplas foram confrontadas e são binariamente idênticas. O manifesto individual foi gerado como arquivo local `SHA256SUMS.txt`, com SHA-256 do próprio manifesto `030196dd02140167a45510be4ee32905261f164774ea8401f4b1cd53278570c6`. **O manifesto completo ainda precisa ser sincronizado para este repositório.** Consulte `reports/INTEGRITY_AUDIT_2026-10-22.md`.
