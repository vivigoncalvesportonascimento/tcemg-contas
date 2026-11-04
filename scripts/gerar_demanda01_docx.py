"""Gera o documento Word editável da Demanda 01 (Ofício SEF/STE nº 288/2026).

Uso:  poetry run python scripts/gerar_demanda01_docx.py
Saída: entregas/demanda-01/Demanda01_Oficio_SEF_288_2026_minuta_respostas_SPLOR.docx
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

sys.path.insert(0, str(Path(__file__).resolve().parent))
from demanda01_conteudo import BASES_NECESSARIAS, ENCAMINHAMENTOS, ITENS, PRAZO  # noqa: E402
from demanda01_resumos_revisados import ROTULOS  # noqa: E402

ROTULOS_SUGESTAO = ("Plano de ação", "Atos publicados:", "Registro sistêmico:", "Evidenciação no ato:",
                    "Evidenciação consolidada:")

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "entregas" / "demanda-01" / "Demanda01_Oficio_SEF_288_2026_minuta_respostas_SPLOR.docx"

AZUL = RGBColor(0x1F, 0x3A, 0x5F)
CINZA = RGBColor(0x55, 0x5F, 0x6B)
FUNDO_ROTULO = "E8EEF5"
FUNDO_CABEC = "1F3A5F"
FUNDO_APONT = "F3F4F6"
FUNDO_SUGEST = "EAF4EC"
FUNDO_ATENC = "FFF4E0"

CORRESP = {
    "R28 (2020)": "SEF (RGF) e SUGESP (medidas)",
    "R30 (2020) · R11 (2021)": "SUGESP (complementar)",
    "R12 (2021)": "SUGESP (complementar)",
    "R10 (2020)": "SEF (GRP/Siafi)",
    "R1 (2021)": "SEF (GRP/Siafi)",
    "D2 (2019) · R13 (2020) · DEA5 (2021)": "SEGOV (UPG) e SEF (GRP)",
    "D42 (2025)": "SUGESP e SEF (GRP)",
    "D33 (2021)": "SUGESP (folha)",
    "D44 (2025)": "SEF, AGE, SEMAD/FEAM",
    "R51 (2025)": "SEDESE / Grupo Coord. FEM",
    "R52 (2025)": "SEF (receitas/ASPS-MDE)",
    "R1 (2022)": "SEF (metas fiscais)",
}


# ----------------------------------------------------------------- utilitários de formatação
def sombrear(celula, cor_hex: str) -> None:
    tc_pr = celula._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), cor_hex)
    tc_pr.append(shd)


def margens_celula(celula, topo=60, base=60, esq=100, dir_=100) -> None:
    tc_pr = celula._tc.get_or_add_tcPr()
    mar = OxmlElement("w:tcMar")
    for nome, valor in (("top", topo), ("bottom", base), ("start", esq), ("end", dir_)):
        el = OxmlElement(f"w:{nome}")
        el.set(qn("w:w"), str(valor))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tc_pr.append(mar)


def larguras(tabela, cms: list[float]) -> None:
    tabela.autofit = False
    for linha in tabela.rows:
        for i, celula in enumerate(linha.cells):
            celula.width = Cm(cms[i])


def nao_quebrar_linhas(tabela) -> None:
    for linha in tabela.rows:
        tr_pr = linha._tr.get_or_add_trPr()
        el = OxmlElement("w:cantSplit")
        el.set(qn("w:val"), "true")
        tr_pr.append(el)


def visao_curta(visao: str) -> str:
    if visao.startswith("—"):
        return "Sem posição (PP 2022)"
    if visao.startswith("Proposta"):
        return "Proposta (pendente Pleno)"
    return visao


def repetir_cabecalho(linha) -> None:
    tr_pr = linha._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "true")
    tr_pr.append(el)


def texto_celula(celula, texto: str, negrito=False, cor=None, tamanho=None, alinhamento=None) -> None:
    celula.text = ""
    par = celula.paragraphs[0]
    run = par.add_run(texto)
    run.bold = negrito
    if cor is not None:
        run.font.color.rgb = cor
    if tamanho:
        run.font.size = Pt(tamanho)
    if alinhamento is not None:
        par.alignment = alinhamento
    par.paragraph_format.space_after = Pt(0)


def campo_pagina(paragrafo) -> None:
    for tipo, texto in (("begin", None), (None, "PAGE"), ("end", None)):
        if tipo:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), tipo)
            paragrafo.add_run()._r.append(el)
        else:
            instr = OxmlElement("w:instrText")
            instr.set(qn("xml:space"), "preserve")
            instr.text = texto
            paragrafo.add_run()._r.append(instr)


def caixa(doc, titulo: str, paragrafos: list[str], cor_fundo: str, marcadores=False) -> None:
    """Tabela de uma célula sombreada, usada como 'quadro' editável."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.rows[0].cells[0]
    sombrear(c, cor_fundo)
    margens_celula(c, 120, 120, 160, 160)
    c.width = Cm(17)
    p = c.paragraphs[0]
    r = p.add_run(titulo)
    r.bold = True
    r.font.color.rgb = AZUL
    p.paragraph_format.space_after = Pt(4)
    for texto in paragrafos:
        par = c.add_paragraph(style="List Bullet" if marcadores else None)
        if not marcadores and texto.lower().startswith("status:"):
            rr = par.add_run(texto)
            rr.bold = True
        elif not marcadores and texto.startswith(ROTULOS_SUGESTAO):
            rotulo, _, resto = texto.partition(":")
            rr = par.add_run(rotulo + ":")
            rr.bold = True
            par.add_run(resto)
        else:
            par.add_run(texto)
        par.paragraph_format.space_after = Pt(4)
        if not marcadores:
            par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def paragrafo_rotulado(p, texto: str) -> None:
    """Escreve o texto no parágrafo; se começar por um rótulo conhecido, o trecho até ':' fica em negrito."""
    if texto.startswith(ROTULOS) and ":" in texto:
        rotulo, _, resto = texto.partition(":")
        r = p.add_run(rotulo + ":")
        r.bold = True
        r.font.color.rgb = AZUL
        p.add_run(resto)
    else:
        p.add_run(texto)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY


