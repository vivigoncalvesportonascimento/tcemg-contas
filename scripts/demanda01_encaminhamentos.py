"""Itens do Ofício SEF/STE nº 288/2026 que a SPLOR não responde diretamente (direcionamento a outras áreas).

Fonte do direcionamento: coluna "SPLOR - Direcionamento" do quadro
data/demandas-resposta/oficio_sef_288_2026_quadro_recomendacoes_determinacoes.csv.
Competências: Decreto nº 48.636/2023 (SEPLAG) – art. 69 (SUGER) e art. 77 (SUGESP).
"""

ART69 = ("Decreto 48.636/2023, art. 69: compete à SUGER 'planejar, coordenar e acompanhar as políticas "
         "estratégicas e a elaboração e revisão do PMDI' (I), 'estabelecer as diretrizes para definição dos "
         "projetos estratégicos' (II), 'manter sistemática de monitoramento de projetos estratégicos' (III) e "
         "'coordenar a implementação das ações previstas nos Acordos Judiciais de Reparação' e a gestão dos "
         "recursos das fontes 95 e 80 (VII e VIII).")

ITENS = [
    {
        "ref": "R13 (2019) · D32 (2021)",
        "tema": "Aportes nas ações de Acompanhamento Intensivo (Projetos Estratégicos)",
        "texto": "Atentar para o histórico de redução dos aportes nas ações de Acompanhamento Intensivo, assim como "
                 "para a baixa aderência da execução orçamentária ao planejamento.",
        "visao": "Parcialmente Atendida (Ofício) / Não Atendida (BGE 2025)",
        "direcionamento_csv": "Recomendar envio para SUGER",
        "paginas": "BGE 2025, p. 705 · BGE 2024, p. 606",
        "demanda": [
            "As ações de 'Acompanhamento Intensivo' passaram a se chamar Projetos Estratégicos em 2020. O TCEMG "
            "quer saber por que a participação orçamentária dessas ações vem caindo e por que sua execução "
            "segue pouco aderente ao planejado.",
            "No BGE 2025 (p. 705), a Cfamge apontou que a participação dos Projetos Estratégicos caiu de 4,54% "
            "para 1,84% da despesa empenhada entre 2021 e 2025. Também registrou a baixa aderência da execução "
            "ao planejamento, ligada à piora do IAP desses projetos (ver D28). Por isso, considerou o item Não "
            "Atendido. Ressalvou que o destaque dos projetos decorre do monitoramento diferenciado, e não "
            "necessariamente de prioridade de recursos.",
        ],
        "fundamento": [
            ART69,
            "Histórico de direcionamento: a SPLOR já encaminhou este item à área de gestão estratégica por meio "
            "dos Memos SPLOR 109/2024 e 127/2024 (NT 38/2024), do Memo SPLOR 50/2025 (OF SPLOR 13/2025) e do "
            "Memo SPLOR 198/2025. Na NT 21/2026 (defesa do BGE 2025), também o indicou como competência da "
            "SUGER.",
        ],
        "destino": "SUGER",
        "apoio": "A parte de 'aderência da execução ao planejamento' envolve dados orçamentários. A SPLOR pode "
                 "fornecer à SUGER, se solicitado, a série de crédito inicial, autorizado e empenhado das ações "
                 "com IAG de Projeto Estratégico.",
    },
    {
        "ref": "R19 (2019) · D36 (2021)",
        "tema": "Recomendações da CPI da Barragem de Brumadinho (item 2.6 do voto do relator – BGE 2019)",
        "texto": "Observar as recomendações estatuídas no relatório elaborado pela Comissão Parlamentar de Inquérito "
                 "da Assembleia Legislativa do Estado de Minas Gerais referente à CPI da Barragem de Brumadinho "
                 "constantes no item 2.6 do voto do Relator.",
        "visao": "Parcialmente Atendida",
        "direcionamento_csv": "Recomendar envio para SUGER",
        "paginas": "BGE 2025, p. 706-708 · BGE 2024, p. 607",
        "demanda": [
            "O TCEMG acompanha recomendações da CPI de Brumadinho. As que seguem pendentes são: (VIII) envolver "
            "o Centro Mineiro de Referência em Resíduos (CMRR) em alternativas à disposição de rejeitos em "
            "barragens; (XIII) realizar estudo longitudinal da saúde física e mental dos trabalhadores "
            "sobreviventes e das populações atingidas.",
            "No BGE 2025 (p. 706-707), a Cfamge registrou que não houve comprovação da retomada das atividades "
            "do CMRR e que o Relatório Técnico da SEF de 2026 não trouxe informação sobre o tema. Sobre o "
            "estudo longitudinal, citou o subprojeto 37 do Projeto Brumadinho UFMG e os estudos de avaliação "
            "de risco à saúde humana. Manteve o item como Parcialmente Atendido.",
        ],
        "fundamento": [
            ART69,
            "O tema é a reparação do desastre de Brumadinho. A execução das recomendações envolve FEAM/CMRR, SES "
            "e o Comitê Pró-Brumadinho. A NT 38/2024 transcreveu resposta do Comitê Pró-Brumadinho (Memo "
            "SEPLAG/RAM-CB nº 42/2024). O OF SPLOR 13/2025, o Memo 198/2025 e a NT 21/2026 indicaram a SUGER.",
        ],
        "destino": "SUGER (com articulação com FEAM/CMRR e SES)",
        "apoio": "Sem participação da SPLOR.",
    },
    {
        "ref": "R20 (2019)",
        "tema": "Piso Salarial Profissional Nacional do magistério (PSPN)",
        "texto": "Observar o Piso Salarial Profissional Nacional (PSPN) na rede estadual de Minas Gerais, em "
                 "consonância com os preceitos normativos da Lei Nacional 11.738/2008, da Lei Estadual 21.710/15 e "
                 "do artigo 201-A e respectivos parágrafos da Constituição Estadual.",
        "visao": "Parcialmente Atendida",
        "direcionamento_csv": "Recomendar envio para SUGESP",
        "paginas": "Relatório Cfamge de monitoramento (SEI 128518367), citado no Memo SPLOR 198/2025. Não "
                   "localizado nos relatórios anuais do repositório.",
        "demanda": [
            "O TCEMG quer evidências de que o vencimento inicial das carreiras do magistério da educação básica "
            "observa o piso nacional (Lei 11.738/2008), considerada a proporcionalidade da jornada, e de que a "
            "legislação estadual correlata é cumprida.",
            "Informações já disponíveis no acervo: a NT 38/2024 (D45/2020) transcreveu a evolução do vencimento "
            "inicial do PEB frente ao piso até 2024. O Memo SPLOR 133/2026 cita os reajustes do magistério para "
            "adequação ao piso: 12,84% pela Lei 24.383/2023 e 5,26% pela Lei 25.245/2025. Cita também a revisão "
            "geral de 5,4% pela Lei 25.804/2026.",
        ],
        "fundamento": [
            "Decreto 48.636/2023, art. 77: compete à SUGESP 'planejar e coordenar a formulação, execução e "
            "avaliação, em nível central, da política de recursos humanos', inclusive a 'administração e "
            "pagamento de pessoal'. A política remuneratória do magistério é dessa área, com a SEE.",
            "Histórico: o Memo SPLOR 198/2025 encaminhou o item à SUGESP. Na NT 38/2024, o item correlato (D45/2020) "
            "foi respondido pela AEI/SEPLAG.",
        ],
        "destino": "SUGESP (com a SEE)",
        "apoio": "Sem participação da SPLOR. Se útil, pode-se indicar à SUGESP os dados já citados no Memo 133/2026.",
    },
    {
        "ref": "R1 (2020) · D17 (2021) · D1 (2022)",
        "tema": "Aprimoramento do PMDI (novos indicadores e revisão de metas)",
        "texto": "Proceda ao aprimoramento do Plano Mineiro de Desenvolvimento Integrado – PMDI atual, com a devida "
                 "inclusão de novos indicadores e revisão de metas que possibilitem mensurar a evolução das "
                 "políticas públicas de forma mais abrangente.",
        "visao": "Não Atendida",
        "direcionamento_csv": "Recomendar envio para SUGER",
        "paginas": "BGE 2025, p. 699 · Defesa 2025, item C1 (indicadores do Proeb/Simave)",
        "demanda": [
            "O TCEMG pede a revisão do PMDI 2019-2030, com novos indicadores e metas revistas. No BGE 2025 "
            "(p. 699), registrou que a revisão não foi iniciada e que a última atualização ocorreu pela Lei "
            "23.577/2020. A SEF informou que as diretrizes e metas continuam válidas porque não houve troca de "
            "governo em 2023.",
            "Na abertura de vista do BGE 2025 (item C1), o TCE também perguntou sobre a revisão do PMDI. O "
            "motivo foi a mudança na metodologia das avaliações educacionais (Proeb, atual Simave), que deixou "
            "sem resultados os indicadores 16 e 17 em 2025.",
        ],
        "fundamento": [
            ART69 + " A elaboração e revisão do PMDI estão expressamente no inciso I.",
            "Histórico: o item foi encaminhado à área de gestão estratégica pelos Memos SPLOR 109/2024 e "
            "127/2024, pelo Memo SPLOR 50/2025 e pelo Memo SPLOR 198/2025. Na NT 21/2026, a SPLOR indicou a "
            "SUGER, tanto no D17 quanto no C1.",
        ],
        "destino": "SUGER",
        "apoio": "Sem participação da SPLOR. A elaboração do PPAG 2028-2031, em 2027, pode ser oportunidade de "
                 "alinhamento PMDI × PPAG, a critério da SUGER.",
    },
    {
        "ref": "D28 (2021)",
        "tema": "Baixo comprometimento com o planejamento das ações de Projetos Estratégicos",
        "texto": "Atentar para o baixo comprometimento com o planejamento das ações de Projetos Estratégicos.",
        "visao": "Não Atendida",
        "direcionamento_csv": "Recomendar envio para SUGER",
        "paginas": "BGE 2025, p. 703-704",
        "demanda": [
            "O TCEMG acompanha a qualidade do planejamento físico e orçamentário dos Projetos Estratégicos "
            "pelo Índice de Avaliação do Planejamento (IAP). O índice evoluiu de 17,99 (2019) para 36,05 "
            "(2024), o que levou a Cfamge a considerar o item atendido no BGE 2024. Em 2025, caiu para 28,03, "
            "abaixo do de 2021 (30,38), e o item voltou a Não Atendido (BGE 2025, p. 704).",
            "Para as demais ações, que não têm monitoramento diferenciado, o IAP foi de 50,88 em 2024 (eficácia "
            "'Razoável'), acima do dos Projetos Estratégicos.",
        ],
        "fundamento": [
            ART69,
            "Na abertura de vista de 2021 (Ofício SEPLAG/SCGAE nº 103/2022, citado no BGE 2025), a resposta foi da "
            "Subsecretaria de Gestão Estratégica. Na NT 21/2026 (D28, C10, R45 e R47-ii), a SPLOR indicou a "
            "SUGER. A SUGER respondeu ao TCE pelo Memo SEPLAG/SCGAE nº 20/2026 (Defesa 2025, p. 80-82).",
        ],
        "destino": "SUGER",
        "apoio": "A SPLOR pode subsidiar com dados de programação e execução. No PLOA 2027 há 17 ações de Projeto "
                 "Estratégico com dotação simbólica (até R$ 1 mil), contra 7 na LOA 2025. Isso afeta o IAP e "
                 "dialoga com a R40/2022, respondida pela SPLOR.",
    },
    {
        "ref": "R34 (2022)",
        "tema": "Legalidade da execução da ação 4554 – Construção e Adequação de Rodovias – Reparação Brumadinho",
        "texto": "Apure, por meio da unidade de Controle Interno competente, a legalidade da execução da despesa na "
                 "ação 4554 – Construção e Adequação de Rodovias – Reparação Brumadinho, bem como de sua "
                 "liquidação e pagamento, e monitore se o cronograma de desembolso financeiro da obra contratada "
                 "está compatível com a programação orçamentária.",
        "visao": "Sem posicionamento do TCE sobre o Parecer de 2022",
        "direcionamento_csv": "Recomendar envio para SUGER",
        "paginas": "Análise da defesa do BGE 2022, p. 64 (origem) · BGE 2023, p. 560-568",
        "demanda": [
            "Origem: em 2022, foram empenhados R$ 53,715 milhões na ação 4554 com a Fonte 95 (Acordo Vale), mas "
            "apenas R$ 1,490 milhão foi liquidado e pago. Desse total, R$ 50 milhões foram empenhados para uma "
            "única empresa (Emconbras), no contrato DC-022/2022 do DER-MG (melhoramento da MG-060, trecho "
            "Papagaios–Pompéu). A Cfamge considerou a explicação 'parcialmente suficiente' (análise da defesa "
            "do BGE 2022, p. 64).",
            "O TCEMG quer que o controle interno competente apure a legalidade da execução, da liquidação e do "
            "pagamento. Quer também que o Estado acompanhe a compatibilidade entre o cronograma físico-financeiro "
            "da obra e a programação orçamentária.",
        ],
        "fundamento": [
            ART69,
            "A apuração de legalidade cabe ao controle interno: a Controladoria Setorial do DER-MG e a CGE. O "
            "acompanhamento do cronograma cabe ao DER-MG, executor do contrato, e à SUGER, gestora dos recursos da "
            "Fonte 95. O OF SPLOR 13/2025 encaminhou o item à área de gestão estratégica (Memo SPLOR 50/2025).",
        ],
        "destino": "SUGER, com envolvimento do DER-MG e da CGE/Controladoria Setorial",
        "apoio": "Sem participação da SPLOR.",
    },
    {
        "ref": "R46 (2025)",
        "tema": "Projetos Estratégicos com dotação compatível com o custo e sem janelas orçamentárias",
        "texto": "As ações classificadas como Projetos Estratégicos sejam incluídas na programação orçamentária anual "
                 "com dotação inicial compatível com o custo estimado de sua execução e com fontes de financiamento "
                 "minimamente asseguradas, evitando-se a utilização de janelas orçamentárias e a dependência de "
                 "captação futura e incerta de recursos externos, de modo a garantir a viabilidade de execução do "
                 "objeto ao longo do exercício e reduzir o risco de iniciativas estratégicas permanecerem sem "
                 "execução por fatores alheios ao controle do Estado.",
        "visao": "Proposta mantida pela Cfamge (pendente do Pleno)",
        "direcionamento_csv": "Recomendar envio para SUGER",
        "paginas": "Defesa 2025, p. 80-82 · BGE 2025, p. 38-42 (origem)",
        "demanda": [
            "O TCEMG observa que os Projetos Estratégicos são as prioridades da LDO 2025 (art. 2º). Mesmo assim, "
            "várias dessas ações tiveram dotação simbólica (janela) ou dependeram de captação externa incerta e "
            "terminaram o exercício sem execução.",
            "Na defesa (Memo SEPLAG/SCGAE nº 20/2026), o Estado explicou que algumas iniciativas dependem de "
            "recursos externos (emendas, convênios) ou não têm execução orçamentária (renúncia fiscal). A "
            "Cfamge manteve a recomendação. Excetuou as ações não orçamentárias, como a Ação 1081 – Invista em "
            "Minas, mas pediu dotação inicial compatível e fontes minimamente asseguradas para as demais.",
        ],
        "fundamento": [
            ART69 + " A definição da carteira e das diretrizes dos Projetos Estratégicos é da SUGER.",
            "A SUGER participa da definição dos valores anuais dos Projetos Estratégicos na elaboração da LOA. "
            "Cabe a ela, portanto, avaliar por que determinadas ações estratégicas foram orçadas por meio de "
            "janela orçamentária e se há condições de prever dotação compatível com o custo estimado.",
            "Na NT 21/2026, a SPLOR indicou a SUGER (R45 e R46), e a SUGER respondeu pelo Memo SEPLAG/SCGAE nº "
            "20/2026.",
        ],
        "destino": "SUGER",
        "apoio": "Sem participação direta da SPLOR. Como subsídio, pode-se informar à SUGER que o PLOA 2027 tem 17 "
                 "ações com IAG de Projeto Estratégico com dotação de até R$ 1 mil (7 na LOA 2025). A lista está "
                 "em entregas/demanda-01/analises/janelas_PLOA_2027.csv.",
    },
]
