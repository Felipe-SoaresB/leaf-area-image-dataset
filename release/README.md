# Dados de distribuição — curadoria v1.0.0, documentação v1.0.1

Esta pasta reúne o **núcleo portátil do dataset** para análise de área foliar. São derivados conservadores dos quatro CSVs-fonte mantidos em `../metadata/`: nenhuma medição foi recalculada e nenhuma fotografia foi reclassificada.

| Arquivo | Linhas | Unidade |
|---|---:|---|
| `images_v1.csv` | 205 | registro de fotografia |
| `area_groups_v1.csv` | 177 | grupo/folha associado a uma referência positiva |

## Legenda dos tratamentos

- `substrate_code`: A = **Areia**, V = **Vermiculita**, T = **Terra** (`v` original é normalizado como V).
- `treatment_percent`: 25, 50, 75 ou 100% da **CRA (capacidade de retenção de água)** do substrato; não indica composição da mistura.
- Consulte [`docs/TREATMENT_CODES.md`](../docs/TREATMENT_CODES.md) para siglas, estados e unidades conhecidas.

## Vínculo e interpretação

A chave da fotografia é `image_id`, e `filename` referencia a imagem JPEG. `sample_group_id` relaciona múltiplas fotos da mesma amostra. `imagej_area_cm2` representa a referência de área em centímetros quadrados quando disponível.

`include_for_area_evaluation` indica seleção realizada a partir do campo original `exclude_from_analysis`, **não** uma conclusão de inspeção visual. `qc_status_source` conserva os estados `pending`, `reference_missing`, `non_sample` e `invalid_capture` da origem. Os casos excluídos permanecem no índice para rastreabilidade.

`area_groups_v1.csv` contém exatamente os 177 grupos ligados a referência utilizável. A coluna `split` contém `development` ou `final_test`. Retakes devem permanecer juntos pelo `sample_group_id`; a captura canônica é indicada em `canonical_filename`.

## Integridade, privacidade e contexto

Estes **dois CSVs de distribuição** eliminam IDs internos do Drive e notas livres de curadoria. **Atenção:** a pasta `../metadata/` já está presente no repositório público e ainda contém IDs internos de Drive e anotações históricas; o histórico Git também requer avaliação de sanitização. Isso não é corrigido apenas editando esta documentação. Para uma publicação científica arquivada/DOI, preparar um pacote limpo com estes CSVs, documentação revisada, licença aprovada e os JPEGs já preparados sem EXIF/GPS.

As **205 imagens JPEG sem EXIF** estão em `../images/data/` via Git LFS. A versão v1.0.0 é o congelamento dos dados e dos vínculos, enquanto a revisão v1.0.2 registrou a inclusão das imagens. O repositório está público no GitHub, mas **não existe DOI nem release formal**, e a publicação definitiva depende das pendências indicadas em `../docs/RELEASE_CHECKLIST.md`.