def subtitulo(doc, texto: str) -> None:
    p = doc.add_paragraph()
    r = p.add_run(texto.upper())
    r.bold = True
    r.font.size = Pt(9.5)
    r.font.color.rgb = AZUL
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True


# ----------------------------------------------------------------- construção do documento
def configurar(doc) -> None:
    estilo = doc.styles["Normal"]
    estilo.font.name = "Calibri"
    estilo.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    estilo.font.size = Pt(10.5)
    estilo.paragraph_format.space_after = Pt(4)
    for nome, tam in (("Heading 1", 15), ("Heading 2", 12.5), ("Heading 3", 11)):
        h = doc.styles[nome]
        h.font.name = "Calibri"
        h.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
        h.font.size = Pt(tam)
        h.font.color.rgb = AZUL
        h.font.bold = True
        h.paragraph_format.space_before = Pt(14 if nome == "Heading 1" else 10)
        h.paragraph_format.space_after = Pt(6)
        h.paragraph_format.keep_with_next = True

    sec = doc.sections[0]
    sec.page_height, sec.page_width = Cm(29.7), Cm(21.0)
    sec.orientation = WD_ORIENT.PORTRAIT
    sec.top_margin = sec.bottom_margin = Cm(2.0)
    sec.left_margin = sec.right_margin = Cm(2.0)
    sec.different_first_page_header_footer = True

    cab = sec.header.paragraphs[0]
    r = cab.add_run("SEPLAG/SPLOR · Demanda 01 · Ofício SEF/STE nº 288/2026 · MINUTA PARA DISCUSSÃO INTERNA")
    r.font.size = Pt(8)
    r.font.color.rgb = CINZA
    cab.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    rod = sec.footer.paragraphs[0]
    rod.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = rod.add_run("Página ")
    r.font.size = Pt(8)
    campo_pagina(rod)


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
    r = p.add_run("Demanda 01\nMonitoramento das recomendações e determinações do TCEMG")
    r.bold = True
    r.font.size = Pt(24)
    r.font.color.rgb = AZUL
    p = doc.add_paragraph()
    r = p.add_run("Subsídios e minutas de resposta ao Ofício SEF/STE nº 288/2026 – Pareceres Prévios 2019 a 2022 "
                  "(1º ciclo de 2026) e propostas do Relatório da Análise da Defesa – exercício 2025")
    r.font.size = Pt(13)
    doc.add_paragraph()
    t = doc.add_table(rows=4, cols=2)
    dados = [
        ("Processo SEI", "1190.01.0016769/2026-46"),
        ("Prazo de resposta à SEF", PRAZO),
        ("Apontamentos analisados", f"{len(ITENS)} (direcionamento SPLOR: responder)"),
        ("Versão", f"Minuta para discussão da equipe – {date.today():%d/%m/%Y}"),
    ]
    for linha, (k, v) in zip(t.rows, dados):
        texto_celula(linha.cells[0], k, negrito=True, cor=AZUL)
        texto_celula(linha.cells[1], v)
        sombrear(linha.cells[0], FUNDO_ROTULO)
    larguras(t, [5.5, 11.5])
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def introducao(doc) -> None:
    doc.add_heading("1. Objetivo e orientações", level=1)
    textos = [
        "Este documento reúne os subsídios para a resposta da SPLOR/SEPLAG ao Ofício SEF/STE nº 288/2026, que "
        "solicita informações atualizadas para o 1º ciclo de monitoramento de 2026 das determinações e "
        "recomendações dos Pareceres Prévios de 2019 a 2022. Também apresenta as propostas de determinação e "
        "recomendação do Relatório da Análise da Defesa do Estado (exercício 2025), ainda pendentes de "
        "aprovação pelo Tribunal Pleno.",
        "Foram analisados os itens classificados na coluna 'SPLOR – Direcionamento' como 'Responder', "
        "'Verificar antes de responder se deve ser recomendado a SUGESP/SEPLAG e SEF' ou 'Responder, mas "
        "verificar se esbarra em competência da SPLOR/SEPLAG'. A competência foi verificada à luz do Decreto "
        "nº 48.636/2023 (SEPLAG) e do Decreto nº 48.680/2023 (SEF).",
        "Para cada apontamento, a ficha traz: o texto do apontamento; um resumo do tema, com as páginas dos "
        "relatórios do TCEMG; a análise de competência; as duas últimas respostas do Governo de MG; a minuta "
        "de resposta sugerida; os pontos de atenção que a equipe precisa validar antes do envio.",
        "As respostas anteriores foram levantadas por varredura de todo o acervo data/respostas-splor (119 "
        "documentos, de 2023 a 21/10/2026), por palavras-chave do tema, com o script "
        "scripts/buscar_respostas_anteriores.py. Não se limitaram aos ofícios de monitoramento: incluem os "
        "relatórios temáticos, as defesas dos Balanços, alertas e representações. Para cada ficha, a tabela traz "
        "as duas manifestações mais recentes sobre o tema, mesmo que relativas a apontamento similar, e a linha "
        "seguinte lista as demais manifestações relacionadas encontradas, para consulta da equipe.",
    ]
    for t in textos:
        p = doc.add_paragraph(t)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    subtitulo(doc, "Formato exigido pela SEF para cada item")
    for t in [
        "Posição atual: 'Atendida', 'Em tratamento' ou 'Não iniciada'.",
        "Atendida: justificativas e documentos/evidências que comprovem o atendimento.",
        "Em tratamento: medidas em curso e, se aplicável, Plano de Ação (medidas, prazos, unidades e contatos "
        "responsáveis).",
        "Não iniciada: justificativa, prazo estimado de início, Plano de Ação e empecilhos/fatores de risco.",
    ]:
        doc.add_paragraph(t, style="List Bullet")

    subtitulo(doc, "Convenções desta minuta")
    for t in [
        "Trechos entre [colchetes] indicam informação a confirmar ou completar pela equipe antes do envio.",
        "Páginas citadas seguem a numeração impressa nos relatórios do TCEMG. 'BGE 2025' é o Relatório sobre "
        "a Macrogestão e Contas do Governador – exercício 2025. 'Defesa 2025' é o Relatório de Análise da "
        "Defesa do Estado – exercício 2025.",
        "Prazos e responsáveis dos planos de ação são sugestões e devem ser pactuados com as áreas citadas.",
    ]:
        doc.add_paragraph(t, style="List Bullet")


