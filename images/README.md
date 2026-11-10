# Fotografias do dataset — Git LFS

A pasta [data/](data/) contém **205 entradas de fotografia JPEG**, inseridas na branch `main` por Git LFS em 09/11/2026. Os JPEGs de distribuição foram preparados **sem EXIF/GPS**, enquanto os originais com EXIF permanecem no acervo de pesquisa.

O Git versiona pequenos arquivos-ponteiro LFS que identificam o SHA-256 e o tamanho de cada JPEG real. **Um ponteiro de aproximadamente 132 bytes não é uma imagem.** O conteúdo binário precisa ser buscado no servidor Git LFS.

## Baixar as fotografias em um clone

```powershell
git lfs install
git clone https://github.com/Felipe-SoaresB/leaf-area-image-dataset.git
cd leaf-area-image-dataset
git lfs pull
python -m pip install -r requirements.txt
python scripts/check_lfs_images.py
```

Para verificar manualmente a lista dos 205 objetos: `git lfs ls-files`. O script exige **205 JPEGs decodificáveis e com os hashes de `checksums/SHA256_RELEASE_NO_EXIF.txt`**, sem metadados EXIF. O download exige permissão no repositório enquanto ele permanecer privado.

Não misturar o manifesto de originais (`SHA256_ORIGINALS.txt`) com os hashes das cópias preparadas para distribuição. As 66 duplicações da pasta original foram deduplicadas antes do envio e não representam novas fotografias.

**Estado:** os ponteiros e o manifesto estão no Git. A validação automática por download dos objetos LFS está sendo incorporada ao GitHub Actions. O repositório ainda não é uma publicação pública e não possui DOI.
