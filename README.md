# Tabebuia roseoalba — Leaf Area Image Dataset

**Edição pública corrigida, preparada como v1.0.3 (11/11/2026).** A coleção histórica v1.0.2 tinha 205 fotografias. Esta edição de distribuição contém **198 JPEGs**; sete fotografias documentais foram retiradas por privacidade. A curadoria e os resultados científicos das amostras elegíveis foram preservados.

Conjunto de fotografias foliares atribuídas pelos autores a *Tabebuia roseoalba*, associadas, quando disponível, a áreas de referência ImageJ. Origem acadêmica: IFMG, Campus Bambuí. Autores: Tatiane Morais Neves e Felipe Soares Barbosa.

## Composição da edição pública corrigida

| Elemento | Quantidade |
|---|---:|
| JPEGs públicos | **198** |
| Grupos de amostra preservados | **181** |
| Grupos com referência ImageJ positiva utilizável | **177** |
| Fotografias elegíveis para análise quantitativa | **191** |
| Fotografias públicas fora da avaliação quantitativa | **7** |
| Divisão por grupo | **44 desenvolvimento / 133 teste final** |

A coleção histórica de 205 fotografias e a edição pública corrigida não são intercambiáveis. A diferença são sete imagens documentais sem autorização comprovada para redistribuição; elas não eram amostras, não pertenciam a grupos de folhas, estavam marcadas `non_sample` e `include_for_area_evaluation=no`. Sua retirada não altera áreas, tratamentos, identificadores restantes, referências ImageJ ou partições.

## Uso e integridade

`release/images_v1.csv` contém uma linha por JPEG público; `release/area_groups_v1.csv` contém os 177 grupos com referência válida. Use `include_for_area_evaluation=yes` para selecionar as 191 imagens elegíveis e mantenha retakes do mesmo grupo na mesma partição. A divisão 44/133 é por grupo.

Os JPEGs em `images/data/` são disponibilizados por Git LFS. Execute `git lfs pull`. `checksums/SHA256_RELEASE_NO_EXIF.txt` registra apenas a edição pública atual. Os hashes dos JPEGs originais retidos na fonte são distintos dos hashes das cópias sem EXIF.

```bash
python -m pip install -r requirements.txt
python scripts/check_release.py
python scripts/check_lfs_images.py
```

A validação técnica de pixels e metadados não substitui autorização de direitos nem inspeção de conteúdo visível. O repositório e o Zenodo Draft ainda exigem saneamento de versões históricas; a correção deste commit não remove arquivos de commits anteriores nem objetos LFS antigos.

## Licença e publicação

A licença indicada para a edição pública é CC BY 4.0, sujeita à confirmação documental de direitos dos autores e de terceiros. O DOI reservado `10.5281/zenodo.24122476` corresponde a um depósito ainda em Draft; a edição v1.0.3 aqui preparada **não foi enviada nem publicada no Zenodo**. Consulte `docs/RELEASE_CHECKLIST.md` antes de tratar esta edição como liberada.

## Contexto

Segundo informação dos autores, o experimento de origem usou delineamento inteiramente casualizado e inicialmente plantou 546 mudas. Esse número descreve o experimento de origem, não o número de folhas, grupos ou fotografias públicas. Os códigos de substrato e irrigação estão em `docs/TREATMENT_CODES.md`; não inferir relações individuais entre mudas e imagens que não estejam documentadas.
