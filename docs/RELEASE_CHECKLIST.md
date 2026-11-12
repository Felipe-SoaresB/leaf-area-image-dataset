# Registro de publicação e acompanhamento — dataset v1.0.3

**Estado em 11/11/2026:** edição corrigida v1.0.3 **publicada no Zenodo** sob [DOI 10.5281/zenodo.24122476](https://doi.org/10.5281/zenodo.24122476), conforme relatório de publicação do mantenedor. A `main` do GitHub distribui a mesma edição corrente de 198 imagens via Git LFS.

## Dados e integridade
- [x] 198 JPEGs públicos sem EXIF/GPS, com SHA-256 registrados no manifesto `checksums/SHA256_RELEASE_NO_EXIF.txt`.
- [x] 181 grupos identificados, 177 referências ImageJ utilizáveis, 191 fotografias elegíveis.
- [x] Partição de 44 grupos development e 133 final_test preservada.
- [x] Sete fotografias documentais sem referência removidas da edição v1.0.3, dos índices correntes e dos pacotes publicados; áreas e tratamentos restantes preservados.
- [x] Validação GitHub Actions [#43115677864](https://github.com/Felipe-SoaresB/leaf-area-image-dataset/actions/runs/43115677864) concluída com sucesso.
- [x] Integridade dos quatro arquivos enviados ao Zenodo validada por hashes MD5 exibidos na plataforma comparados aos pacotes locais (conforme relatório do mantenedor).

## Publicação
- [x] `main` incorpora a correção, sem force-push nem reescrita do histórico.
- [x] Zenodo contém somente os quatro artefatos v1.0.3.
- [x] Registro Zenodo publicado e DOI 10.5281/zenodo.24122476 resolvendo para registro público.
- [x] README, CITATION.cff, licença e ficha APC atualizados com DOI.
- [ ] **Corrigir a frase residual da descrição pública do Zenodo** que ainda afirma que o depósito está em Draft e o DOI não foi registrado. Alterar metadados da publicação existente, sem alterar arquivos e sem criar nova versão.
- [ ] Criar, se desejado, a GitHub Release/tag formal `v1.0.3`, verificando antes o conteúdo dos arquivos gerados pelo GitHub quando o repositório usa LFS. DOI do Zenodo já é a referência científica persistente.

## Direitos e versões históricas
- [x] O mantenedor informou que os coautores autorizaram o licenciamento CC BY 4.0 dos dados e fotografias da distribuição pública.
- [ ] Arquivar comprovação escrita da autorização dos titulares e revisar possíveis direitos de terceiros conforme necessário.
- [ ] Documentar eventual decisão posterior sobre commits e objetos Git/LFS históricos. A remoção do estado corrente não purga o histórico, mas a edição Zenodo v1.0.3 contém apenas as 198 imagens distribuídas.

## APC
- [x] Ficha técnica preparada e DOI publicado incluído em `docs/APC_FICHA_TECNICA_DATASET.md`.
- [ ] Confirmar com a CAC a vigência do regulamento, o peso do item 129 e o formato das evidências.
- [ ] Incluir no dossiê final a ficha, a URL do DOI, o README, a comprovação da contribuição individual e os demais documentos exigidos.

## Data
O campo de publicação apresentado no Zenodo mostra 22/10/2026, conforme informado pelo responsável. A ação final Publish foi confirmada em 11/11/2026. Não confundir a data registrada nos metadados com o momento da publicação efetiva do registro.
