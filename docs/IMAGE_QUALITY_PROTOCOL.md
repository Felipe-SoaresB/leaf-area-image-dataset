# Protocolo de controle de qualidade visual — Dataset foliar

**Data:** 22/10/2026. Esta etapa é uma triagem e NÃO aprova cientificamente imagens.

## Critérios por fotografia
1. Folha inteira visível e não cortada.
2. Limites da folha identificáveis e distinguíveis do papel, recipiente, sombras e reflexos.
3. Nitidez na folha (não apenas nas letras do papel).
4. Iluminação e contraste suficientes, sem saturação relevante na folha.
5. Escala/calibração reproduzível e relação com medida ImageJ em cm².
6. Revisão das informações manuscritas presentes na imagem.
7. Retakes pertencentes ao mesmo sample_group_id e preservação do split por grupo.

## Decisões
- `pendente`: nenhuma avaliação humana concluída.
- `apta`: aprovada manualmente mediante conferência dos critérios.
- `revisar`: requer inspeção da foto integral ou esclarecimento.
- `inapta`: problema documentado e justificado.
- `excluida_na_fonte`: manter decisão anterior sem alterar o original.

As 191 fotos `qc_status=pending` continuam assim até revisão humana. Outras 14 seguem com exclusões anteriores (7 documentais, 6 sem referência e 1 superexposta).

## Heurísticas automáticas
A variância do Laplaciano (foco global) e o desvio-padrão do brilho (contraste global) foram medidos numa versão em quarto de resolução. Os 10% inferiores das 191 pendentes foram marcados como prioridades de conferência, não como inadequados: foco global <= 62,79; contraste global <= 23,89. Há 20 fotos sinalizadas por foco, 20 por contraste e **32 únicas com algum desses alertas**.

Essas métricas não são prova de qualidade da folha, porque o quadro inclui papel quadriculado, inscrições manuscritas, vidro e reflexos.

## Privacidade e versões de distribuição
Todos os 205 originais possuem EXIF com seção GPS; **204 contêm latitude e longitude** e um possui a seção GPS sem coordenadas. Foram criados 205 JPEGs de trabalho sem EXIF, removendo o segmento APP1/Exif de forma binária, sem recomprimir os pixels, preservando o conteúdo científico visível. Os 205 arquivos sanitizados foram reabertos e verificados sem EXIF.

Nunca publicar diretamente os originais. Manter manifestos de hashes distintos para original e distribuição. Textos visíveis nos pixels precisam de inspeção manual separada; remoção de EXIF não remove inscrições manuscritas.

O sistema de revisão offline usa prévias reduzidas e sem EXIF, mas uma decisão duvidosa deve ser feita sobre o JPEG de resolução integral.

## Próxima decisão formal
Depois de revisão das 191 fotos e confirmação do protocolo de escala com os coautores, versionar um CSV de decisões, sem sobrescrever silenciosamente `tabela_mestre_v1.csv`. Somente então fechar o controle de qualidade científico e preparar Zenodo/DOI.