def quadro_resumo(doc) -> None:
    doc.add_heading("2. Quadro-resumo", level=1)
    cab = ["Nº", "Referência", "Tema", "Visão TCE-MG", "Status sugerido", "Envolver também"]
    t = doc.add_table(rows=1, cols=len(cab))
    t.style = "Table Grid"
    for i, h in enumerate(cab):
        c = t.rows[0].cells[i]
        texto_celula(c, h, negrito=True, cor=RGBColor(0xFF, 0xFF, 0xFF), tamanho=9)
        sombrear(c, FUNDO_CABEC)
    repetir_cabecalho(t.rows[0])
    for n, it in enumerate(ITENS, start=1):
        linha = t.add_row().cells
        valores = [str(n), it["ref"], it["tema"], visao_curta(it["visao_tce"]), it["status"],
                   CORRESP.get(it["ref"], "—")]
        for i, v in enumerate(valores):
            texto_celula(linha[i], v, tamanho=8.5, negrito=(i == 4))
        if n % 2 == 0:
            for c in linha:
                sombrear(c, "F7F9FC")
    nao_quebrar_linhas(t)
    larguras(t, [0.8, 3.0, 5.2, 2.8, 2.2, 3.0])


def ficha(doc, n: int, it: dict) -> None:
    if n > 1:
        doc.add_page_break()
    doc.add_heading(f"Item {n} · {it['ref']} — {it['tema']}", level=2)

    meta = [
        ("Origem", it["origem"]),
        ("Ano(s) de referência", it["anos"]),
        ("Visão TCE-MG", it["visao_tce"]),
        ("Direcionamento SPLOR", it["direcionamento"]),
        ("Páginas nos relatórios", it["paginas"]),
        ("Status sugerido", it["status"]),
    ]
    t = doc.add_table(rows=len(meta), cols=2)
    t.style = "Table Grid"
    for linha, (k, v) in zip(t.rows, meta):
        texto_celula(linha.cells[0], k, negrito=True, cor=AZUL, tamanho=9)
        texto_celula(linha.cells[1], v, tamanho=9, negrito=(k == "Status sugerido"))
        sombrear(linha.cells[0], FUNDO_ROTULO)
    larguras(t, [4.2, 12.8])

    subtitulo(doc, "Apontamento a ser respondido")
    caixa(doc, f"{it['ref']}", [it["texto"]], FUNDO_APONT)

    subtitulo(doc, "Resumo do tema (relatórios do TCEMG)")
    for par in it["resumo"]:
        paragrafo_rotulado(doc.add_paragraph(), par)

    subtitulo(doc, "Análise de competência")
    p = doc.add_paragraph(it["competencia"])
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    subtitulo(doc, "Duas últimas respostas da SPLOR/Governo de MG sobre o tema")
    cab = ["Documento", "Data", "Status informado", "Síntese"]
    t = doc.add_table(rows=1, cols=4)
    t.style = "Table Grid"
    for i, h in enumerate(cab):
        texto_celula(t.rows[0].cells[i], h, negrito=True, cor=RGBColor(0xFF, 0xFF, 0xFF), tamanho=9)
        sombrear(t.rows[0].cells[i], FUNDO_CABEC)
    for doc_, data_, status_, sintese in it["respostas"]:
        linha = t.add_row().cells
        for i, v in enumerate((doc_, data_, status_, sintese)):
            texto_celula(linha[i], v, tamanho=8.5)
    nao_quebrar_linhas(t)
    larguras(t, [4.0, 1.9, 2.3, 8.8])
    if it.get("outras"):
        p = doc.add_paragraph()
        r = p.add_run("Outras manifestações relacionadas no acervo (data/respostas-splor): ")
        r.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = AZUL
        r2 = p.add_run(it["outras"])
        r2.font.size = Pt(9)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

    subtitulo(doc, "Sugestão de resposta ao TCEMG")
    caixa(doc, "Minuta (editável)", it["sugestao"], FUNDO_SUGEST)

    subtitulo(doc, "Pontos de atenção antes do envio")
    caixa(doc, "Validar com a equipe", it["atencao"], FUNDO_ATENC, marcadores=True)


