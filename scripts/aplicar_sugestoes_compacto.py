"""Aplica as sugestões revisadas (itens 4, 7 e 18) na versão compacta editada manualmente, sem regenerá-la.

Por item: substitui o conteúdo da caixa "Minuta (editável)", acrescenta os novos pontos à caixa
"Validar com a equipe" e atualiza a linha "Outras manifestações relacionadas". O restante é preservado.

Uso: poetry run python scripts/aplicar_sugestoes_compacto.py
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

from docx import Document
from docx.shared import RGBColor
from docx.table import Table
from docx.text.paragraph import Paragraph

sys.path.insert(0, str(Path(__file__).resolve().parent))
from demanda01_sugestoes_revisadas import ATENCAO_EXTRA, OUTRAS, SUGESTOES  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
ARQ = RAIZ / "entregas" / "demanda-01" / "Demanda01_Oficio_SEF_288_2026_minuta_respostas_SPLOR_revisado_compacto.docx"
AZUL = RGBColor(0x1F, 0x3A, 0x5F)
TITULOS = {"R10 (2020)": "Item 4 ·", "R1 (2021)": "Item 7 ·", "R49 (2025)": "Item 18 ·"}
ROTULOS = ("Status:", "Plano de ação", "Atos publicados:", "Registro sistêmico:", "Evidenciação no ato:",
           "Evidenciação consolidada:")


def blocos_do_item(doc, prefixo):
    """Retorna (paragrafos, tabelas) entre o título do item e o próximo título."""
    corpo = doc.element.body
    dentro, pars, tabs = False, [], []
    for el in corpo.iterchildren():
        if el.tag.endswith("}p"):
            p = Paragraph(el, doc._body)
            if p.style is not None and p.style.name.startswith("Heading") and p.text.strip():
                if dentro:
                    break
                dentro = p.text.startswith(prefixo)
                continue
            if dentro:
                pars.append(p)
        elif el.tag.endswith("}tbl") and dentro:
            tabs.append(Table(el, doc._body))
    return pars, tabs


def novo_paragrafo_apos(modelo: Paragraph, ancora_el, texto: str, rotular=True):
    el = copy.deepcopy(modelo._p)
    for filho in list(el):
        if filho.tag.endswith("}r") or filho.tag.endswith("}hyperlink"):
            el.remove(filho)
    ancora_el.addnext(el)
    p = Paragraph(el, modelo._parent)
    if rotular and texto.startswith(ROTULOS) and ":" in texto:
        rot, _, resto = texto.partition(":")
        r = p.add_run(rot + ":")
        r.bold = True
        p.add_run(resto)
    else:
        p.add_run(texto)
    return el


def main() -> None:
    doc = Document(ARQ)
    for ref, prefixo in TITULOS.items():
        pars, tabs = blocos_do_item(doc, prefixo)
        caixa = next(t for t in tabs if len(t.rows) == 1 and t.cell(0, 0).text.startswith("Minuta"))
        cel = caixa.cell(0, 0)
        cps = cel.paragraphs
        modelo = cps[2] if len(cps) > 2 else cps[1]  # parágrafo comum (não o de status)
        for p in cps[1:]:
            if p is not modelo:
                p._p.getparent().remove(p._p)
        ancora = cps[0]._p
        for texto in SUGESTOES[ref]:
            ancora = novo_paragrafo_apos(modelo, ancora, texto)
        modelo._p.getparent().remove(modelo._p)
        msg = f"{ref}: sugestão substituída ({len(SUGESTOES[ref])} parágrafos)"

        if ref in ATENCAO_EXTRA:
            at = next(t for t in tabs if len(t.rows) == 1 and t.cell(0, 0).text.startswith("Validar"))
            ultimo = at.cell(0, 0).paragraphs[-1]
            ancora = ultimo._p
            for texto in ATENCAO_EXTRA[ref]:
                ancora = novo_paragrafo_apos(ultimo, ancora, texto, rotular=False)
            msg += f"; +{len(ATENCAO_EXTRA[ref])} ponto(s) de atenção"

        if ref in OUTRAS:
            p = next(p for p in pars if p.text.startswith("Outras manifestações relacionadas"))
            p.runs[-1].text = OUTRAS[ref]
            for r in p.runs[1:-1]:
                r.text = ""
            msg += "; 'outras manifestações' atualizada"
        print(msg)
    try:
        doc.save(ARQ)
    except PermissionError:
        raise SystemExit("Arquivo aberto no Word: feche-o e rode novamente. Nada foi gravado.")
    print(f"Atualizado: {ARQ.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
