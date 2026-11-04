"""Análises quantitativas da Demanda 01 (Ofício SEF/STE nº 288/2026).

Bases: data/dados/execucao_2025.csv, execucao_2026.csv (Armazém Siafi) e ploa2027_base_qdd_fiscal.xlsx.
Uso:   poetry run python scripts/analise_demanda01.py
Saída: entregas/demanda-01/analises/*.csv e resumo impresso (copiado para resumo.txt)
"""

from __future__ import annotations

import io
from contextlib import redirect_stdout
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "data" / "dados"
SAIDA = RAIZ / "entregas" / "demanda-01" / "analises"

VALORES = ["Crédito Inicial", "Crédito Autorizado", "Empenhado", "Liquidado", "Pago Orçamentário"]
JANELA_MAX = 1_000  # dotação simbólica típica (R$ 1 mil)


def carregar_execucao(ano: int) -> pd.DataFrame:
    df = pd.read_csv(DADOS / f"execucao_{ano}.csv", sep=";", encoding="latin1", decimal=",")
    df.columns = [c.strip() for c in df.columns]
    for c in ("Programa Cod.", "Função Cód."):
        df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int64")
    return df


def carregar_ploa2027() -> pd.DataFrame:
    df = pd.read_excel(DADOS / "ploa2027_base_qdd_fiscal.xlsx")
    return df.rename(columns={
        "uo_cod": "Uo", "acao_cod": "Ação", "acao_desc": "Ação Desc.", "fonte_cod": "Fonte",
        "ipu_cod": "IPU", "grupo_cod": "Grupo", "programa_cod": "Programa Cod.",
        "programa_desc": "Programa Desc.", "vlr_loa_desp": "Crédito Inicial", "uo_nome_sigla": "Uo Sigla",
        "iag_cod": "IAG",
    })


def fmt(v: float) -> str:
    return f"R$ {v / 1e6:,.2f} mi".replace(",", "X").replace(".", ",").replace("X", ".")


def pct(v: float) -> str:
    return f"{v * 100:.2f}%".replace(".", ",")


# ----------------------------------------------------------------- R6/2022 e R29/D39
def execucao_por_programa(df: pd.DataFrame, ano: int) -> None:
    g = df.groupby(["Programa Cod.", "Programa Desc."], dropna=False)[VALORES].sum().reset_index()
    g = g[g["Crédito Autorizado"] > 0].copy()
    g["exec_empenho"] = g["Empenhado"] / g["Crédito Autorizado"]
    g["exec_liquidado"] = g["Liquidado"] / g["Crédito Autorizado"]
    g = g.sort_values("exec_empenho")
    g.to_csv(SAIDA / f"programas_execucao_{ano}.csv", sep=";", decimal=",", index=False, encoding="utf-8-sig")
    abaixo = g[g["exec_empenho"] < 0.5]
    print(f"\n== R6/2022 – Programas com execução (empenho/autorizado) < 50% – {ano}")
    print(f"Programas com crédito autorizado: {len(g)}; abaixo de 50%: {len(abaixo)} ({pct(len(abaixo) / len(g))})")
    abaixo_liq = g[g["exec_liquidado"] < 0.5]
    print(f"Pelo liquidado: {len(abaixo_liq)} ({pct(len(abaixo_liq) / len(g))})")
    print(f"Peso dos programas < 50% no autorizado: {pct(abaixo['Crédito Autorizado'].sum() / g['Crédito Autorizado'].sum())}")
    for _, r in abaixo.iterrows():
        print(f"  {r['Programa Cod.']:>4} {str(r['Programa Desc.'])[:60]:60} aut {fmt(r['Crédito Autorizado']):>18}"
              f"  emp {pct(r['exec_empenho']):>7}")

    # fontes predominantes do crédito autorizado não empenhado nos programas < 50%
    sub = df[df["Programa Cod."].isin(abaixo["Programa Cod."])]
    sub = sub.assign(saldo=sub["Crédito Autorizado"] - sub["Empenhado"])
    por_fonte = sub.groupby("Fonte")["saldo"].sum().sort_values(ascending=False)
    total = por_fonte.sum()
    print("  Saldo não empenhado desses programas por fonte (top 8):")
    for f, v in por_fonte.head(8).items():
        print(f"    fonte {f:>3}: {fmt(v):>18} ({pct(v / total)})")

    tot = df[VALORES].sum()
    print(f"\n== R29/D39 – Indicadores globais {ano}")
    print(f"Inicial {fmt(tot['Crédito Inicial'])} | Autorizado {fmt(tot['Crédito Autorizado'])} | "
          f"Empenhado {fmt(tot['Empenhado'])} | Liquidado {fmt(tot['Liquidado'])}")
    print(f"Liquidado/Autorizado ('Sucesso do Planejamento Orçamentário'): {pct(tot['Liquidado'] / tot['Crédito Autorizado'])}")
    print(f"Empenhado/Inicial: {pct(tot['Empenhado'] / tot['Crédito Inicial'])} "
          f"(variação {pct(tot['Empenhado'] / tot['Crédito Inicial'] - 1)})")


