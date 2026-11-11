# Guia de atualização do Zenodo — v1.0.3

**O registro `10.5281/zenodo.24122476` deve permanecer em Draft.** Este guia descreve os arquivos locais preparados; nenhum upload, substituição ou publicação foi realizado.

## Pacote preparado
Em `leaf-area_images_v1.0.3.zip`, há somente os 198 JPEGs públicos e seu manifesto SHA-256. `leaf_area_dataset_documentation_v1.0.3.zip` contém CSVs corrigidos, cartão, dicionário, contexto, exclusões, proveniência, README, licença e citação. Também foram preparados CSVs independentes `images_v1.0.3.csv` e `area_groups_v1.0.3.csv`. Um ZIP combinado para auditoria local contém imagens, CSVs e documentação numa única árvore. `validation_report.json` e `SHA256_PACKAGE.txt` registram hashes e validação.

## Passos, somente após autorização do mantenedor
1. Conferir este pacote com uma segunda pessoa e confirmar autorização/licença para cada arquivo distribuído.
2. Resolver a exposição do GitHub/LFS e confirmar a edição pública do branch.
3. Abrir o Draft sem clicar em **Publish**. Registrar localmente a lista e hashes dos arquivos atuais antes de qualquer alteração.
4. Somente após autorização explícita para upload, substituir os arquivos de dados/documentação do Draft pelos quatro artefatos v1.0.3, atualizar descrição e versão para 198/181/177/191 e preservar DOI reservado.
5. Baixar novamente cada arquivo do Draft, validar SHA-256 e conteúdo, confirmar os mesmos quatro arquivos e conferir a descrição. Manter o registro em Draft para revisão.
6. Não clicar em Publish sem autorização expressa posterior.

A descrição pública deve diferenciar 205 imagens históricas de 198 na edição corrigida, registrar que a redução remove sete fotografias documentais sem impacto na análise quantitativa e preservar a divisão por grupo de 44/133. Não publicar a lista nominal dos arquivos retirados.