def anexos(doc) -> None:
    doc.add_page_break()
    doc.add_heading("3. Itens do Ofício encaminhados a outras áreas", level=1)
    doc.add_paragraph("Itens classificados no quadro de controle como 'Recomendar envio' a outras unidades, por "
                      "não serem de competência da SPLOR. Sugere-se encaminhá-los por memorando, informando o "
                      "prazo de 12/11/2026.").alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    t = doc.add_table(rows=1, cols=4)
    t.style = "Table Grid"
    for i, h in enumerate(["Referência", "Tema", "Destino", "Observação"]):
        texto_celula(t.rows[0].cells[i], h, negrito=True, cor=RGBColor(0xFF, 0xFF, 0xFF), tamanho=9)
        sombrear(t.rows[0].cells[i], FUNDO_CABEC)
    for linha_ in ENCAMINHAMENTOS:
        cells = t.add_row().cells
        for i, v in enumerate(linha_):
            texto_celula(cells[i], v, tamanho=8.5, negrito=(i == 2))
    nao_quebrar_linhas(t)
    larguras(t, [3.4, 5.0, 2.4, 6.2])

    doc.add_heading("4. Bases de dados utilizadas e pendentes", level=1)
    for b in BASES_NECESSARIAS:
        doc.add_paragraph(b, style="List Bullet")

    doc.add_heading("5. Observações sobre respostas anteriores e compromissos assumidos", level=1)
    for t_ in [
        "Compromissos da NT 21/2026 verificados nas bases: (i) D44: a Fonte 52 saiu do FFP e da PMMG no PLOA "
        "2027 (cumprido na programação), mas houve execução pela PMMG em 2026; (ii) D22: as melhorias no "
        "demonstrativo do IMRS 'já na LOA 2027' não constam do PLOA 2027 (não cumprido); (iii) D42/D33: a Ação "
        "2417 foi mantida e ampliada no PLOA 2027.",
        "O Memo SEPLAG/SPLOR nº 198/2025 contém, ao final da resposta ao item R1 (relatório 2023), a frase "
        "residual 'Se quiser, posso deixar o texto mais técnico ou mais sintético.' Recomenda-se revisão final "
        "cuidadosa dos textos antes da assinatura.",
        "O mesmo memorando atribuiu status 'Atendida' à D6/2020 (ODS), embora o texto informe que o painel não "
        "estava concluído. A sugestão desta minuta é 'Em tratamento', em linha com a visão do TCE.",
        "Há diferença entre o IAP 2025 informado pela SPLOR (51,04%, NT 21/2026) e o apurado pela Cfamge "
        "(50,57, BGE 2025, p. 700). Convém harmonizar.",
        "Para o item IPU, o OF SPLOR 13/2025 encaminhou à SEGOV o item correlato (R7/2022), e o Memo 195/2025 "
        "respondeu diretamente. Esta minuta propõe resposta da SPLOR, citando SEGOV e SEF.",
    ]:
        doc.add_paragraph(t_, style="List Bullet")

    doc.add_heading("6. Fontes consultadas", level=1)
    fontes = [
        "Ofício SEF/STE nº 288/2026 e quadro de controle (data/demandas-resposta).",
        "TCEMG – Relatório sobre a Macrogestão e Contas do Governador, exercícios 2023, 2024 e 2025; "
        "Relatório de Análise da Defesa do Estado, exercício 2025; Of. TCEMG 21465/2026 – Decreto NE 673/2026 (data/analise-contas).",
        "Respostas SPLOR: Nota Técnica nº 21/2026; Memorandos nº 149/2026, 195/2025 e 198/2025; Ofício nº 13/2025; Nota "
        "Técnica nº 38/2024 (data/respostas-splor).",
        "Relatório de Transição SPLOR 2026, versão de 28/10/2026; RGF 2026 – 2º quadrimestre "
        "(data/documentacao-complementar).",
        "Decreto nº 48.636/2023 (SEPLAG); Decreto nº 48.680/2023 (SEF); LC 101/2000; Lei 19.990/2011; "
        "Classificador Econômico da Despesa (07/10/2026); LOA 2026 e PLOA 2027, volumes 1 e 5 "
        "(data/legislacao-basica).",
        "Execução orçamentária 2025 e 2026, alterações orçamentárias 2026 (Armazém Siafi) e QDD fiscal do PLOA 2027 (data/dados), "
        "processados por scripts/analise_demanda01.py.",
    ]
    for f in fontes:
        doc.add_paragraph(f, style="List Bullet")


def main() -> None:
    doc = Document()
    configurar(doc)
    capa(doc)
    introducao(doc)
    quadro_resumo(doc)
    doc.add_page_break()
    doc.add_heading("Fichas dos apontamentos", level=1)
    doc.add_paragraph("Cada ficha a seguir corresponde a um apontamento do Ofício SEF/STE nº 288/2026 com "
                      "direcionamento para resposta da SPLOR.")
    for n, it in enumerate(ITENS, start=1):
        ficha(doc, n, it)
    anexos(doc)
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    doc.save(SAIDA)
    print(f"Documento gerado: {SAIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
