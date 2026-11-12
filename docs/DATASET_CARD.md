# Cartão do dataset — edição pública corrigida v1.0.3

## Identificação
**Título:** Tabebuia roseoalba Leaf Area Image Dataset with ImageJ References  
**Autores:** Tatiane Morais Neves; Felipe Soares Barbosa
**Instituição de origem:** IFMG — Campus Bambuí
**Estado:** edição pública v1.0.3 publicada no [Zenodo (DOI: 10.5281/zenodo.24122476)](https://doi.org/10.5281/zenodo.24122476).

## Composição e unidade de análise
A edição pública corrigida contém 198 JPEGs e preserva 181 grupos de amostras. Desses, 177 grupos têm referência positiva válida obtida dos registros ImageJ e correspondem a 191 fotografias elegíveis para análise quantitativa. Os outros sete JPEGs públicos são não elegíveis. A coleção histórica v1.0.2 tinha 205 JPEGs; sete fotografias documentais sem autorização comprovada foram retiradas da nova distribuição.

A divisão experimental preservada contém 44 grupos de desenvolvimento e 133 de teste final. Retakes permanecem agrupados; a unidade de partição é `sample_group_id`. Nenhuma área, tratamento, associação dos registros restantes ou regra de divisão foi recalculada.

## Aquisição e referências
Os autores identificam as folhas como *Tabebuia roseoalba*. As referências de área provêm de registros ImageJ. A documentação não estabelece vínculo individual entre mudas originalmente plantadas e fotografias. Uma área ausente ou zero na fonte não deve ser interpretada automaticamente como área biológica nula.

## Privacidade, integridade e versão
Os sete registros retirados eram classificados como `non_sample` e excluídos da avaliação quantitativa. O relatório nominal de exclusão é mantido localmente em armazenamento privado e não integra o pacote público. A nova edição contém 198 JPEGs preparados sem EXIF/GPS, CSVs de distribuição revisados e um novo manifesto SHA-256. A validação da edição não elimina cópias em commits Git, refs antigas, objetos Git LFS ou caches. O registro Zenodo publicado contém apenas os quatro artefatos v1.0.3.

O DOI `10.5281/zenodo.24122476` está publicado. O mantenedor confirmou autorização dos coautores para distribuir as imagens e os CSVs públicos sob CC BY 4.0. É recomendável preservar a autorização escrita e os relatórios de integridade como documentação da pesquisa.

## Limitações
A triagem automática não substitui validação visual independente de todas as referências. As imagens variam em iluminação, foco e contexto. Os resultados aplicam-se ao conjunto descrito e não autorizam generalização para população ou condições não amostradas.
