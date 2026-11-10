# Incluir imagens no repositório privado por Git LFS

A coleção contém **205 JPEGs originais distintos** (aproximadamente 552 MiB). As 66 duplicações por nome no Drive não são novas imagens, e as cópias desse par foram confrontadas por SHA-256.

Os **originais contêm EXIF/GPS**. Não adicioná-los ao GitHub em nenhuma branch, nem mesmo temporariamente, porque commits permanecem no histórico. Utilize apenas **cópias sem EXIF**.

## Envio

O kit privado de preparação possui os seguintes arquivos:
- `publicar_imagens_github.py`: lê a pasta local de originais, verifica os 205 SHA-256 originais, remove APP1/EXIF sem recomprimir, confere os hashes da versão sanitizada, clona o repositório e envia via Git LFS.
- `SHA256_ORIGINAIS.txt` e `SHA256_SEM_EXIF.txt`: manifestos para validar cada imagem.
- `LEIA-ME.md`: instruções para Windows.

Depois de baixar e extrair a pasta de fotografias original do Drive, com **Python 3**, **Git** e **Git LFS** disponíveis, execute na pasta do kit:

```powershell
py -3 publicar_imagens_github.py --fotos "C:\\Users\\SEU_USUARIO\\Downloads\\Fotos"
```

Para apenas testar os 205 arquivos e a sanitização sem enviar nada:

```powershell
py -3 publicar_imagens_github.py --fotos "C:\\Users\\SEU_USUARIO\\Downloads\\Fotos" --somente-verificar
```

O script clona em diretório novo, rastreia `images/data/*.jpg` por Git LFS, confere **205** entradas e faz push para a branch `main`. O arquivo `checksums/SHA256_RELEASE_NO_EXIF.txt` acompanha as imagens no mesmo commit. A conta GitHub deve estar autenticada.

## Política de versionamento

O snapshot `snapshot/v1.0.0` descreve a versão de **metadados** consolidada. Após inclusão efetiva e conferida das fotografias, registrar a entrega de imagens como nova versão, sem modificar os valores dos quatro CSVs nem substituir o snapshot anterior.

Este documento não confirma que as imagens já estejam no GitHub; confira a pasta `images/data` e o histórico dos commits após o envio.
