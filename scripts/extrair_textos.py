"""Extrai o texto de todos os PDFs/DOCX de data/ para corpus/, preservando a estrutura de pastas.

Cada arquivo gera um .txt com marcadores "=== PÁGINA N ===" para permitir citar a página
nos relatórios do TCEMG. Arquivos já extraídos (mais novos que a origem) são pulados.

Uso:  poetry run python scripts/extrair_textos.py [--forcar]
"""

from __future__ import annotations

import sys
from pathlib import Path

import pymupdf as fitz
from docx import Document

RAIZ = Path(__file__).resolve().parent.parent
ORIGEM = RAIZ / "data"
DESTINO = RAIZ / "corpus"


def extrair_pdf(caminho: Path) -> tuple[str, int, int]:
    partes, vazias = [], 0
    with fitz.open(caminho) as doc:
        for i, pagina in enumerate(doc, start=1):
            texto = pagina.get_text("text")
            if not texto.strip():
                vazias += 1
            partes.append(f"\n=== PÁGINA {i} ===\n{texto}")
        return "".join(partes), len(doc), vazias


def extrair_docx(caminho: Path) -> tuple[str, int, int]:
    doc = Document(caminho)
    linhas = [p.text for p in doc.paragraphs]
    for tabela in doc.tables:
        for linha in tabela.rows:
            linhas.append(" | ".join(c.text.strip() for c in linha.cells))
    return "\n".join(linhas), 1, 0


def main() -> None:
    forcar = "--forcar" in sys.argv
    sem_texto = []
    for arq in sorted(ORIGEM.rglob("*")):
        if arq.suffix.lower() not in {".pdf", ".docx"}:
            continue
        saida = DESTINO / arq.relative_to(ORIGEM).with_suffix(".txt")
        if not forcar and saida.exists() and saida.stat().st_mtime >= arq.stat().st_mtime:
            continue
        saida.parent.mkdir(parents=True, exist_ok=True)
        try:
            extrator = extrair_pdf if arq.suffix.lower() == ".pdf" else extrair_docx
            texto, paginas, vazias = extrator(arq)
        except Exception as exc:  # noqa: BLE001 - registrar e seguir para o próximo arquivo
            print(f"ERRO  {arq.relative_to(RAIZ)}: {exc}")
            continue
        saida.write_text(texto, encoding="utf-8")
        if paginas and vazias / paginas > 0.5:
            sem_texto.append(arq.relative_to(RAIZ))
        print(f"ok    {arq.relative_to(RAIZ)} ({paginas} pág.)")
    if sem_texto:
        print("\nArquivos majoritariamente sem texto (provável digitalização, requer OCR):")
        for s in sem_texto:
            print(f"  - {s}")


if __name__ == "__main__":
    main()
