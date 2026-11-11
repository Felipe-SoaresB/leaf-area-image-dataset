# Proveniência e trilha de curadoria — v1.0.0

**Acervo fotográfico:** pasta Fotos da pesquisa no Google Drive.  
**Registros de área:** planilha nativa `dados - folha`, com valores obtidos via ImageJ.  
**Origem da curadoria:** repositório privado `Felipe-SoaresB/trabalho-de-pdi-individual`.  
**Coautores:** Tatiane Morais Neves e Felipe Soares Barbosa, IFMG Campus Bambuí.

## Auditoria de 22/10/2026
Foram identificados 271 objetos JPEG no Drive, correspondentes a 205 nomes e 66 pares com nomes repetidos. **Os 66 pares foram comparados por SHA-256 e se mostraram idênticos**; as 205 fotografias canônicas foram decodificadas e tiveram SHA-256 registrados em `checksums/SHA256_ORIGINALS.txt`.

As associações entre fotos e planilha ImageJ foram preservadas conforme `metadata/tabela_mestre_v1.csv`. A planilha possui 291 registros brutos; o dataset de análise contém 177 grupos com área positiva vinculada. A divisão development/final_test mantém retakes agrupados. Divergências de transcrição registradas na curadoria foram mantidas nos dados históricos, não corrigidas silenciosamente.

O experimento de origem foi descrito pelos coautores como DIC, com 546 mudas inicialmente plantadas de *Tabebuia roseoalba*. Não há mapeamento individual de planta para foto nesta versão.

## Congelamento v1.0.0
Os quatro arquivos da importação v1.0.0 permanecem rastreáveis em commits históricos. Na edição pública corrigida, `tabela_mestre_v1.csv` e `imagens_drive.csv` foram filtrados para retirar os sete registros documentais; `release/` contém campos selecionados e renomeados dos dados existentes, sem gerar novos valores biológicos. A alteração dos CSVs correntes não apaga os blobs/commits históricos.

## Edição pública corrigida v1.0.3 — 11/11/2026
A distribuição histórica v1.0.2 teve 205 fotografias no Git LFS. A revisão pública corrigida remove sete fotos documentais sem autorização comprovada, deixando 198 JPEGs; os sete registros tinham status `non_sample` e não participavam da avaliação quantitativa. A remoção preserva dados dos 181 grupos, 177 referências válidas, 191 fotos elegíveis e divisão 44/133. O manifesto novo contempla somente os 198 JPEGs públicos.

A validação do checkout local da edição preparada verifica os binários e metadados. Ela não purga commits, refs, objetos Git LFS nem caches históricos. O DOI reservado `10.5281/zenodo.24122476` continua em Draft; nenhum arquivo desse registro foi substituído. O conjunto público só deve ser declarado corrigido após a remoção efetiva dos objetos antigos ou confirmação do GitHub sobre sua indisponibilização.