# ----------------------------------------------------------------- R40/2022 – janelas
def janelas(df: pd.DataFrame, rotulo: str, com_execucao: bool) -> pd.DataFrame:
    chave = ["Uo", "Uo Sigla", "Ação", "Ação Desc."]
    cols = ["Crédito Inicial"] + (["Crédito Autorizado", "Empenhado"] if com_execucao else [])
    g = df.groupby(chave, dropna=False)[cols].sum().reset_index()
    j = g[(g["Crédito Inicial"] > 0) & (g["Crédito Inicial"] <= JANELA_MAX)].copy()
    acoes_com_dotacao = (g["Crédito Inicial"] > 0).sum()
    print(f"\n== R40 – Janelas orçamentárias (ação/UO com crédito inicial ≤ R$ 1 mil) – {rotulo}")
    print(f"Ações (UO×ação) com dotação inicial: {acoes_com_dotacao}; janelas: {len(j)} ({pct(len(j) / acoes_com_dotacao)})")
    if com_execucao:
        sup = j[j["Crédito Autorizado"] > j["Crédito Inicial"]]
        exe = j[j["Empenhado"] > 0]
        print(f"Janelas suplementadas no exercício: {len(sup)} ({fmt(sup['Crédito Autorizado'].sum())} autorizados); "
              f"com empenho: {len(exe)} ({fmt(exe['Empenhado'].sum())})")
    # fontes das janelas (linhas de dotação)
    linhas = df.merge(j[["Uo", "Ação"]], on=["Uo", "Ação"])
    linhas = linhas[linhas["Crédito Inicial"] > 0]
    print("  Fontes das dotações-janela (top 8):", linhas["Fonte"].value_counts().head(8).to_dict())
    j.to_csv(SAIDA / f"janelas_{rotulo.replace(' ', '_')}.csv", sep=";", decimal=",", index=False, encoding="utf-8-sig")
    return j


# ----------------------------------------------------------------- D44/2025 – fonte 52
def fonte52(df: pd.DataFrame, rotulo: str, valor: str) -> None:
    f = df[df["Fonte"] == 52]
    g = f.groupby(["Uo", "Uo Sigla", "Ação", "Ação Desc."])[valor].sum().reset_index()
    g = g[g[valor] != 0].sort_values(valor, ascending=False)
    total = g[valor].sum()
    fora = g[~g["Uo"].isin(UOS_TFAMG)]
    print(f"\n== D44 – Fonte 52 (TFAMG) – {rotulo} [{valor}] total {fmt(total)}; fora de SEMAD/FEAM/IEF: "
          f"{fmt(fora[valor].sum())} ({pct(fora[valor].sum() / total if total else 0)})")
    for _, r in fora.iterrows():
        print(f"    UO {r['Uo']} {str(r['Uo Sigla'])[:28]:28} ação {r['Ação']} {str(r['Ação Desc.'])[:45]:45} {fmt(r[valor]):>16}")
    g.to_csv(SAIDA / f"fonte52_{rotulo.replace(' ', '_')}.csv", sep=";", decimal=",", index=False, encoding="utf-8-sig")


UOS_TFAMG: set[int] = set()  # preenchido em main() a partir das siglas


# ----------------------------------------------------------------- D42/D33 – ação 2417
def acao2417(df: pd.DataFrame, rotulo: str, valor: str) -> None:
    a = df[df["Ação"] == 2417]
    grupo1 = df[df["Grupo"] == 1][valor].sum()
    print(f"\n== D42/D33 – Ação 2417 – {rotulo} [{valor}]: {fmt(a[valor].sum())} em {a['Uo'].nunique()} UOs; "
          f"{pct(a[valor].sum() / grupo1)} do grupo 1 (pessoal) de todo o orçamento; "
          f"{pct(a[valor].sum() / df[valor].sum())} do total")
    prog = a.groupby(["Programa Cod.", "Programa Desc."])[valor].sum()
    print("  Programas:", {f"{k[0]} {k[1]}": fmt(v) for k, v in prog.items()})


# ----------------------------------------------------------------- R49/2025 – reserva de contingência
def reserva(df: pd.DataFrame, ano: int) -> None:
    r = df[df["Uo"] == 1991][["Crédito Inicial", "Crédito Autorizado", "Empenhado"]].sum()
    print(f"\n== R49 – UO 1991 Reserva de Contingência – {ano}: inicial {fmt(r['Crédito Inicial'])}, "
          f"autorizado {fmt(r['Crédito Autorizado'])}, anulado (inicial − autorizado) "
          f"{fmt(r['Crédito Inicial'] - r['Crédito Autorizado'])}")


