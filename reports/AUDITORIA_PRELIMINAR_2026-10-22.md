# Auditoria técnica preliminar — Leaf Area Image Dataset v1.0

**Data da conferência:** 22/10/2026  
**Origens:** Google Drive / pasta `TCC` / subpasta `Fotos`; GitHub privado `Felipe-SoaresB/trabalho-de-pdi-individual`, branch `main`.  
**Autores informados:** Tatiane Morais Neves e Felipe Soares Barbosa, estudantes do IFMG Campus Bambuí.  
**Autorização:** segundo informação dos titulares neste atendimento, ambos autorizam publicação pública. **O registro documental ainda deverá ser arquivado.**

## Escopo efetivamente executado

- Consulta à listagem atual dos JPEGs no Drive, com identificação, tamanho e nome dos arquivos.
- Leitura integral e análise estrutural de `tabela_mestre_v1.csv`, `imagens_drive.csv`, `referencias_imagej.csv` e `divisao_experimental_v1.csv` via conector do GitHub.
- Conferências cruzadas das tabelas com a listagem da pasta de fotos.
- Inspeção da documentação `DATASET_V1.md`, `AQUISICAO_E_PREPARACAO.md`, `INSPECAO_INICIAL.md` e `REVISAO_EXCECOES.md`.

**NÃO executado nesta auditoria:** baixar e decodificar os 205 JPEGs desta versão, calcular SHA-256 do conteúdo deles, comparar byte a byte as 66 duplas, validar propriedades EXIF atuais das imagens. Os valores históricos desses testes aparecem na documentação prévia, não são checagens binárias repetidas nesta rodada.

## Resultado confirmado na versão atual

| Propriedade | Valor verificado | Situação |
|---|---:|---|
| JPEGs na pasta original do Drive | 271 | confirmado |
| Nomes únicos de fotografia | 205 | confirmado |
| Nomes presentes duas vezes | 66 | confirmado |
| Nomes presentes uma vez | 139 | confirmado |
| Duplas com tamanhos de arquivo diferentes | 0 das 66 duplas | confirmado **somente por tamanho** |
| Imagens listadas na tabela mestre | 205 | confirmado |
| `image_id` únicos | 205 | confirmado |
| Arquivos nomeados na tabela mestre e no manifesto `imagens_drive.csv` | conjuntos coincidentes (205) | confirmado |
| IDs canônicos do Drive localizados | 205 | confirmado |
| Tamanhos canônicos compatíveis com listagem atual | 205 | confirmado |
| Registros da planilha ImageJ | 291 | confirmado |
| Referências com área positiva | 245 | confirmado |
| Registros com área igual a zero | 45 | confirmado |
| Registros com área textual não numérica | 1 (`tirar foto`) | confirmado |
| Grupos biológicos identificados | 181 | confirmado |
| Grupos com identidade `confirmed` | 180 | confirmado |
| Grupos `unmapped` | 1 (`SG0175`) | confirmado |
| Grupos elegíveis para comparação quantitativa | 177 | confirmado |
| Imagens das 177 amostras elegíveis | 191 | confirmado |
| Retakes adicionais nas 177 amostras | 14 | confirmado |
| Grupos no desenvolvimento | 44 | confirmado |
| Grupos no teste final | 133 | confirmado |
| Canônicos fora da regra de primeira captura | 0 | confirmado |
| Divergências internas entre retakes do mesmo grupo (campos-chave) | 0 | confirmado |
| Divisão com áreas divergentes da tabela mestre | 0 | confirmado |
| Fotos `qc_status=pending` | 191 | requer descrição de QC |
| Fotografias de amostras sem área utilizável | 6, distribuídas em 4 grupos | exclusão documentada |
| Fotos documentais | 7 | exclusão documentada |
| Foto inválida por superexposição | 1 | exclusão documentada |

**Tamanho pelo manifesto da listagem do Drive:** 579.166.838 bytes (~552,3 MiB) para uma cópia de cada um dos 205 nomes; 771.800.329 bytes (~736,0 MiB) incluindo as cópias extras. Isso não substitui análise dos arquivos baixados.

## Exceções existentes que devem permanecer visíveis

1. Sem referência ImageJ utilizável: `SG0002` (3 fotos), `SG0135`, `SG0168`, `SG0175`; não substituir ausentes por zero físico real.
2. Há 8 grupos com diferenças **numéricas ou textuais relevantes** em `Coleto` entre tabela mestre e planilha original. O algoritmo registra avisos, preservando os registros como dados de origem:

| Grupo | Coleto na tabela mestre | Coleto na planilha | Nota |
|---|---:|---:|---|
| SG0001 | 1.03 | 1.3 | mapeamento inferido, documentado |
| SG0002 | 1.50 | 1.47 | mapeamento resolvido pela consistência global |
| SG0045 | 1.03 | 1.3 | divergência documentada |
| SG0063 | 2.15 | `2..15` | valor textual malformado na origem |
| SG0098 | 1.02 | 1.2 | divergência documentada |
| SG0102 | 1.09 | 1.9 | divergência documentada |
| SG0112 | 2.07 | 2.4 | correspondência por identificador, com divergência |
| SG0157 | 1.09 | 1.9 | mapeamento inferido, documentado |

3. `qc_status=pending` aparece em 191 fotografias. Não é correto afirmar que passaram por **todos** os critérios de qualidade final sem definir o campo.
4. As 66 duplas são iguais em tamanho, mas ainda não foram comprovadas idênticas por hash nesta rodada.
5. A análise de integridade das imagens executada no projeto anterior relata 205 JPEGs RGB, fotografados no moto g(20), 104 paisagem e 101 retrato; **estes atributos vêm da documentação do projeto, não de nova leitura binária hoje.**

## Identificação da revisão do GitHub consultada

Git blob SHA dos CSVs, que identifica o conteúdo versionado no Git (não é SHA-256 do JPEG):

- `tabela_mestre_v1.csv`: `b9e975cea11ea28be180630da892484ece8f2489`
- `imagens_drive.csv`: `097aa424c487a61f33b61ac8b05fb056f644359b`
- `referencias_imagej.csv`: `7d4bbaa91752227e48a5fc96999265f7502f4fa4`
- `divisao_experimental_v1.csv`: `28cb89752a80b2c22cd9e1860e18fac4560b1191`

A tabela `tabela_mestre.csv` e `tabela_mestre_v1.csv` tinham **o mesmo Git blob SHA** na conferência.

## Próxima porta de aprovação

Executar o script `validate_dataset.py` sobre os CSVs e os 205 JPEGs reais. Gerar `SHA256SUMS.txt`, identificar qualquer divergência, registrar o relatório JSON/Markdown e — se forem disponibilizadas as 271 cópias — confirmar as 66 duplas por SHA-256. Somente então registrar a validação binária como concluída e montar o pacote para publicação.

**Status de liberação:** validação estrutural aprovada; **verificação binária e conferência documental finais pendentes**. Não publicar nem alterar permissões nesta fase.