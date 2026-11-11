# Arquivos de curadoria e metadados — edição pública corrigida v1.0.3

Esta pasta contém quatro tabelas de curadoria com campos técnicos e registros de referência. O histórico v1.0.0 foi capturado com 205 linhas de imagem; o estado público corrente foi atualizado para 198 linhas após retirar sete registros documentais sem autorização comprovada. O arquivo ImageJ e a divisão por grupos não foram alterados.

| Arquivo | Linhas atuais | Nota |
|---|---:|---|
| `tabela_mestre_v1.csv` | 198 | inclui campos de curadoria interna |
| `imagens_drive.csv` | 198 | inclui IDs internos do Drive |
| `referencias_imagej.csv` | 291 | referência histórica original |
| `divisao_experimental_v1.csv` | 177 | partições preservadas |

**Não use esta pasta como pacote de distribuição.** Ela ainda contém IDs internos do Google Drive e outras notas/campos de curadoria que não são necessários ao uso científico público. Para distribuição atual, utilize somente CSVs sanitizados em `../release/`, documentação pública selecionada e os JPEGs incluídos no manifesto corrigido. A remoção do conteúdo atual não apaga commits ou refs antigos; veja `../docs/GITHUB_HISTORY_CLEANUP_PLAN.md`.

A lista nominal das sete fotografias documentais retiradas e seus hashes foi mantida fora deste repositório, em registro privado local, para não republicar seus nomes nos documentos da nova edição.
