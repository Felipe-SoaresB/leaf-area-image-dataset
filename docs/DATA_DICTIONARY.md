# Dicionário de dados — v1.0.0

## release/images_v1.csv — 205 linhas (uma por fotografia)

| Coluna | Definição |
|---|---|
| `image_id` | Identificador estável da fotografia |
| `filename` | Nome do JPEG correspondente |
| `capture_date`, `capture_time` | Data e hora declaradas da captura |
| `sample_group_id` | Identificador da amostra/folha; pode ocorrer em múltiplas fotos (retakes); vazio em fotos documentais/inválidas |
| `substrate_code` | Código normalizado do substrato conforme fonte |
| `treatment_percent` | Percentual de tratamento conforme fonte |
| `replicate_id` | Identificador de bandeja/repetição da fonte |
| `imagej_sheet_row` | Linha de referência da planilha ImageJ original |
| `imagej_area_cm2` | Área de referência em cm²; vazio/zero não significa necessariamente medição biológica nula |
| `reference_status` | Situação de referência: positiva, zero, ausente ou vazio |
| `mapping_status` | Situação de vinculação com a planilha na curadoria |
| `qc_status_source` | Status histórico de curadoria; `pending` NÃO significa certificado de qualidade nem rejeição |
| `include_for_area_evaluation` | `yes` ou `no`, copiado da decisão de inclusão para avaliação quantitativa |

## release/area_groups_v1.csv — 177 linhas (uma por grupo de área utilizável)

| Coluna | Definição |
|---|---|
| `sample_group_id` | Identificador da amostra/grupo |
| `canonical_image_id`, `canonical_filename` | Fotografia canônica associada |
| `substrate_code`, `treatment_percent` | Tratamento registrado |
| `imagej_area_cm2` | Área positiva de referência em cm² do grupo |
| `n_images` | Quantidade de fotos registradas para o grupo |
| `extra_retake_images` | Capturas extras da mesma amostra |
| `stratum` | Estrato derivado de substrato e tratamento |
| `split` | `development` ou `final_test`, separados por grupo |
| `selection_rule` | Regra documentada de seleção da captura canônica |

## Arquivos preservados em metadata/

`tabela_mestre_v1.csv` é a fonte integral de 205 fotografias (contém IDs do Drive, notas de mapeamento e decisões de exclusão). `imagens_drive.csv` documenta arquivos físicos, IDs e duplicações. `referencias_imagej.csv` contém os 291 registros originais, incluindo valores não aproveitados em análise de imagens. `divisao_experimental_v1.csv` define os 177 grupos elegíveis e partições.

As variáveis auxiliares `coleto`, `MF`, `MS` e `CRA` têm registros de origem cuja definição/unidade completa não faz parte do escopo desta versão; por isso não foram adicionadas às tabelas portáteis de área foliar.
