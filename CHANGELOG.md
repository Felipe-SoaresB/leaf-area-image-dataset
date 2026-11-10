# Histórico de versões

## v1.0.1 — 09/11/2026 (documentação)

- Acrescentado dicionário explícito de códigos: A = Areia, V = Vermiculita, T = Terra (normalização de `v`).
- Documentado que 25/50/75/100 são níveis de CRA na irrigação, sem confundi-los com proporções de mistura do substrato.
- Esclarecidas abreviações da tabela foliar, estados de inclusão, partições e relação fotografia–grupo–ImageJ.
- **Sem mudança nas 205 fotografias, nos quatro CSVs-fonte ou nos valores das duas tabelas de distribuição.** O snapshot `snapshot/v1.0.0` permanece congelado.


## v1.0.0 — 09/11/2026

**Congelamento da curadoria do conjunto de dados.** Nenhum valor dos quatro CSVs de origem foi reescrito nesta versão.

- Estrutura consolidada: 205 fotos distintas, 181 grupos identificados, 177 grupos com área de referência utilizável.
- Registros científicos derivados e portáteis em `release/images_v1.csv` e `release/area_groups_v1.csv`.
- Divisão experimental preservada por grupo: 44 development e 133 final_test.
- Documentação de aquisição, referências ImageJ, exclusões e decisões de curadoria.
- Integridade de originais por manifesto SHA-256 e cópias redundantes verificadas (auditoria 22/10/2026).
- Indicação explícita de que imagens para distribuição, DOI e licença ainda não foram formalizados.
- Testes automáticos para garantir consistência entre CSVs originais e representação distribuível.

**Escopo:** versão da estrutura, dos metadados e das regras de vinculação. Não atribui revisão visual individual, novas medidas biológicas ou verificação independente de taxonomia.

## Registro anterior — 22/10/2026

- Primeira importação auditada dos quatro CSVs e documentação.
- Auditoria binária dos JPEGs e identificação de metadados GPS.
- Triagem automática exploratória de qualidade (sem aprovação/reprovação de novas fotografias).
