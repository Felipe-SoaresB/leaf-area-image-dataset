# Registro histórico e instruções para a edição pública v1.0.3

Este documento substitui as instruções operacionais de envio da edição v1.0.2. As passagens históricas sobre 205 arquivos registram o que foi publicado em 09/11/2026, não o conteúdo público autorizado para a nova distribuição.

## Edição pública corrigida

O estado de trabalho v1.0.3 contém 198 JPEGs sem EXIF/GPS. Sete fotografias documentais foram excluídas por falta de comprovação de autorização para redistribuição. A coleção de 205 imagens permanece como registro histórico; áreas, tratamentos, grupos e split (44/133) foram preservados. Consulte `docs/GITHUB_HISTORY_CLEANUP_PLAN.md`.

Os scripts para validação local são:

```powershell
py -3 -m pip install -r requirements.txt
py -3 scripts/check_release.py
py -3 scripts/check_lfs_images.py
py -3 scripts/build_zenodo_package.py --output-dir "D:\Projetos\leaf-area-zenodo-v1.0.3" --private-audit "$env:LOCALAPPDATA\LeafAreaPrivacyHold\2026-11-11\private_exclusion_audit.json" --baseline-commit d07f5d679c030035eea3b40c30f1eaf1e72b2d37
```

O último comando gera ZIPs e valida hashes, exclusões, equivalência científica do índice remanescente, 198 imagens, metadados e extração. O relatório é uma validação técnica, não prova de licença, consentimento, saneamento histórico nem publicação.

## Histórico v1.0.2
O envio original ao Git LFS colocou 205 cópias JPEG sem EXIF/GPS em `main` e foi verificado pelo Actions run #42733590286. Essa referência é mantida para rastreabilidade. Os JPEGs retirados podem continuar recuperáveis em commits e objetos LFS antigos; a simples remoção do branch atual não purga esses objetos. O Zenodo fica em Draft até nova autorização. Não enviar, substituir, force-push, reescrever histórico ou publicar sem aprovação expressa.
