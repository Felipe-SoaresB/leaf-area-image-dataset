# Índices de distribuição — edição pública corrigida v1.0.3

Esta edição pública corrige a privacidade da distribuição histórica de imagens. A coleção histórica v1.0.2 tinha 205 JPEGs; a edição pública corrigida contém 198, após retirar sete fotografias documentais sem comprovação de autorização para redistribuição. As sete eram `non_sample`, não integravam grupos de folhas nem avaliação quantitativa. Áreas, tratamentos, identificadores restantes, dados ImageJ e partições não foram alterados.

| Arquivo | Registros | Unidade |
|---|---:|---|
| `images_v1.csv` | 198 | fotografia pública |
| `area_groups_v1.csv` | 177 | grupo com referência positiva válida |

O índice de imagens mantém os status originais para os 198 registros distribuídos. São 191 imagens elegíveis para análise e sete não elegíveis por outros critérios já existentes. Os 177 grupos válidos mantêm a divisão de 44 grupos de desenvolvimento e 133 de teste final.

`substrate_code` usa A = Areia, V = Vermiculita e T = Terra. `treatment_percent` representa nível relativo à capacidade de retenção de água do substrato. Consulte `docs/DATA_DICTIONARY.md` e `docs/TREATMENT_CODES.md`.

Os CSVs não contêm nomes das imagens retiradas nem IDs de Drive. As fotografias públicas sem EXIF/GPS ficam em `images/data/` via Git LFS. O manifesto correspondente é `checksums/SHA256_RELEASE_NO_EXIF.txt`. A cópia de trabalho histórica do repositório, seus commits antigos e o depósito Zenodo em Draft ainda exigem saneamento independente; esta edição não os apaga retroativamente.
