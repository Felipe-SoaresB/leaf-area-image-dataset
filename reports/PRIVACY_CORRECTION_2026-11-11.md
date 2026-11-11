# Correção de privacidade — edição pública v1.0.3

**Estado:** pacote preparado localmente; a distribuição pública ainda não foi totalmente saneada. Este relatório não contém nomes de arquivos retirados. A relação nominal e os hashes estão em armazenamento local privado, fora do repositório e do pacote Zenodo.

## Decisão e dados preservados
Sete fotografias documentais foram removidas da distribuição corrigida porque não há comprovação de autorização para redistribuí-las. Na tabela pública histórica, todas estavam identificadas como `non_sample` e `include_for_area_evaluation=no`; não tinham grupo de amostra nem referência de área. Portanto, sua retirada não altera medições, tratamentos, referências ImageJ, identificadores remanescentes ou divisões.

| Indicador | Coleção histórica | Edição pública corrigida |
|---|---:|---:|
| JPEGs | 205 | 198 |
| Grupos de amostra mapeados | 181 | 181 |
| Grupos com referência ImageJ positiva válida | 177 | 177 |
| Fotos elegíveis para análise quantitativa | 191 | 191 |
| Divisão por grupo | 44/133 | 44/133 |

As sete cópias sem EXIF que constavam da distribuição foram preservadas localmente em armazenamento privado, com ACL restrita à conta local, Administradores e Sistema. Além disso, os sete arquivos RAW de câmera foram localizados na pasta privada de origem, recuperados e preservados em subpasta privada separada. Os hashes dos RAWs coincidem com `SHA256_ORIGINALS.txt` do baseline histórico, e os hashes das cópias sem EXIF coincidem com o manifesto de distribuição. Nenhum RAW foi incluído no branch ou no pacote público.

## Validações do pacote
O pacote é verificável por contagem, correspondência com os índices, hashes, decodificação JPEG/RGB, EXIF/GPS, extração e conferência dos hashes pós-extração. Os resultados detalhados e caminhos dos artefatos acompanham a entrega local. A ausência de metadados EXIF não avalia rostos, nomes ou texto visível nos pixels das 198 imagens restantes.

## Bloqueios de publicação
O commit seguro remove as imagens do estado corrente do branch, mas não reescreve histórico. A branch pública `main`, refs/tags/PRs ainda não saneadas, objetos LFS e caches podem continuar servindo as cópias. O Zenodo Draft também contém o ZIP histórico. Nenhum arquivo foi substituído nesse Draft. Assim, **a edição corrigida está tecnicamente preparada, mas não está pronta para publicação** até concluir o saneamento do GitHub/LFS e atualizar/revisar o Draft com autorização.

## Limites científicos
Os valores de área, tratamentos, grupos, imagens elegíveis e split foram preservados. A edição corrigida é uma redistribuição menor da coleção histórica, não uma nova amostra experimental nem uma alteração de resultados científicos. Contagens de 205 se referem exclusivamente à edição histórica v1.0.2.
