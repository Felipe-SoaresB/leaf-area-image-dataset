# Tabebuia roseoalba — Leaf Area Image Dataset

**Dataset v1.0.0 · Curadoria consolidada**

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

## Como usar os dados

A pasta [`release/`](release/README.md) contém uma representação portátil dos metadados:

- [`release/images_v1.csv`](release/images_v1.csv): uma linha por fotografia, com identificação, relação com a amostra, referência ImageJ quando existente e status original de inclusão;
- [`release/area_groups_v1.csv`](release/area_groups_v1.csv): 177 grupos elegíveis para avaliação quantitativa, incluindo a divisão por grupo em desenvolvimento e teste.

Use o atributo `include_for_area_evaluation=yes` para selecionar as 191 fotografias associadas a referências de área elegíveis; para **avaliar modelos**, mantenha todas as capturas da mesma `sample_group_id` no mesmo conjunto e, quando necessário, use uma fotografia canônica por grupo para evitar pseudorreplicação.

As quatro tabelas de origem auditadas foram preservadas sem alteração em [`metadata/`](metadata/README.md). O dicionário e a rastreabilidade estão em [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md) e [`docs/PROVENANCE.md`](docs/PROVENANCE.md).

## Reprodutibilidade e integridade

`checksums/SHA256_ORIGINALS.txt` registra os hashes binários dos 205 JPEGs de origem. A versão para distribuição das imagens deve utilizar **cópias sem EXIF/GPS**, com manifesto distinto. O script de verificação é:

```bash
python scripts/validate_dataset.py --metadata-dir metadata --output-dir resultado_metadata
python scripts/check_release.py
```

A verificação de estrutura roda automaticamente no GitHub Actions.

## Escopo e disponibilização

A **versão 1.0.0 congela os metadados e suas regras de seleção**. Os JPEGs **não estão hospedados neste repositório**, que permanece privado durante a preparação do depósito científico. O arquivo de imagens para distribuição e o DOI ainda não foram publicados.

Os estados de qualidade mantidos nos CSVs refletem a curadoria existente; não representam certificação visual individual das imagens. Para critérios de exclusão, decisões de associação e demais limites do conjunto, consulte [`docs/EXCLUSIONS_AND_LIMITATIONS.md`](docs/EXCLUSIONS_AND_LIMITATIONS.md). Não se deve interpretar registros de área zero como medições físicas nulas quando correspondem a ausência de referência.

**Citação:** arquivo [`CITATION.cff`](CITATION.cff). O DOI será acrescentado somente quando existir.
