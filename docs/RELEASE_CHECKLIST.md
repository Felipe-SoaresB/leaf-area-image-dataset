# Checklist de publicação — edição pública corrigida v1.0.3

**Estado em 11/11/2026: PREPARADA LOCALMENTE, NÃO PRONTA PARA PUBLICAR.** Esta edição remove sete fotos documentais sem autorização comprovada. O GitHub continua tendo arquivos acessíveis em `main`, histórico/refs antigas e LFS, e o Zenodo Draft ainda mantém o ZIP histórico de 205 imagens.

## Dados e invariantes
- [x] Sete registros históricos confirmados como `non_sample` e fora da avaliação (`include_for_area_evaluation=no`); RAWs privados e cópias anteriormente distribuídas preservados em armazenamento local separado, hashes conferidos.
- [x] Edição pública de trabalho: 198 JPEGs, 181 grupos, 177 referências ImageJ válidas, 191 imagens elegíveis.
- [x] Partição preservada: 44 grupos development / 133 final_test.
- [x] Sete imagens retiradas das tabelas/índices/checksums ativos e do diretório LFS da edição corrigida.
- [x] Áreas, tratamentos, grupos, referências elegíveis e split não recalculados.
- [ ] Executar revisão independente dos direitos/licenças e conteúdo visual das 198 imagens remanescentes.

## Integridade e depósito
- [x] SHA-256 regenerado para os 198 JPEGs públicos.
- [x] Plano de pacote e validação integral definidos; resultado detalhado em `reports/PRIVACY_CORRECTION_2026-11-11.md`.
- [x] ZIPs corrigidos preparados localmente após verificação de extração.
- [ ] Não substituir arquivos nem metadados do Zenodo Draft até autorização explícita.
- [ ] Após autorização, atualizar os quatro artefatos do Draft e confirmar novamente o conteúdo antes de Publish.
- [ ] Não clicar em Publish sem autorização expressa e revisão do usuário.

## GitHub e objetos históricos
- [x] Correção segura publicada para revisão em `privacy/corrected-public-v1.0.3` (commit `66407bd`); `main` não foi alterada.
- [ ] Revisar e integrar correção ao `main` por fluxo normal, depois de revisão humana.
- [ ] Abrir solicitação ao GitHub Support para indisponibilizar os objetos LFS e caches comprometidos; não remover refs/tags nem reescrever histórico sem autorização expressa.
- [ ] Auditar todas as branches, tags, PR refs, releases, Actions artifacts e clones públicos após a resposta do GitHub.
- [ ] Confirmar por URLs LFS antigas que os objetos não podem mais ser baixados.

## APC e documentação
- [x] Ficha técnica APC atualizada como material comprobatório, não como garantia de pontuação.
- [ ] Confirmar com a CAC qual regulamento vigente, evidências e formato de DOI/release são aceitos para o item 129.
- [ ] Arquivar autorização escrita dos titulares para a edição exata de 198 imagens e os termos de licença.

## Critério de liberação
A publicação permanece bloqueada até: (1) saneamento ou confirmação de indisponibilidade dos arquivos históricos no GitHub; (2) atualização e conferência do Zenodo Draft; (3) comprovação de autorização para redistribuir todas as 198 imagens e documentação; (4) revisão final do usuário. Não há release formal nesta etapa.
