# Histórico de versões

## v1.0.3 — edição pública corrigida, publicada no Zenodo em 11/11/2026

- Preparada distribuição de 198 JPEGs após retirar sete fotografias documentais sem comprovação de autorização para redistribuição.
- Mantidos 181 grupos, 177 grupos ImageJ elegíveis, 191 fotografias quantitativamente elegíveis e divisão de 44/133 grupos; nenhuma área ou tratamento foi alterado.
- Atualizados índices públicos, hashes, verificadores e documentação para distinguir a coleção histórica de 205 imagens desta edição corrigida.
- Edição pública distribuída no Zenodo em quatro arquivos v1.0.3, com validação de integridade informada pelo responsável; DOI: [10.5281/zenodo.24122476](https://doi.org/10.5281/zenodo.24122476).
- A correção foi incorporada à `main` sem reescrita histórica. Objetos antigos Git/LFS podem permanecer acessíveis; a edição v1.0.3 não os inclui.

## v1.0.2 — 09/11/2026 (imagens no Git LFS)

- Adicionadas **205 fotografias JPEG sem EXIF/GPS** à pasta `images/data/` usando Git LFS.
- Manifesto `checksums/SHA256_RELEASE_NO_EXIF.txt` incluído e correspondente às 205 fotografias.
- O GitHub Actions baixou **os 205 objetos LFS completos**, verificou os hashes SHA-256, formato JPEG RGB, resolução, ausência de EXIF e concordância com o índice; execução aprovada.
- Atualizados README, instruções de download e checklist de publicação.
- Sem alteração das medições ImageJ, dos quatro CSVs originais, das divisões experimentais ou dos critérios de inclusão.
- O DOI ainda não existia naquele registro. A frase original que indicava repositório privado era incorreta: o repositório `main` estava público. A edição corrigida v1.0.3 documenta a exposição histórica e sua pendência de saneamento.


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
