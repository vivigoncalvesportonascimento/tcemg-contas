# tcemg-contas

Repositório de documentação do TCEMG/Cfamge e das respostas da SPLOR/SEPLAG, usado como base de consulta
para responder a novos questionamentos e pedidos de informação do Tribunal de Contas de Minas Gerais.

## Ambiente (Poetry)

```bash
poetry install                                   # cria .venv e instala dependências
poetry run python scripts/extrair_textos.py      # extrai texto dos PDFs/DOCX de data/ para corpus/
```

O `corpus/` replica a estrutura de `data/` em arquivos `.txt`, com marcadores `=== PÁGINA N ===`
(numeração do PDF; nos relatórios do TCEMG coincide com a numeração impressa). Use-o para busca
(`grep`/ripgrep) e citação de páginas. Rode a extração novamente sempre que incluir PDFs em `data/`
(só os arquivos novos ou alterados são processados; `--forcar` reprocessa tudo).

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `data/analise-contas` | Relatórios do TCEMG sobre as contas do Governador e análises da defesa do Estado |
| `data/balanco` | Balanços Gerais do Estado |
| `data/demandas-resposta` | Demandas em aberto (ofícios e quadros de controle) |
| `data/respostas-splor` | Respostas anteriores da SPLOR (memorandos, ofícios, notas técnicas) |
| `data/documentacao-complementar` | RGF, RREO, relatório de transição etc. |
| `data/legislacao-basica` | CF, CE/MG, LRF, Lei 4.320, LDO, LOA, PPAG, decretos de competência |
| `corpus/` | Texto extraído (gerado) |
| `scripts/` | Extração e geração de documentos |
| `entregas/` | Documentos produzidos por demanda |

## Demandas

- **Demanda 01 – Ofício SEF/STE nº 288/2026** (monitoramento TCEMG, 1º ciclo 2026; prazo 12/11/2026)
  - Conteúdo editável: `scripts/demanda01_conteudo.py`
  - Gerar o Word: `poetry run python scripts/gerar_demanda01_docx.py`
  - Saída: `entregas/demanda-01/Demanda01_Oficio_SEF_288_2026_minuta_respostas_SPLOR.docx`
