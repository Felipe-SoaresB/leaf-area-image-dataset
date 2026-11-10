# Critérios de inclusão, exclusões e limites de interpretação — v1.0.0

## Unidade e seleção
`image_id` identifica uma fotografia. `sample_group_id` identifica um grupo/folha associado a uma ou mais fotografias, inclusive retakes. A avaliação quantitativa foi estruturada pelos **177 grupos com referência de área utilizável**, totalizando 191 imagens.

De 205 registros de imagem, **14 não pertencem ao conjunto quantitativo**:
- 6 fotografias sem referência válida: grupo SG0002 (3 fotografias), SG0135, SG0168 e SG0175;
- 7 fotografias documentais, sem unidade de área associada;
- 1 fotografia considerada inválida por superexposição (`IMG_20251206_155837.jpg`).

SG0175 não foi associado à planilha de medição. Referências com zero que representam ausência de leitura **não** devem ser interpretadas como folha de área zero.

## Integridade e qualidade
A integridade binária foi verificada por SHA-256, inclusive 66 pares redundantes de arquivo. Houve triagem global exploratória de exposição, contraste e nitidez. Os 191 registros elegíveis conservam a marca histórica `qc_status=pending`, isto é, **não passaram por homologação visual individual registrada**. Isso não impede a disponibilização com descrição honesta do escopo, mas **não autoriza** afirmar que todas as imagens apresentam bordas nítidas, segmentação fácil ou calibração reavaliada.

## Referências e protocolo
As áreas publicadas são referências transcritas da planilha ImageJ de origem, com associação documentada; não foram medidas novamente nesta versão. O protocolo completo de aquisição e calibração não foi fornecido nesta curadoria. Não extrapolar o dataset para representar todas as 546 mudas plantadas inicialmente.

## Divergências de transcrição (registro de rastreabilidade)
O campo auxiliar `coleto` tem diferenças numéricas ou de formatação em relação à planilha de origem:

| Grupo | Mestre | Referência ImageJ |
|---|---|---|
| SG0001 | 1.03 | 1.3 |
| SG0002 | 1.50 | 1.47 |
| SG0045 | 1.03 | 1.3 |
| SG0063 | 2.15 | 2..15 |
| SG0098 | 1.02 | 1.2 |
| SG0102 | 1.09 | 1.9 |
| SG0112 | 2.07 | 2.4 |
| SG0157 | 1.09 | 1.9 |

Esses valores não foram reproduzidos nos CSVs de distribuição do núcleo de área foliar. Os registros completos, justificativas e proveniência seguem preservados nos arquivos de origem.

## Privacidade dos JPEGs
Os JPEGs originais contêm EXIF, incluindo coordenadas GPS em 204 arquivos. Para depósito público, utilizar **cópias sem EXIF**, preservando os originais restritos e identificando hashes distintos. Verificar também informações manuscritas diretamente visíveis nos pixels quando a coleção for distribuída.
