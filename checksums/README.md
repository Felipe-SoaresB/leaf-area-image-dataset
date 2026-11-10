# Integridade do conjunto de imagens

- `SHA256_ORIGINALS.txt`: 205 hashes SHA-256 das fotografias JPEG canônicas na origem, auditados em 22/10/2026.
- O pacote local de triagem contém `SHA256_RELEASE_NO_EXIF.txt`, com 205 hashes **distintos** para as cópias que tiveram EXIF removido. Esse manifesto deve acompanhar o futuro depósito das fotografias de distribuição.
- Há também relatório de igualdade binária de 66 pares redundantes na origem, `reports/INTEGRITY_AUDIT_2026-10-22.md`.

**Atenção:** o hash do JPEG original não coincide necessariamente com o hash do arquivo sanitizado. Devem ser conservados e identificados separadamente, sem misturar objetos de versões diferentes.

O SHA-256 do arquivo `SHA256_ORIGINALS.txt`, conforme auditoria de origem, é `030196dd02140167a45510be4ee32905261f164774ea8401f4b1cd53278570c6`.
