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

A distribuição elimina IDs privados do Drive e notas livres de curadoria; os originais permanecem restritos no repositório de preparação. **Não** tornar a totalidade do repositório privado atual pública: arquivos sensíveis constam do histórico Git. Para publicação, iniciar um depósito com histórico limpo contendo apenas os arquivos desta pasta, documentação selecionada, licença aprovada e JPEGs sem EXIF/GPS.

As imagens ainda não integram este repositório. A versão v1.0.0 é o congelamento dos dados e dos vínculos; disponibilização pública e DOI serão registrados em ato próprio.