def reserva_por_decreto(arquivo: Path) -> None:
    """Decretos (numeração Siafi) com anulação da UO 1991 – base de alterações orçamentárias."""
    d = pd.read_csv(arquivo, sep=";", encoding="cp1252", decimal=",")
    d.columns = [c.strip() for c in d.columns]
    decs = d.loc[d["Uo Cod."] == 1991, "Num. Decreto"].unique()
    linhas = []
    for n in decs:
        x = d[d["Num. Decreto"] == n]
        o19 = x[x["Origem Credito"] == 19]
        benef = o19.groupby("Uo Sigla")["Suplementação"].sum().sort_values(ascending=False)
        linhas.append({
            "decreto_siafi": n, "data_registro": str(x["Data Registro"].iloc[0])[:10],
            "lei": x["Lei Aprovação"].iloc[0],
            "anulacao_reserva": x.loc[x["Uo Cod."] == 1991, "Anulação"].sum(),
            "suplementacao_origem19": o19["Suplementação"].sum(),
            "suplementacao_total_decreto": x["Suplementação"].sum(),
            "outras_anulacoes_decreto": x.loc[x["Uo Cod."] != 1991, "Anulação"].sum(),
            "uos_beneficiadas": "; ".join(f"{k} {v / 1e6:.2f} mi" for k, v in benef.items()),
        })
    r = pd.DataFrame(linhas).sort_values("anulacao_reserva", ascending=False)
    r["decreto_misto"] = r["outras_anulacoes_decreto"] > 500
    r.to_csv(SAIDA / "reserva_contingencia_decretos_2026.csv", sep=";", decimal=",", index=False, encoding="utf-8-sig")
    tot = r["anulacao_reserva"].sum()
    o19_total = d.loc[d["Origem Credito"] == 19, "Suplementação"].sum()
    print(f"\n== R49 – Decretos 2026 (Siafi) com anulação da UO 1991: {len(r)} decretos, {fmt(tot)}; "
          f"suplementações com origem 19 (Anulação Reserva Contingência): {fmt(o19_total)}")
    print(f"  Decretos mistos (reserva + outras anulações): {int(r['decreto_misto'].sum())}, "
          f"{fmt(r.loc[r['decreto_misto'], 'anulacao_reserva'].sum())}; 3 maiores = "
          f"{pct(r['anulacao_reserva'].head(3).sum() / tot)}")
    for _, x in r.head(6).iterrows():
        print(f"    Siafi {x['decreto_siafi']:>4} ({x['data_registro']}): {fmt(x['anulacao_reserva']):>16} → {x['uos_beneficiadas']}")


def main() -> None:
    SAIDA.mkdir(parents=True, exist_ok=True)
    e25, e26, p27 = carregar_execucao(2025), carregar_execucao(2026), carregar_ploa2027()
    siglas = pd.concat([e25[["Uo", "Uo Sigla"]], e26[["Uo", "Uo Sigla"]]]).drop_duplicates()
    UOS_TFAMG.update(siglas[siglas["Uo Sigla"].str.contains(r"\b(?:SEMAD|FEAM|IEF)\b", regex=True, na=False)]["Uo"])
    # siglas do PLOA vêm por extenso: usar as mesmas UOs da execução

    buf = io.StringIO()
    with redirect_stdout(buf):
        print(f"UOs consideradas destinatárias da TFAMG: {sorted(UOS_TFAMG)}")
        execucao_por_programa(e25, 2025)
        janelas(e25, "LOA 2025", True)
        janelas(e26, "LOA 2026", False)
        janelas(p27, "PLOA 2027", False)
        fonte52(e25, "2025", "Empenhado")
        fonte52(e26, "2026 (até 30-10-2026)", "Empenhado")
        fonte52(e26, "LOA 2026", "Crédito Inicial")
        fonte52(p27, "PLOA 2027", "Crédito Inicial")
        acao2417(e25, "LOA 2025", "Crédito Inicial")
        acao2417(e25, "2025", "Empenhado")
        acao2417(e26, "LOA 2026", "Crédito Inicial")
        acao2417(p27, "PLOA 2027", "Crédito Inicial")
        reserva(e25, 2025)
        reserva(e26, 2026)
        reserva_por_decreto(DADOS / "alteracao_orcamentaria_2026.csv")
        print(f"\nPLOA 2027 – total QDD fiscal: {fmt(p27['Crédito Inicial'].sum())}")
    texto = buf.getvalue()
    (SAIDA / "resumo.txt").write_text(texto, encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main()
