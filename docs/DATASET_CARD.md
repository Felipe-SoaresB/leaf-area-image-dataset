# Cartão do dataset — v1.0.0

## Identificação
**Título:** Tabebuia roseoalba Leaf Area Image Dataset with ImageJ References  
**Coautoria:** Tatiane Morais Neves; Felipe Soares Barbosa  
**Instituição de origem:** IFMG — Campus Bambuí  
**Versão de curadoria:** 1.0.0 (09/11/2026)

## Objetivo e natureza
Coleção de fotografias foliares vinculadas, quando possível, a medições de área em cm² provenientes de registros ImageJ. O conjunto pode apoiar análise exploratória, prototipagem e avaliação de algoritmos de estimativa de área foliar por imagem.

## Aquisição e contexto informado
Espécie identificada pelos autores como *Tabebuia roseoalba*. Experimento de origem declarado como DIC, com 546 mudas inicialmente plantadas. As fotografias identificadas foram capturadas em dezembro de 2025, segundo nomes e registros de aquisição. Não foi estabelecida a correspondência um-a-um das mudas originais com as folhas fotografadas.

## Composição
- 205 JPEGs distintos e 181 grupos mapeados.
- 177 grupos com referência de área utilizável, correspondentes a 191 fotografias; 14 fotografias ficam fora da avaliação quantitativa.
- 291 registros de origem na planilha de referências, mas somente os vínculos elegíveis entraram no arquivo de 177 grupos.
- 44 grupos de desenvolvimento e 133 de teste, separados por grupo, sem dividir retakes entre os conjuntos.

## Referência e tratamento
A área de referência foi obtida dos registros de ImageJ disponibilizados na pesquisa. Associações entre foto e planilha foram documentadas e auditadas em metadados. As 66 duplicações de arquivo da pasta de origem foram comprovadas idênticas por SHA-256; elas não equivalem a 66 novas amostras.

## Critério de inclusão
Para comparações quantitativas usar `release/area_groups_v1.csv`, que contém grupos com associação e referência positiva. Fotografias em `release/images_v1.csv` com `include_for_area_evaluation=no` não integram essa análise. Uma área ausente/zero da fonte pode indicar ausência de leitura, não dimensão biológica nula.

## Limites de interpretação
A auditoria binária e a triagem automática não equivalem a aferição independente da área ImageJ nem a aprovação visual individual de todos os quadros. As amostras podem variar em iluminação, nitidez e condições do entorno. O uso deve respeitar a unidade amostral por grupo, as regras de vinculação e o contexto experimental disponível. Detalhes estão em `EXCLUSIONS_AND_LIMITATIONS.md` e `PROVENANCE.md`.

## Disponibilidade e versão
O acervo canônico tem manifestação SHA-256. A documentação e os dados foram congelados em v1.0.0 no repositório privado. As fotografias destinadas a distribuição devem ser empacotadas sem EXIF/GPS, verificadas e depositadas separadamente. Não existe DOI atribuído nesta etapa.
