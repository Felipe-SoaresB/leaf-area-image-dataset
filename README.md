# Leaf Area Image Dataset — versão de preparação

**Status: repositório em preparação (PRIVATE STAGING). Este pacote não constitui uma publicação científica nem uma versão validada para distribuição.**

Dataset de fotografias de folhas, com medidas de referência provenientes de registros ImageJ e metadados para avaliação de métodos de estimativa de área foliar a partir de imagens. Desenvolvido no contexto acadêmico do **Instituto Federal de Minas Gerais (IFMG), Campus Bambuí**.

## Autoria

- **Tatiane Morais Neves** — coautora, estudante do IFMG Campus Bambuí.
- **Felipe Soares Barbosa** — coautor, estudante do IFMG Campus Bambuí.

A autorização dos dois coautores para a publicação foi informada. Os termos de licenciamento e a autorização documental serão registrados antes da divulgação pública. Não há atribuição de funções específicas sem validação dos coautores.

## Contexto experimental — informações fornecidas pelos coautores

Segundo informações fornecidas por Tatiane Morais Neves durante a preparação do dataset:

- **Espécie declarada:** *Tabebuia roseoalba* (grafia informada; identificação taxonômica ainda não verificada independentemente).
- **Delineamento experimental declarado:** DIC — **Delineamento Inteiramente Casualizado**.
- **Plantio inicial declarado:** **546 plantas/mudas plantadas** no início do experimento.

Esses três dados descrevem o **experimento de origem**, e não a quantidade de fotografias ou amostras incluídas no dataset. O número de 546 plantas iniciais **não deve ser equiparado** às 205 imagens distintas, aos 181 grupos mapeados ou aos 177 grupos de avaliação quantitativa. Também **não é possível deduzir** dos dados recebidos o número de plantas sobreviventes, a quantidade de folhas por planta ou o esquema físico de plantio.

Para distinguir **delineamento estatístico** de **disposição física das mudas**, faltam detalhes dos tratamentos, número de repetições, alocação, bandejas/parcelas, espaçamento, datas e condições de coleta. Ver [`docs/EXPERIMENTAL_CONTEXT.md`](docs/EXPERIMENTAL_CONTEXT.md).

## Estado atual dos dados (auditoria estrutural de 22/10/2026)

| Item | Contagem |
| --- | ---: |
| Fotografias distintas por nome (JPEG) | 205 |
| Arquivos físicos na pasta de origem, incluindo cópias | 271 |
| Nomes de fotografias duplicados | 66 |
| Grupos de amostras identificados | 181 |
| Grupos elegíveis para análise de área | 177 |
| Imagens pertencentes a esses 177 grupos | 191 |
| Registros brutos de área por ImageJ | 291 |
| Grupos de desenvolvimento | 44 |
| Grupos de teste final | 133 |

**Importante:** 205 imagens não equivalem a 205 amostras independentes; existem recapturas (`retakes`). Algumas imagens foram excluídas de comparação quantitativa. Os números são resultado de auditoria de metadados, **não** de novo cálculo SHA-256 das fotografias reais.

## Organização

```text
leaf-area-image-dataset/
├── README.md
├── AUTHORS.md
├── CITATION.cff              # citação preliminar; sem DOI ainda
├── .gitignore
├── requirements.txt
├── metadata/
│   ├── README.md
│   ├── tabela_mestre_v1.csv
│   ├── imagens_drive.csv
│   ├── referencias_imagej.csv
│   └── divisao_experimental_v1.csv
├── images/
│   └── README.md             # fotografias não incluídas no Git
├── scripts/
│   └── validate_dataset.py
├── docs/
│   ├── DATA_DICTIONARY.md
│   ├── EXPERIMENTAL_CONTEXT.md
│   ├── PROVENANCE.md
│   ├── EXCLUSIONS_AND_LIMITATIONS.md
│   └── RELEASE_CHECKLIST.md
├── checksums/
│   └── README.md
└── reports/
    ├── README.md
    └── AUDITORIA_PRELIMINAR_2026-10-22.md
```

## Como verificar

**Metadados somente:** instalar as dependências e executar:

```bash
python -m pip install -r requirements.txt
python scripts/validate_dataset.py --metadata-dir metadata --output-dir resultado_metadata
```

**Metadados e JPEGs:** com uma pasta local `C:/dataset/images` contendo *uma cópia original por nome*, executar:

```powershell
python scripts/validate_dataset.py --metadata-dir metadata --images-dir "C:\dataset\images" --output-dir resultado_com_imagens --write-checksums
```

O programa apenas lê entradas e grava relatórios na pasta de saída. O repositório de preparação inclui cópias dos quatro CSVs de curadoria, provenientes do repositório privado do projeto de PDI; não inclui as fotografias JPEG. A importação dos CSVs deve ser conferida pelos respectivos Git blob SHAs.

## Política de publicação futura

Antes de abrir o repositório, precisamos concluir SHA-256 dos JPEGs, examinar EXIF e informações de terceiros, documentar qualidade e exclusões, aprovar licença(s) de dados/código, registrar autorização e alinhar o arquivo científico (por exemplo, no Zenodo). **Não considerar este repositório uma versão pública ou um DOI registrado.**

Veja `docs/RELEASE_CHECKLIST.md`.