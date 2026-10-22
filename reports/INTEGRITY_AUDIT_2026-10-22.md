# Auditoria de integridade binária — Dataset Foliar v1.0

**Data:** 22 de outubro de 2026  
**Estado:** Integridade binária comprovada; revisão científica e publicação ainda pendentes.

## Fontes

A pasta Fotos do Google Drive (repositório original de pesquisa) foi listada novamente, e todos os 271 objetos correspondem aos IDs, nomes, multiplicidades e tamanhos declarados em `metadata/imagens_drive.csv`. O repositório de metadados está privado.

## Método

Foram obtidos via conector autenticado os JPEGs identificados por `canonical_drive_id` (205 nomes). Cada arquivo foi aberto, verificado e integralmente decodificado com Pillow; calculou-se seu SHA-256 binário. Os 66 segundos arquivos com nome repetido, identificados pelo outro ID em `all_drive_ids`, foram baixados e comparados ao original canônico preservado separadamente, por SHA-256.

## Resultados verificados

| Teste | Resultado |
|---|---|
| Objetos existentes no Drive | 271 |
| Nomes distintos de JPEG | 205 |
| Pares de nomes repetidos | 66 |
| Fotografias canônicas baixadas, abertas e decodificadas | 205/205 |
| Falhas de decodificação | 0 |
| Arquivos JPEG RGB | 205/205 |
| EXIF: fabricante e modelo | motorola / moto g(20), em 205/205 |
| Resolução 4000×3000 | 104 |
| Resolução 3000×4000 | 101 |
| SHA-256 únicos entre fotos de nomes distintos | 205 |
| Total das cópias canônicas | 579.166.838 bytes |
| Duplas confrontadas por SHA-256 | 66/66 |
| Duplas com conteúdo diferente | **0** |

O manifesto local `SHA256SUMS.txt` contém 205 linhas; seu próprio SHA-256 é:

`030196dd02140167a45510be4ee32905261f164774ea8401f4b1cd53278570c6`

**Resultado: APROVADO para integridade binária.**

## Evidências geradas

Foram gerados `SHA256SUMS.txt`, `DUPLICATE_PAIR_SHA256.csv`, `image_audit_details.json` e relatório de auditoria. Estes arquivos foram disponibilizados ao pesquisador como um pacote de evidências; a sincronização do conteúdo completo dos manifestos com este repositório permanece pendente.

## O que esta auditoria NÃO valida

- A qualidade visual de todas as folhas, recorte experimental, iluminação e condições de aquisição; 191 linhas permanecem com `qc_status=pending`.
- A correção biológica das associações entre folha, amostra e linha ImageJ, ou a exatidão dos valores de área.
- Privacidade/adequação para publicação dos metadados EXIF e dos IDs internos de Google Drive.
- Direitos de terceiros, licença de distribuição final e aprovação para depósito em Zenodo.

**Nenhum JPEG foi adicionado ao GitHub ou publicado.** A mudança no repositório resume a evidência binária sem modificar os dados de origem.
