# Estado de publicação e auditoria do dataset — 09/11/2026

**Projeto:** Tabebuia roseoalba — Leaf Area Image Dataset  
**Repositório:** https://github.com/Felipe-SoaresB/leaf-area-image-dataset  
**Situação:** disponível publicamente no GitHub; depósito científico com DOI ainda pendente.

## 1. Preparação técnica — concluída
- [x] Tabela mestre de curadoria v1.0.0 preservada.
- [x] 205 fotografias distintas; 181 grupos; 177 grupos com referência ImageJ válida.
- [x] Separação experimental de 44 grupos para desenvolvimento e 133 para teste.
- [x] Retakes agrupados por `sample_group_id`.
- [x] Duplicações da origem e hashes originais registrados.
- [x] Cópias de distribuição JPEG preparadas sem EXIF/GPS.
- [x] 205 imagens versionadas via Git LFS em `images/data/`; não remover os objetos LFS.
- [x] Manifesto `checksums/SHA256_RELEASE_NO_EXIF.txt` com 205 registros.
- [x] GitHub Actions verificou o download e a integridade dos 205 JPEGs (execução [#42733590286](https://github.com/Felipe-SoaresB/leaf-area-image-dataset/actions/runs/42733590286)).
- [x] CSVs reduzidos de distribuição em `release/`, com 205 fotografias e 177 grupos.
- [x] README, dicionário de dados, cartão do dataset, procedência e limitações disponíveis.

## 2. Acesso público — concluído com ressalvas
- [x] Repositório configurado como **público**.
- [x] Entradas Git LFS presentes no ramo `main` e verificadas pela automação do GitHub.
- [ ] Confirmar em uma sessão **sem login** o clone/download dos 205 arquivos reais e verificar eventuais limitações de banda LFS.
- [ ] Confirmar visualmente que rótulos e informações presentes **nos pixels** são adequados à divulgação; remoção de EXIF não remove texto fotografado.

## 3. Direitos e licença — pendente
- [ ] Arquivar anuência escrita dos dois coautores para distribuição pública do conjunto de dados.
- [ ] Ratificar titularidade, créditos, ordem de autoria e eventuais direitos de terceiros.
- [ ] Definir com os coautores uma licença específica para fotografias/dados e, separadamente, para código de validação.
- [ ] Acrescentar o arquivo de licença adequado **somente após** a autorização correspondente.

Até a definição da licença, **repositório público não equivale a permissão irrestrita de reutilização**.

## 4. Metadados históricos públicos — pendência prioritária
- [ ] A pasta pública `metadata/` inclui registros históricos com IDs internos de arquivos Google Drive e notas de curadoria.
- [ ] Avaliar e preparar uma versão pública limitada aos campos pertinentes de `release/` e à documentação sem identificadores internos.
- [ ] Se houver dados cuja divulgação não foi autorizada, planejar saneamento **do histórico Git**; apagar arquivos no commit atual não remove commits antigos.
- [ ] Verificar impacto sobre scripts de validação, hashes e integridade antes de mudar/remover quaisquer CSVs.
- [ ] Preservar as 205 imagens no Git LFS durante qualquer operação de limpeza do repositório.

Nenhuma reescrita de histórico foi executada nesta atualização documental.

## 5. Identificadores de publicação — pendente, sem obrigação presumida
- [ ] Confirmar se uma **GitHub Release** formal é necessária no barema de APC.
- [ ] Após ratificar os direitos e verificar a distribuição pública, preparar release estável (tag única).
- [ ] Avaliar depósito externo em repositório científico (ex.: Zenodo), sempre com licença/coautoria conferidas.
- [ ] Obter DOI se apropriado e permitido; acrescentá-lo a `CITATION.cff` **somente quando existir**.
- [ ] Confirmar com a CAC quais documentos comprovam o código 129.

**Distinção:** a string `v1.0.2` em `VERSION` e `CITATION.cff` não significa que já exista uma GitHub Release formal.

## 6. Comprovação de APC — ainda não homologada
Para eventual solicitação como dataset disponibilizado, reunir:
1. URL pública do repositório, data de conferência e evidência de autoria/contribuição.
2. README, cartão do dataset, dicionário e arquivos `release/`.
3. Manifesto de SHA-256 e execução da validação automatizada.
4. Comprovação de acesso às imagens e direitos de disponibilização.
5. Tag/release e DOI, **se exigidos pelo barema**.
6. Documentos e declaração solicitados pela CAC, conforme regulamento vigente.

A pontuação deve ser definida com base no barema oficial e validada pela comissão. A presença de arquivos no GitHub, por si só, não garante deferimento.

## 7. Escopo preservado
As correções deste documento são editoriais e de status. Não modificam os dados científicos, o conjunto de imagens, os manifestos ou a metodologia já congelada.
