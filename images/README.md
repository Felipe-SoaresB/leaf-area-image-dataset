# Fotografias do dataset — Git LFS

**Licença das 198 imagens da edição pública v1.0.3:** [CC BY 4.0](../LICENSE-DATA.md), com atribuição aos dois coautores.

A pasta [data/](data/) contém **198 fotografias JPEG** na branch `main` da edição v1.0.3. A distribuição histórica v1.0.2 tinha 205 imagens; sete fotos documentais foram retiradas da distribuição pública atual. Os JPEGs de distribuição foram preparados **sem EXIF/GPS**, enquanto os originais com EXIF permanecem no acervo de pesquisa.

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

Para verificar a lista dos 198 objetos da edição atual: `git lfs ls-files`. O script exige **198 JPEGs decodificáveis e com os hashes de `checksums/SHA256_RELEASE_NO_EXIF.txt`**, sem metadados EXIF. O repositório está público. O download efetivo depende da disponibilidade dos objetos no Git LFS; a execução automatizada de validação confirmou o download autenticado por GitHub Actions, mas uma verificação de acesso anônimo ainda é recomendada.

Não misturar o manifesto de originais (`SHA256_ORIGINALS.txt`) com os hashes das cópias preparadas para distribuição. As 66 duplicações da pasta original foram deduplicadas antes do envio e não representam novas fotografias.

**Estado:** os 198 ponteiros e o manifesto da edição v1.0.3 estão no Git. A validação automática conferiu SHA-256, JPEG RGB, resolução e ausência de EXIF, com sucesso em [GitHub Actions #43115677864](https://github.com/Felipe-SoaresB/leaf-area-image-dataset/actions/runs/43115677864). A edição v1.0.3 está publicada no [Zenodo com DOI 10.5281/zenodo.24122476](https://doi.org/10.5281/zenodo.24122476). A validação técnica não substitui revisão visual e de direitos de terceiros. Não foi confirmada criação de uma GitHub Release formal.
