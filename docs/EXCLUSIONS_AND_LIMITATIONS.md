# Critérios de inclusão, exclusões e limites de interpretação

## Edição pública corrigida v1.0.3
A edição pública contém 198 fotografias e 181 grupos mapeados. Os 177 grupos com referência de área utilizável correspondem a 191 fotografias quantitativamente elegíveis. A divisão experimental preserva 44 grupos em `development` e 133 em `final_test`.

A edição histórica v1.0.2 continha 205 fotografias: 14 não integravam a avaliação quantitativa, entre elas sete fotos documentais sem unidade de área e uma captura inválida por superexposição. Na edição corrigida, as sete fotos documentais sem autorização comprovada foram removidas integralmente dos arquivos, índices e manifesto ativos. Restam sete JPEGs distribuídos fora da avaliação quantitativa: seis sem referência válida e uma captura inválida. A lista nominal das imagens retiradas está em um registro local privado, fora do repositório e do pacote público.

As imagens retiradas eram classificadas no índice histórico como `non_sample` e `include_for_area_evaluation=no`. Elas não tinham grupo ou área associados. A remoção não altera as 191 observações elegíveis, as áreas, os tratamentos, os identificadores restantes nem o split 44/133.

## Unidade e interpretação
`image_id` identifica uma fotografia; `sample_group_id` identifica uma unidade amostral/folha, que pode ter retakes. Avaliações quantitativas devem usar os 177 grupos com referência utilizável e manter retakes do mesmo grupo na mesma partição. Referências zero ou ausentes podem representar falta de leitura, não área biológica nula.

## Integridade e qualidade
A integridade dos JPEGs é controlada por SHA-256. A triagem exploratória de nitidez, exposição e contraste não equivale à aprovação visual individual das imagens. Os status `pending` preservam o histórico de curadoria e não certificam cada pixel nem a referência ImageJ.

## Proveniência e limitações
As áreas publicadas são transcritas de registros ImageJ, com associações documentadas, e não foram medidas novamente nesta edição. Há diferenças de transcrição no campo auxiliar `coleto`, excluído dos CSVs de distribuição. O protocolo completo de aquisição/calibração e a associação individual de cada muda às fotos não estão disponíveis. Não extrapolar resultados para todas as mudas do experimento ou condições não amostradas.

## Privacidade e distribuição
As cópias públicas foram preparadas sem EXIF/GPS; isso não remove texto ou pessoas visíveis nos pixels. A correção de v1.0.3 não apaga cópias existentes em histórico Git, refs, objetos Git LFS, caches ou no Zenodo Draft. A sanitização retroativa do GitHub exige plano próprio e, dependendo do histórico/armazenamento, suporte do GitHub. O Draft do Zenodo permanece sem alterações até autorização explícita.
