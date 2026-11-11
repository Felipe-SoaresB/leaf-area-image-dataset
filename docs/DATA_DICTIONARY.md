# Dicionário de dados — documentação v1.0.1 (dados v1.0.0)

## release/images_v1.csv — 198 linhas na edição pública corrigida v1.0.3 (uma por fotografia)

| Coluna | Definição |
|---|---|
| `image_id` | Identificador estável da fotografia |
| `filename` | Nome do JPEG correspondente |
| `capture_date`, `capture_time` | Data e hora declaradas da captura |
| `sample_group_id` | Identificador da amostra/folha; pode ocorrer em múltiplas fotos (retakes); vazio em fotos documentais/inválidas |
| `substrate_code` | A = areia; V = vermiculita; T = terra. O código original `v` foi normalizado como V |
| `treatment_percent` | Nível da capacidade de retenção de água (CRA) do substrato: 25, 50, 75 ou 100% — não é percentual de mistura |
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
| `substrate_code`, `treatment_percent` | Substrato e nível percentual de CRA do tratamento (ver tabela de códigos) |
| `imagej_area_cm2` | Área positiva de referência em cm² do grupo |
| `n_images` | Quantidade de fotos registradas para o grupo |
| `extra_retake_images` | Capturas extras da mesma amostra |
| `stratum` | Estrato derivado de substrato e tratamento |
| `split` | `development` ou `final_test`, separados por grupo |
| `selection_rule` | Regra documentada de seleção da captura canônica |

## Coleção histórica e arquivos de curadoria

Os arquivos de origem da curadoria estão em `metadata/`. A coleção histórica possuía 205 fotos; a edição pública corrigida distribui 198, após excluir sete fotos documentais classificadas como `non_sample` sem autorização comprovada para redistribuição. Essas sete não faziam parte da análise quantitativa. A área pública de distribuição é representada pelos arquivos em `release/`; não reutilize contagens/hashes da edição histórica como se fossem desta edição.

`tabela_mestre_v1.csv` e `imagens_drive.csv` refletem a edição corrente e não contêm as sete linhas removidas. `referencias_imagej.csv` conserva 291 registros da planilha de origem. `divisao_experimental_v1.csv` preserva os 177 grupos elegíveis e suas partições.

O significado dos tratamentos, a normalização de `v` para `V`, os estados de curadoria e as abreviações estão reunidos em [`TREATMENT_CODES.md`](TREATMENT_CODES.md). As variáveis auxiliares `coleto`, `MF`, `MS` e `CRA` da planilha foliar não foram introduzidas nas tabelas portáteis; algumas ainda necessitam confirmação de expansão ou unidade. O `CRA` numérico da planilha foliar **não deve ser confundido** com o percentual de CRA usado na irrigação.
