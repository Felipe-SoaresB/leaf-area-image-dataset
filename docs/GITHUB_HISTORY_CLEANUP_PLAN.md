# Plano de saneamento seguro de GitHub e Git LFS

## Situação verificada
A branch pública `main` no início desta auditoria continha os sete JPEGs sob `images/data/` como ponteiros LFS de 132 bytes e as fotos binárias estavam acessíveis no LFS. Os hashes SHA-256 dos sete arquivos sanitizados foram registrados privadamente. A correção foi enviada para revisão na branch pública `privacy/corrected-public-v1.0.3` (commit `66407bd`), mas `main` não foi alterada; a exclusão em um commit novo não elimina cópias históricas.

Os refs vistos na auditoria remota anterior incluem `main`, `images-staging`, `snapshot/v1.0.0` e `snapshot/v1.0.1`; devem ser rechecados antes de qualquer saneamento. Esta cópia foi clonada apenas com `main`, logo não foi usada para afirmar limpeza integral dos demais refs. Nenhum tag/ref foi removido.

## Ações seguras sem reescrita
1. Revisar e aprovar o commit normal que remove os sete arquivos do estado corrente e corrige CSVs/docs/manifests.
2. Depois da revisão, integrar por fluxo normal, sem force-push. Isso interrompe novas distribuições a partir do `main` atualizado, mas deixa imagens acessíveis nos commits/ref antigos.
3. Auditar branches, tags, refs de PR, releases, Actions artifacts, forks e URLs LFS. Não apagar tags/refs ou PRs neste passo.
4. Abrir um ticket privado ao GitHub Support solicitando orientação e indisponibilização dos sete objetos por questão de privacidade. O rascunho local contém os nomes e OIDs; não foi enviado. Perguntar especificamente se o suporte pode purgar objetos LFS e caches sem reescrever todo o histórico.
5. Aguardar a resposta do suporte e documentar o efeito sobre forks, PRs, cache Git, refs e clones.
6. Revalidar as outras 198 imagens via LFS e seus SHA-256 após qualquer ação autorizada.

## Limite técnico e opção posterior
O GitHub informa que remover um arquivo do commit atual não o remove do histórico; limpeza integral de conteúdo sensível normalmente requer reescrita coordenada do histórico e contato com suporte para caches, PRs e LFS. A documentação também informa que objetos LFS removidos do histórico continuam no armazenamento até exclusão/purga pelo suporte (ou recriação do repositório, opção destrutiva e não recomendada aqui). [Remoção de dados sensíveis](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository), [remoção de arquivos LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/removing-files-from-git-large-file-storage).

Uma reescrita de histórico, force-push, remoção de refs/PRs ou exclusão/recriação do repositório **não está autorizada e não foi executada**. A recomendação é primeiro receber orientação do suporte e mapear forks/refs; se for inevitável reescrever, planejar cópia de segurança, ref list completa, congelamento de pushes, coordenação dos colaboradores, comandos com `git-filter-repo --sensitive-data-removal`, relatório de commits alterados e checklist de pós-purga. Só prosseguir após autorização explícita do mantenedor.

## Critério de confirmação
O incidente não deve ser considerado sanado enquanto os sete downloads LFS antigos ou referências históricas continuarem acessíveis. Registrar URLs/hash de tentativas sem login, resposta do Support, refs mantidas/removidas por autorização e resultado da revalidação dos 198 objetos restantes.
