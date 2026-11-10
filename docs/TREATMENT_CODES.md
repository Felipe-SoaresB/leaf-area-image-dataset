# Códigos de tratamentos e abreviações

**Documentação v1.0.1 · Conteúdo científico da curadoria v1.0.0**

Este documento permite interpretar os rótulos das imagens e as colunas do dataset sem conhecimento prévio do experimento. As tabelas numéricas e os identificadores da v1.0.0 permanecem inalterados.

## Substratos

| Código nos dados | Substrato | Observação |
|---|---|---|
| `A` | **Areia** | Código usado nos registros curados |
| `V` | **Vermiculita** | Código normalizado |
| `v` | **Vermiculita** | Variante de maiúsculas/minúsculas encontrada na planilha; normalizada como `V` |
| `T` | **Terra** | O tipo/composição da terra não foi especificado nesta documentação |

A correspondência foi conferida pela planilha de planejamento original do TCC, que utiliza nomes completos de substrato, em conjunto com a aba `Metodologia` da planilha geral, que utiliza os códigos A/V/T. As massas de tubete para cada substrato coincidem entre essas fontes.

## Níveis de irrigação / tratamento

| Valor em `treatment_percent` (ou `percentual`) | Interpretação |
|---|---|
| `25` | Tratamento de irrigação equivalente a 25% da CRA de referência do substrato |
| `50` | 50% da CRA de referência |
| `75` | 75% da CRA de referência |
| `100` | 100% da CRA de referência |

**CRA**, no contexto de irrigação, designa a **capacidade de retenção de água** do substrato. O planejamento registra valores-alvo de massa do tubete para cada nível hídrico, específicos de areia, vermiculita e terra. O valor numérico não indica percentual de mistura entre substratos, percentual de folhas fotografadas ou medida da umidade instantânea no momento da captura.

São três substratos × quatro níveis = **12 combinações de tratamento possíveis**. A distribuição experimental foi declarada **DIC (Delineamento Inteiramente Casualizado)**. O conjunto de fotos é um recorte do experimento original, e não uma representação de todas as 546 mudas inicialmente plantadas.

**Exemplo:** `A` + `50` = amostra do substrato **areia**, no tratamento de irrigação de **50% da CRA**. Não significa “50% areia”.

## Identificadores e variáveis de imagem

| Nome / código | Interpretação |
|---|---|
| `image_id` | Identificador único do registro de uma fotografia |
| `filename` | Nome do JPEG |
| `sample_group_id` / `SGxxxx` | Identificador de uma mesma amostra/folha, que pode ter múltiplas fotografias |
| `retake` | Outra captura fotográfica da mesma amostra; não constitui nova amostra biológica independente |
| `substrate_code` / `substrato_normalizado` | Código de substrato A, V ou T |
| `treatment_percent` / `percentual` | Nível percentual de CRA aplicado como tratamento |
| `replicate_id` / `bandeja_repeticao` | Identificação combinada de bandeja e repetição, conservada como texto (ex.: `3-1`) |
| `imagej_sheet_row` / `sheet_row` | Número da linha correspondente na planilha das medições |
| `imagej_area_cm2` / `area_referencia_cm2` | Área foliar de referência medida no **ImageJ**, em **cm²** |
| `C` manuscrito | Identificação de `Coleto`, conforme mapeamento das fotografias |
| `Coleto` / `coleto` | Campo experimental referente ao coleto da muda; a característica específica e a unidade não estão explicitadas no protocolo disponibilizado |
| `MF` | Sigla presente nos dados originais, usualmente empregada para *massa fresca*; expansão e unidade aguardam confirmação da equipe experimental |
| `MS` | Sigla presente nos dados originais, usualmente empregada para *massa seca*; expansão e unidade aguardam confirmação da equipe experimental |
| `CRA` na **coluna da planilha `dados - folha`** | Campo numérico separado do `%` de tratamento. A planilha geral usa o cabeçalho `CPA` em seção foliar semelhante; **não presumir** que esse `CRA` tenha o mesmo significado da CRA de irrigação sem confirmação |
| `CPA` na planilha geral | Cabeçalho de variável foliar encontrado na planilha geral; expansão e unidade específicas ainda não confirmadas nos materiais analisados |

**Atenção à sigla CRA:** a **CRA expressa em percentuais 25/50/75/100** é a condição hídrica do experimento. A coluna numérica nomeada `CRA` em `dados - folha` é outro campo da planilha e **não deve ser interpretada automaticamente como o percentual da condição hídrica**.

## Estados e regras da curadoria

| Campo/valor | Uso |
|---|---|
| `mapping_status=confirmed` | Ligação da imagem com a amostra da planilha considerada confirmada |
| `mapping_status=unmapped` | Não foi possível estabelecer associação conclusiva |
| `reference_status=positive` | Há referência numérica positiva de área |
| `reference_status=zero` / `missing` | Valor nulo ou ausente na fonte; não implica que a folha tenha área física zero |
| `qc_status_source=pending` | Estado histórico sem homologação visual individual; não é aprovação nem rejeição |
| `reference_missing` | Fotografia de amostra sem área de referência utilizável |
| `non_sample` | Fotografia documental que não é uma amostra para medição |
| `invalid_capture` | Captura anteriormente classificada como inválida |
| `include_for_area_evaluation=yes` | Pertence à seleção quantitativa de referência positiva |
| `include_for_area_evaluation=no` | Não pertence à seleção quantitativa |
| `development` | Partição de desenvolvimento dos modelos |
| `final_test` | Partição de teste final, separada por grupo |
| `stratum` | Combinação codificada de substrato e nível de CRA |
| `canonical_filename` | Fotografia escolhida como representativa do grupo |
| `n_images` | Número total de fotografias do grupo |
| `extra_retake_images` | Quantidade de capturas extras do mesmo grupo |

## Fontes e delimitação

- Planilha original do experimento: **`TCC - versão original 13 maio 13h54.xlsx`**, com substratos escritos por extenso e cronograma de rega.
- Planilha geral da pesquisa: **`Copy of Planilha Geral TCC Tatiane`**, abas `Metodologia`, `Randomização` e `Folha`.
- Planilha de medições: **`dados - folha`**.
- Documentação da curadoria: `metadata/`, `docs/PROVENANCE.md` e `docs/EXCLUSIONS_AND_LIMITATIONS.md`.

Os nomes dos arquivos de origem são informados para rastreabilidade; endereços privados do Google Drive não são necessários para interpretar o conjunto. Nenhuma coluna ou valor numérico da v1.0.0 foi modificado. Siglas auxiliares cuja expansão ou unidade não foi confirmada continuam registradas, sem interpretação inventada.
