# Controle de qualidade fotográfica — versão 1.0.0

## Objetivo
Registrar a diferença entre **integridade técnica**, **triagem automática** e **avaliação científica individual**.

- **Integridade técnica:** JPEGs abertos e decodificados; hashes SHA-256 verificados e duplicações binárias comparadas.
- **Triagem automática:** sinais globais de foco, contraste e exposição usados para identificar imagens que poderiam merecer inspeção.
- **Revisão individual:** classificação manual da adequação de cada fotografia ao procedimento de segmentação e medição; **não realizada como etapa de homologação nesta versão**.

A triagem automática registrou 32 fotografias elegíveis com pelo menos um alerta exploratório de baixo foco/contraste relativo ao lote. Isso **não é reprovação científica**. O caso `IMG_20251206_155837.jpg` já constava como captura inválida na curadoria original.

## Política de distribuição
Manter os estados históricos do arquivo mestre sem converter `pending` em `approved`. Permitir uso das 177 referências de área elegíveis, respeitando retakes, sem atribuir qualidade universal ao material.

Uma eventual revisão humana futura deve produzir registros de decisão e uma **nova versão** do conjunto, não modificar retroativamente os dados da v1.0.0.

## Proteção de dados nas imagens
As 205 fotografias originais continham metadados EXIF; 204 incluíam coordenadas GPS. Criaram-se cópias de trabalho sem EXIF, não recompostas por compressão, com manifesto SHA-256 distinto. Qualquer depósito deve incluir somente versões de distribuição e conferir também informações visíveis no conteúdo fotografado.
