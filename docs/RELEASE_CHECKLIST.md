# Estado da curadoria e preparação de publicação — v1.0.0

## Versão de curadoria: concluída
- [x] Autores e autorização pública declarados pelos dois coautores.
- [x] Inventário dos arquivos e associação com ImageJ conferidos.
- [x] Quatro CSVs preservados em `metadata/` com Git blob SHA idêntico à origem.
- [x] 205 JPEGs canônicos e 66 duplicações confrontados por SHA-256.
- [x] Seleção de 177 grupos e divisão experimental preservadas.
- [x] Limites de referência e exclusões descritos sem alterar estados originais.
- [x] Metadados transportáveis de distribuição derivados sem IDs do Drive.
- [x] Versionamento e dicionário de dados definidos.
- [x] Triagem automática registrada, sem alegar aprovação visual individual.

## Disponibilização científica: etapa separada
- [ ] Selecionar e ratificar licença de dados/imagens com ambos os coautores; definir licença do código.
- [ ] Preparar e revisar o pacote efetivo dos 205 JPEGs **sem EXIF/GPS**, comparando hashes com o manifesto de distribuição.
- [ ] Conferir informações visíveis nos pixels antes da divulgação.
- [ ] Depositar os arquivos com DOI (por exemplo Zenodo) e atualizar a citação com identificadores reais.
- [ ] Criar histórico público limpo, sem os IDs privados de Drive presentes no repositório de preparação.
- [ ] Revisar os requisitos oficiais de APC e preparar documentação comprobatória, caso se deseje pontuação.

Não há exigência adotada de revisar manualmente cada uma das 191 fotos para **congelar os dados na v1.0.0**. Caso uma revisão individual seja realizada posteriormente, ela deverá ser documentada como uma alteração versionada. Congelamento privado não equivale a publicação com DOI.

## Transferência das imagens para GitHub
- [x] Verificar as 205 cópias de distribuição sem EXIF e os respectivos hashes SHA-256.
- [x] Configurar Git LFS exclusivamente para `images/data/*.jpg`.
- [x] Recebido envio informado pelo usuário; confirmadas as 205 entradas Git LFS em `images/data/` e o manifesto com 205 nomes.
- [x] Sete ponteiros amostrais com SHA-256 coincidente com o manifesto de distribuição.
- [x] Validados por download no GitHub Actions os 205 objetos LFS, com JPEG RGB, SHA-256, resolução e ausência de EXIF (execução #42733590286).
- [x] Registro de revisão **v1.0.2** para o recebimento dos arquivos; metadados da v1.0.0 mantidos.
