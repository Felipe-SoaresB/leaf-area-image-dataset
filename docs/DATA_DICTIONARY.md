# Dicionário de dados (preliminar)

## tabela_mestre_v1.csv

Cada linha representa uma fotografia, inclusive retakes e exclusões. `image_id` identifica o registro de imagem; `filename` é o arquivo JPEG; `drive_id` é o ID do objeto de origem; `capture_date` e `capture_time` são a data/hora curadas; `sample_group_id` agrupa diferentes fotografias da mesma amostra/folha.
`substrato_original` e `substrato_normalizado` são códigos do substrato; `percentual` é o nível registrado do tratamento; `bandeja_repeticao` identifica bandeja/repetição; `coleto` é uma medida/campo bruto com divergências de transcrição documentadas; `sheet_row` referencia a linha da planilha ImageJ.
`area_referencia_cm2` representa a referência de área em cm²; `area_status` distingue `positive`, `zero`, `missing` e valor vazio; `mapping_status`, `mapping_confidence` e `mapping_notes` documentam o vínculo entre fotografia e planilha.
`qc_status` indica o status da imagem, mas `pending` NÃO significa aprovação final da qualidade; `exclude_from_analysis` e `exclusion_reason` documentam exclusões.

## imagens_drive.csv

Uma linha por nome distinto: `filename`, `capture_date`, `capture_time`, `drive_file_count`, `canonical_drive_id`, `size_bytes`, `duplicate_suspected` e `all_drive_ids`. `size_bytes` não comprova identidade binária; são necessários hashes SHA-256.

## referencias_imagej.csv

Uma linha por medição da planilha de origem: `sheet_row`, `substrato_original`, `substrato_normalizado`, `percentual`, `bandeja_repeticao`, `coleto`, `MF`, `MS`, `CRA`, `area`, `area_status`, `sample_key`. A área é tratada como referência em cm². As unidades de MF/MS/CRA devem ser confirmadas no protocolo original. Zeros associados a ausência de leitura não podem ser interpretados como área biológica zero.

## divisao_experimental_v1.csv

Uma linha por grupo elegível: `sample_group_id`, `canonical_image_id`, `canonical_filename`, `substrato`, `percentual`, `area_referencia_cm2`, `n_images`, `extra_retake_images`, `stratum`, `split`, `selection_rule`.
`split` vale `development` (44 grupos) ou `final_test` (133 grupos). Separação é por grupo, nunca por retake. `canonical_*` corresponde à primeira foto canônica do grupo.
