"""Busca respostas anteriores da SPLOR (corpus/respostas-splor) por tema.

Uso:
  poetry run python scripts/buscar_respostas_anteriores.py --listar            # lista documentos com data
  poetry run python scripts/buscar_respostas_anteriores.py "termo1" "termo2"  # documentos que citam os termos,
                                                                              # do mais recente ao mais antigo,
                                                                              # com trecho e página
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / "corpus" / "respostas-splor"
MESES = {m: i for i, m in enumerate(
    ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro",
     "novembro", "dezembro"], start=1)}
RE_DATA = re.compile(r"Belo Horizonte,\s*(\d{1,2})\s+de\s+([a-zç]+)\s+de\s+(\d{4})", re.I)
RE_DATA2 = re.compile(r"em\s+(\d{2})/(\d{2})/(\d{4}),\s+às", re.I)  # data da assinatura eletrônica


def data_documento(texto: str) -> date | None:
    m = RE_DATA.search(texto)
    if m and m.group(2).lower() in MESES:
        return date(int(m.group(3)), MESES[m.group(2).lower()], int(m.group(1)))
    m = RE_DATA2.search(texto)
    if m:
        return date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
    return None


def documentos() -> list[tuple[date | None, Path, str]]:
    docs = []
    for arq in PASTA.glob("*.txt"):
        texto = arq.read_text(encoding="utf-8")
        docs.append((data_documento(texto), arq, texto))
    return sorted(docs, key=lambda d: d[0] or date(1900, 1, 1), reverse=True)


def pagina_de(texto: str, pos: int) -> str:
    marcas = list(re.finditer(r"=== PÁGINA (\d+) ===", texto[:pos]))
    return marcas[-1].group(1) if marcas else "?"


def buscar(termos: list[str], max_trechos: int = 2, largura: int = 350) -> None:
    if "--so-docs" in termos:
        termos = [t for t in termos if t != "--so-docs"]
        max_trechos = 0
    padrao = re.compile("|".join(re.escape(t) for t in termos), re.I)
    for dt, arq, texto in documentos():
        achados = list(padrao.finditer(texto))
        if not achados:
            continue
        print(f"\n## {dt or 's/ data'} | {arq.stem} | {len(achados)} ocorrência(s)")
        for m in achados[:max_trechos]:
            ini = max(0, m.start() - largura // 2)
            trecho = re.sub(r"\s+", " ", texto[ini:m.end() + largura])
            print(f"   p.{pagina_de(texto, m.start())}: …{trecho}…")


if __name__ == "__main__":
    if "--listar" in sys.argv:
        for dt, arq, _ in documentos():
            print(f"{dt or 's/ data'} | {arq.stem}")
    else:
        buscar(sys.argv[1:])
