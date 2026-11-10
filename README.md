# Tabebuia roseoalba — Leaf Area Image Dataset

**Versão v1.0.2 · Metadados científicos consolidados em v1.0.0 · Fotografias disponíveis via Git LFS**

Conjunto de fotografias de folhas atribuídas à espécie *Tabebuia roseoalba* e metadados de áreas foliares de referência obtidas por ImageJ. O material foi organizado para permitir estudos de **estimativa de área foliar a partir de imagens**, documentação e comparação de métodos computacionais. Origem acadêmica: **Instituto Federal de Minas Gerais (IFMG), Campus Bambuí**.

**Autores:** Tatiane Morais Neves e Felipe Soares Barbosa (estudantes do IFMG Campus Bambuí).

## Conteúdo da versão 1.0.0

| Elemento | Quantidade |
|---|---:|
| Fotografias JPEG distintas | **205** |
| Grupos de amostra identificados | **181** |
| Grupos vinculados a área de referência utilizável | **177** |
| Fotografias associadas a esses grupos | **191** |
| Fotografias fora da avaliação quantitativa | **14** |
| Registros da planilha ImageJ de origem | **291** |
| Divisão de desenvolvimento | **44 grupos** |
| Divisão de teste final | **133 grupos** |

As contagens de fotografias e de grupos de amostra são diferentes porque algumas folhas possuem múltiplas capturas (`retakes`). Os arquivos foram verificados quanto a integridade binária e as 66 cópias com nomes repetidos encontradas na origem eram idênticas por SHA-256.

## Contexto da aquisição

Segundo a coautora que forneceu o contexto experimental, a espécie é *Tabebuia roseoalba*, o experimento utilizou **DIC (Delineamento Inteiramente Casualizado)** e teve **546 mudas inicialmente plantadas**. Esse número descreve o experimento de origem, não o número de folhas ou fotos deste conjunto. A relação individual entre cada muda e imagem não foi documentada nesta versão.

## Tratamentos e códigos

Os substratos são **A = Areia**, **V = Vermiculita** e **T = Terra** (a variante minúscula `v` equivale a V). Os níveis **25%, 50%, 75% e 100%** correspondem a condições de irrigação relativas à **CRA — capacidade de retenção de água** do substrato. Os códigos descrevem o tratamento; não representam porcentagens de mistura dos substratos.

O significado das siglas, os identificadores e os estados das tabelas está reunido em [**Códigos e abreviações**](docs/TREATMENT_CODES.md). Informações que não foram explicitadas nas planilhas originais permanecem assinaladas no dicionário, sem suposições.

## Como usar os dados

A pasta [`release/`](release/README.md) contém uma representação portátil dos metadados:

- [`release/images_v1.csv`](release/images_v1.csv): uma linha por fotografia, com identificação, relação com a amostra, referência ImageJ quando existente e status original de inclusão;
- [`release/area_groups_v1.csv`](release/area_groups_v1.csv): 177 grupos elegíveis para avaliação quantitativa, incluindo a divisão por grupo em desenvolvimento e teste.

Use o atributo `include_for_area_evaluation=yes` para selecionar as 191 fotografias associadas a referências de área elegíveis; para **avaliar modelos**, mantenha todas as capturas da mesma `sample_group_id` no mesmo conjunto e, quando necessário, use uma fotografia canônica por grupo para evitar pseudorreplicação.

As quatro tabelas de origem auditadas foram preservadas sem alteração em [`metadata/`](metadata/README.md). O dicionário e a rastreabilidade estão em [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md) e [`docs/PROVENANCE.md`](docs/PROVENANCE.md).

## Reprodutibilidade e integridade

`checksums/SHA256_ORIGINALS.txt` registra os hashes dos JPEGs originais, enquanto [`checksums/SHA256_RELEASE_NO_EXIF.txt`](checksums/SHA256_RELEASE_NO_EXIF.txt) contém os hashes das **205 cópias sem EXIF** incluídas via Git LFS. Os dois manifestos não são intercambiáveis. O script de verificação é:

```bash
python scripts/validate_dataset.py --metadata-dir metadata --output-dir resultado_metadata
python scripts/check_release.py
python scripts/check_lfs_images.py
```

O terceiro comando requer os JPEGs completos, baixados por `git lfs pull`, e a dependência `Pillow` (`pip install -r requirements.txt`).

A verificação de estrutura roda automaticamente no GitHub Actions.

## Escopo e disponibilização

A **versão 1.0.0 congela os metadados e suas regras de seleção**. As **205 imagens sem EXIF** foram adicionadas em [`images/data/`](images/data/) via **Git LFS**. Faça o clone com Git LFS instalado e execute `git lfs pull` para obter os JPEGs completos; arquivos de 132 bytes presentes apenas no Git são ponteiros LFS, não fotografias. O repositório permanece **privado**. O depósito científico público e o DOI ainda não foram realizados.

Os estados de qualidade mantidos nos CSVs refletem a curadoria existente; não representam certificação visual individual das imagens. Para critérios de exclusão, decisões de associação e demais limites do conjunto, consulte [`docs/EXCLUSIONS_AND_LIMITATIONS.md`](docs/EXCLUSIONS_AND_LIMITATIONS.md). Não se deve interpretar registros de área zero como medições físicas nulas quando correspondem a ausência de referência.

**Citação:** arquivo [`CITATION.cff`](CITATION.cff). O DOI será acrescentado somente quando existir.
