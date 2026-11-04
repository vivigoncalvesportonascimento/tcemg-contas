"""Gera o Word com os itens do Ofício SEF/STE nº 288/2026 encaminhados a outras áreas (validação da chefia).

Uso:  poetry run python scripts/gerar_demanda01_encaminhamentos_docx.py
Saída: entregas/demanda-01/Demanda01_Oficio_SEF_288_2026_itens_outras_areas.docx
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.shared import Cm, Pt, RGBColor

sys.path.insert(0, str(Path(__file__).resolve().parent))
from demanda01_conteudo import PRAZO  # noqa: E402
from demanda01_encaminhamentos import ITENS  # noqa: E402
from gerar_demanda01_docx import (  # noqa: E402
    AZUL, CINZA, FUNDO_APONT, FUNDO_ATENC, FUNDO_CABEC, FUNDO_ROTULO, FUNDO_SUGEST, caixa, configurar, larguras,
    nao_quebrar_linhas, repetir_cabecalho, sombrear, subtitulo, texto_celula,
)

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "entregas" / "demanda-01" / "Demanda01_Oficio_SEF_288_2026_itens_outras_areas.docx"
BRANCO = RGBColor(0xFF, 0xFF, 0xFF)


def capa(doc) -> None:
    for _ in range(5):
        doc.add_paragraph()
    p = doc.add_paragraph()
    r = p.add_run("GOVERNO DO ESTADO DE MINAS GERAIS\nSecretaria de Estado de Planejamento e Gestão\n"
                  "Subsecretaria de Planejamento e Orçamento – SPLOR")
    r.font.size = Pt(11)
    r.font.color.rgb = CINZA
    doc.add_paragraph()
    p = doc.add_paragraph()
    r = p.add_run("Demanda 01\nItens a encaminhar a outras áreas")
    r.bold = True
    r.font.size = Pt(24)
    r.font.color.rgb = AZUL
    p = doc.add_paragraph()
    r = p.add_run("Ofício SEF/STE nº 288/2026 – apontamentos do TCEMG que não são de competência da SPLOR e "
                  "proposta de encaminhamento, para validação da chefia")
    r.font.size = Pt(13)
    doc.add_paragraph()
    t = doc.add_table(rows=4, cols=2)
    for linha, (k, v) in zip(t.rows, [
        ("Processo SEI", "1190.01.0016769/2026-46"),
        ("Prazo de resposta à SEF", PRAZO),
        ("Itens", f"{len(ITENS)} apontamentos com direcionamento a outras áreas"),
        ("Versão", f"Para validação da chefia – {date.today():%d/%m/%Y}"),
    ]):
        texto_celula(linha.cells[0], k, negrito=True, cor=AZUL)
        texto_celula(linha.cells[1], v)
        sombrear(linha.cells[0], FUNDO_ROTULO)
    larguras(t, [5.5, 11.5])
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def introducao(doc) -> None:
    doc.add_heading("1. Objetivo", level=1)
    for texto in [
        "Este documento reúne os apontamentos do Ofício SEF/STE nº 288/2026 que, pelo quadro de controle da "
        "SPLOR, não serão respondidos por esta Subsecretaria, por tratarem de matérias de competência de outras "
        "áreas. Para cada um, apresenta o apontamento, um resumo do que o TCEMG demanda (com as páginas dos "
        "relatórios), o fundamento do encaminhamento e a área recomendada.",
        "Solicita-se à chefia validar, item a item, se o encaminhamento proposto está correto, assinalando 'De "
        "acordo' ou indicando o ajuste no campo próprio. Após a validação, sugere-se encaminhar os itens às "
        "áreas por memorando, com cópia do Ofício 288 e prazo compatível com a resposta à SEF, em 12/11/2026.",
        "Critério: o direcionamento parte da coluna 'SPLOR – Direcionamento' do quadro de controle e foi "
        "conferido com as competências do Decreto nº 48.636/2023 (art. 69 – SUGER; art. 77 – SUGESP) e com os "
        "encaminhamentos já feitos pela SPLOR em ciclos anteriores do mesmo monitoramento.",
    ]:
        doc.add_paragraph(texto).alignment = WD_ALIGN_PARAGRAPH.JUSTIFY


def quadro(doc) -> None:
    doc.add_heading("2. Quadro-resumo", level=1)
    cab = ["Nº", "Referência", "Tema", "Visão TCE-MG", "Encaminhar para", "Validação"]
    t = doc.add_table(rows=1, cols=len(cab))
    t.style = "Table Grid"
    for i, h in enumerate(cab):
        texto_celula(t.rows[0].cells[i], h, negrito=True, cor=BRANCO, tamanho=9)
        sombrear(t.rows[0].cells[i], FUNDO_CABEC)
    repetir_cabecalho(t.rows[0])
    for n, it in enumerate(ITENS, start=1):
        c = t.add_row().cells
        for i, v in enumerate([str(n), it["ref"], it["tema"], it["visao"], it["destino"], "☐ De acordo\n☐ Ajustar"]):
            texto_celula(c[i], v, tamanho=8.5, negrito=(i == 4))
    nao_quebrar_linhas(t)
    larguras(t, [0.8, 2.9, 5.0, 2.7, 3.3, 2.3])


def ficha(doc, n: int, it: dict) -> None:
    doc.add_page_break()
    doc.add_heading(f"Item {n} · {it['ref']} — {it['tema']}", level=2)
    t = doc.add_table(rows=4, cols=2)
    t.style = "Table Grid"
    for linha, (k, v) in zip(t.rows, [
        ("Visão TCE-MG", it["visao"]),
        ("Direcionamento no quadro", it["direcionamento_csv"]),
        ("Páginas nos relatórios", it["paginas"]),
        ("Encaminhamento proposto", it["destino"]),
    ]):
        texto_celula(linha.cells[0], k, negrito=True, cor=AZUL, tamanho=9)
        texto_celula(linha.cells[1], v, tamanho=9, negrito=(k == "Encaminhamento proposto"))
        sombrear(linha.cells[0], FUNDO_ROTULO)
    larguras(t, [4.2, 12.8])

    subtitulo(doc, "Apontamento")
    caixa(doc, it["ref"], [it["texto"]], FUNDO_APONT)

    subtitulo(doc, "O que o TCEMG demanda")
    for par in it["demanda"]:
        doc.add_paragraph(par).alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    subtitulo(doc, "Fundamento do encaminhamento")
    for par in it["fundamento"]:
        doc.add_paragraph(par, style="List Bullet").alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    subtitulo(doc, "Recomendação da SPLOR")
    caixa(doc, f"Encaminhar para: {it['destino']}", [f"Participação da SPLOR: {it['apoio']}"], FUNDO_SUGEST)

    subtitulo(doc, "Validação da chefia")
    v = doc.add_table(rows=1, cols=1)
    v.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = v.rows[0].cells[0]
    sombrear(c, FUNDO_ATENC)
    c.width = Cm(17)
    texto_celula(c, "☐ De acordo com o encaminhamento        ☐ Ajustar para: ______________________________\n"
                    "Observações: ____________________________________________________________________",
                 tamanho=9.5)


def main() -> None:
    doc = Document()
    configurar(doc)
    capa(doc)
    introducao(doc)
    quadro(doc)
    for n, it in enumerate(ITENS, start=1):
        ficha(doc, n, it)
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    doc.save(SAIDA)
    print(f"Documento gerado: {SAIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
