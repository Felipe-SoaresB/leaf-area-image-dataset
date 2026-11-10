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
Os quatro arquivos de `metadata/` permanecem idênticos aos blobs da importação auditada. `release/` contém apenas campos selecionados e renomeados dos dados existentes; não gera novos valores biológicos. `VERSION`, `CHANGELOG.md`, `CITATION.cff` e a branch de snapshot registram a versão sem sobrescrever os originais.

As 205 cópias preparadas sem EXIF/GPS foram adicionadas via Git LFS à revisão v1.0.2. Elas possuem hashes diferentes dos originais, que devem continuar preservados na fonte. A validação automática dos 205 objetos LFS foi aprovada na execução [GitHub Actions #42733590286](https://github.com/Felipe-SoaresB/leaf-area-image-dataset/actions/runs/42733590286). O repositório está público; isso não equivale a DOI, licença ratificada ou histórico público sanitizado.
