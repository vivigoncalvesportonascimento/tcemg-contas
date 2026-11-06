"""Converte o CSV de itens a encaminhar a outras áreas em um Word simples para avaliação da chefia.

Entrada: data/demandas-resposta/oficio_sef_288_2026_itens_outras_areas_justificativa.csv
Saída:   entregas/demanda-01/Demanda01_Oficio_SEF_288_2026_itens_outras_areas_quadro_simples.docx
"""

import csv
from pathlib import Path

from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "data" / "demandas-resposta" / "oficio_sef_288_2026_itens_outras_areas_justificativa.csv"
SAIDA = RAIZ / "entregas" / "demanda-01" / "Demanda01_Oficio_SEF_288_2026_itens_outras_areas_quadro_simples.docx"

LARGURAS = [1.6, 6.2, 4.6, 3.4, 7.8]  # cm; soma = 23,6 (A4 paisagem com margens de 2 cm)


def sombrear(celula, cor: str) -> None:
    tc_pr = celula._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), cor)
    tc_pr.append(shd)


def escrever(celula, texto: str, negrito: bool = False) -> None:
    p = celula.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(texto)
    r.bold = negrito
    r.font.size = Pt(8.5)


def main() -> None:
    with open(ENTRADA, encoding="utf-8-sig", newline="") as f:
        linhas = list(csv.reader(f, delimiter=";"))
    cab, dados = linhas[0], linhas[1:]

    doc = Document()
    sec = doc.sections[0]
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width, sec.page_height = Cm(29.7), Cm(21.0)
    sec.left_margin = sec.right_margin = Cm(2)
    sec.top_margin = sec.bottom_margin = Cm(1.8)
    estilo = doc.styles["Normal"]
    estilo.font.name = "Calibri"
    estilo.font.size = Pt(10)

    doc.add_heading("Ofício SEF/STE nº 288/2026 – Itens a encaminhar a outras áreas", level=1)
    p = doc.add_paragraph(
        "Apontamentos do TCEMG que, no entendimento da SPLOR, não cabe a esta Subsecretaria responder. "
        "O quadro traz a unidade recomendada para cada um e os precedentes de encaminhamento já feitos "
        "pela SPLOR em ciclos anteriores. Processo SEI 1190.01.0016769/2026-46; resposta à SEF até 12/11/2026."
    )
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    doc.add_paragraph("Solicita-se à chefia avaliar o encaminhamento proposto para cada item.")

    titulos = ["Nº / Ref.", "Apontamento (TCE-MG)", "Breve descrição", "Envio recomendado", cab[6]]
    t = doc.add_table(rows=1, cols=len(titulos))
    t.style = "Table Grid"
    t.autofit = False
    for i, h in enumerate(titulos):
        escrever(t.rows[0].cells[i], h, negrito=True)
        sombrear(t.rows[0].cells[i], "D9E2F3")
    trPr = t.rows[0]._tr.get_or_add_trPr()
    th = OxmlElement("w:tblHeader")
    th.set(qn("w:val"), "true")
    trPr.append(th)

    for n, d in enumerate(dados, start=1):
        c = t.add_row().cells
        escrever(c[0], f"{n}\n{d[2]}\n({d[1]})", negrito=True)
        escrever(c[1], d[3])
        escrever(c[2], d[4])
        escrever(c[3], d[5].strip(), negrito=True)
        escrever(c[4], d[6])
        cant = OxmlElement("w:cantSplit")
        c[0]._tc.getparent().get_or_add_trPr().append(cant)

    for linha in t.rows:
        for celula, larg in zip(linha.cells, LARGURAS):
            celula.width = Cm(larg)

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    doc.save(SAIDA)
    print(f"{len(dados)} itens em {SAIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
