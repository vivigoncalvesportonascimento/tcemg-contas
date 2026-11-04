"""Aplica os resumos revisados (itens 4, 7 e 18) na versão compacta editada manualmente, sem regenerá-la.

Substitui apenas os parágrafos antigos do "Resumo do tema" desses itens, conferindo o início de cada um
antes de remover. O restante do documento é preservado.

Uso: poetry run python scripts/aplicar_resumos_compacto.py
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import RGBColor
from docx.text.paragraph import Paragraph

sys.path.insert(0, str(Path(__file__).resolve().parent))
from demanda01_resumos_revisados import RESUMOS, ROTULOS  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
ARQ = RAIZ / "entregas" / "demanda-01" / "Demanda01_Oficio_SEF_288_2026_minuta_respostas_SPLOR_revisado_compacto.docx"
AZUL = RGBColor(0x1F, 0x3A, 0x5F)

# item → (prefixo do título, início dos parágrafos antigos a substituir, na ordem)
ALVOS = {
    "R10 (2020)": ("Item 4 ·", ["A recomendação nasceu de divergências", "Nos BGE 2023 (p. 591) e 2024"]),
    "R1 (2021)": ("Item 7 ·", ["Desdobramento da R10/2020", "No BGE 2024 (p. 616), a Cfamge manteve"]),
    "R49 (2025)": ("Item 18 ·", ["Em 2025, os créditos adicionais financiados", "Na defesa (p. 84-85), a Cfamge"]),
}


def preencher(p, texto: str) -> None:
    if texto.startswith(ROTULOS) and ":" in texto:
        rotulo, _, resto = texto.partition(":")
        r = p.add_run(rotulo + ":")
        r.bold = True
        r.font.color.rgb = AZUL
        p.add_run(resto)
    else:
        p.add_run(texto)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY


def main() -> None:
    doc = Document(ARQ)
    pars = doc.paragraphs
    for ref, (titulo, antigos) in ALVOS.items():
        h = next(i for i, p in enumerate(pars) if p.style.name.startswith("Heading") and p.text.startswith(titulo))
        r = next(i for i in range(h, len(pars)) if pars[i].text.strip().upper().startswith("RESUMO DO TEMA"))
        velhos = pars[r + 1:r + 1 + len(antigos)]
        for p, ini in zip(velhos, antigos):
            if not p.text.strip().startswith(ini):
                raise SystemExit(f"{ref}: parágrafo inesperado – '{p.text[:60]}'. Nada foi gravado.")
        modelo = velhos[0]._p
        ancora = velhos[-1]._p.getnext()
        for p in velhos:
            p._p.getparent().remove(p._p)
        novos = RESUMOS[ref]
        for texto in novos:
            el = copy.deepcopy(modelo)
            for filho in list(el):
                if filho.tag.endswith("}r") or filho.tag.endswith("}hyperlink"):
                    el.remove(filho)
            ancora.addprevious(el)
            preencher(Paragraph(el, velhos[0]._parent), texto)
        pars = doc.paragraphs
        print(f"{ref}: {len(antigos)} parágrafo(s) substituído(s) por {len(novos)}")
    try:
        doc.save(ARQ)
    except PermissionError:
        raise SystemExit("Arquivo aberto no Word: feche-o e rode novamente. Nada foi gravado.")
    print(f"Atualizado: {ARQ.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
