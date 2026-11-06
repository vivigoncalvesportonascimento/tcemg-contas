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
        "ref": "R28 (2020)",
        "tema": "Notas explicativas no RGF sobre medidas de recondução da despesa com pessoal",
        "texto": "Recomendar que inclua notas explicativas nos RGF para informar as medidas corretivas, adotadas ou "
                 "a adotar, de recondução ao limite de despesa com pessoal, visando conferir maior transparência "
                 "em relação à situação fiscal do Poder ou órgão, tanto à sociedade como aos Tribunais de Contas, "
                 "que têm a atribuição de fiscalizar o cumprimento da LRF.",
        "visao": "Não Atendida",
        "direcionamento_csv": "Verificar antes de responder se deve ser recomendado a SUGESP/SEPLAG e SEF",
        "paginas": "BGE 2025, p. 712 (R13/2021) · BGE 2024, p. 620",
        "demanda": [
            "O TCEMG quer que o Relatório de Gestão Fiscal (RGF) traga notas explicativas com as medidas "
            "corretivas, adotadas ou a adotar, para reconduzir a despesa com pessoal ao limite.",
            "No BGE 2024 (p. 620), a SEF/SCAF informou que o RGF publica apenas a trajetória de retorno ao "
            "limite, não as medidas corretivas. Comprometeu-se a inserir as notas e ressalvou que as medidas são "
            "de competência da SEPLAG e do Governo. No BGE 2025 (p. 712), a CGE registrou que, ao longo de 2026, "
            "SEF e SEPLAG promoveriam os ajustes para incluir as notas. A Cfamge manteve o item como Não "
            "Atendido.",
            "Constatação no repositório: no RGF do 2º quadrimestre de 2026, a DTP do Executivo foi de 47,36% da "
            "RCL, acima do limite prudencial de 46,55%, e o campo 'Medidas Corretivas' continua em branco.",
        ],
        "fundamento": [
            "Competência compartilhada, sem atribuição da SPLOR. A elaboração e a publicação do RGF são da "
            "SEF/STE. A definição e o acompanhamento das medidas de contenção da despesa com pessoal são da "
            "SUGESP: Decreto 48.636/2023, art. 77, compete à SUGESP 'planejar e coordenar a formulação, execução "
            "e avaliação, em nível central, da política de recursos humanos', inclusive a 'administração e "
            "pagamento de pessoal'.",
            "Histórico: o Memo SPLOR 200/2025 (BGE 2024 – C12) remeteu à SUGESP o pedido de informar as medidas "
            "corretivas, conforme o Memo SPLOR 82/2025 (09/07/2025, item C12 do Relatório Técnico Preliminar do BGE 2024), "
            "que recomendou a resposta pela SUGESP, já em cópia no processo SEI. O OF SPLOR 13/2025 e o Memo SPLOR 198/2025 indicaram "
            "tratar-se de matéria de competência da SEF. A própria SEF declarou ao TCE que as medidas são da "
            "SEPLAG, o que reforça a necessidade de fluxo conjunto SUGESP–SEF.",
        ],
        "destino": "SUGESP/SEPLAG e SEF",
        "apoio": "Dessa forma, a SPLOR recomenda que a SUGESP/SEPLAG se manifeste sobre as medidas corretivas "
                 "adotadas ou previstas no âmbito da gestão de pessoas e que a SEF informe os procedimentos para "
                 "inclusão dessas informações nas notas explicativas do RGF. A SPLOR poderá fornecer, quando "
                 "necessário, subsídios relativos às projeções orçamentárias da despesa de pessoal e ao "
                 "acompanhamento dos limites fiscais.",
    },
    {
        "ref": "R30 (2020) · R11 (2021)",
        "tema": "Limites de despesa com pessoal e vedações do art. 22 da LRF",
        "texto": "Observar com rigor os limites máximos de gastos com pessoal, atentando para as vedações "
                 "estabelecidas no parágrafo único do art. 22 da Lei de Responsabilidade Fiscal, caso extrapolado "
                 "o limite prudencial, ressaltando-se, todavia, que a vedação prevista no inciso I do mencionado "
                 "dispositivo legal não alcança o pagamento e a atualização anual do piso nacional do magistério, "
                 "assegurados pela Lei nº 11.738, de 2008.",
        "visao": "Não Atendida",
        "direcionamento_csv": "Responder (a SPLOR entende que a competência é da SUGESP)",
        "paginas": "BGE 2025, p. 712 · Defesa 2025, p. 19 (medidas de pessoal)",
        "demanda": [
            "O TCEMG quer que o Poder Executivo observe os limites de despesa com pessoal e as vedações do "
            "parágrafo único do art. 22 da LRF enquanto estiver acima do limite prudencial, ressalvados o "
            "pagamento e a atualização do piso nacional do magistério.",
            "No BGE 2025 (p. 712), a Cfamge ratificou o não atendimento porque o Poder Executivo continuou acima "
            "do limite prudencial durante 2025. No RGF do 2º quadrimestre de 2026, a DTP do Executivo foi de "
            "R$ 55,757 bilhões, ou 47,36% da RCL ajustada (limite prudencial de 46,55% e máximo de 49,00%). Na "
            "defesa do BGE 2025 (p. 19), o Estado listou as medidas de contenção adotadas.",
        ],
        "fundamento": [
            "Razões similares às do item R28/2020: a observância das vedações do art. 22 da LRF (reajustes, "
            "nomeações, criação de cargos, horas extras etc.) decorre da política de gestão de pessoas, de "
            "competência da SUGESP (Decreto 48.636/2023, art. 77).",
            "Histórico: o OF SPLOR 13/2025 indicou a SUGESP para o R30, e a NT 21/2026 indicou a SUGESP para o "
            "R11. O R11 foi respondido pela AEI/SEPLAG na NT 38/2024. A SPLOR já prestou informações "
            "orçamentárias sobre a DTP nos Memos SPLOR 64/2026 e 133/2026 (alertas do TCE).",
        ],
        "destino": "SUGESP",
        "apoio": "A SPLOR poderá fornecer, quando necessário, subsídios relativos às projeções orçamentárias da "
                 "despesa de pessoal e ao acompanhamento dos limites fiscais (DTP/RCL), com base nos Memos SPLOR "
                 "64/2026 e 133/2026.",
    },
    {
        "ref": "R12 (2021)",
        "tema": "Redução estrutural das despesas com pessoal",
        "texto": "Manter-se pertinaz nos esforços para redução das despesas com pessoal, adotando medidas "
                 "estruturantes, com vistas ao equilíbrio dos dispêndios dessa natureza.",
        "visao": "Não Atendida",
        "direcionamento_csv": "Responder (a SPLOR entende que a competência é da SUGESP)",
        "paginas": "BGE 2025, p. 712 · Defesa 2025, p. 19",
        "demanda": [
            "O TCEMG quer que o Estado mantenha esforços para reduzir a despesa com pessoal, com medidas "
            "estruturantes que levem ao equilíbrio desse gasto.",
            "No BGE 2025 (p. 712), a Cfamge registrou que a CGE considerou a recomendação implementada, diante "
            "das medidas de contenção informadas pela SEPLAG. A Cfamge, porém, ratificou o não atendimento: a "
            "despesa com pessoal segue crescendo e o Executivo continuou acima do limite prudencial.",
        ],
        "fundamento": [
            "Razões similares às dos itens R28/2020 e R30/2020 · R11/2021: medidas estruturantes de redução da "
            "despesa com pessoal decorrem da política de gestão de pessoas, de competência da SUGESP "
            "(Decreto 48.636/2023, art. 77).",
            "Histórico: a NT 21/2026 indicou a SUGESP para o R12, e a NT 38/2024 transcreveu a resposta da "
            "AEI/SEPLAG. Nos Memos SPLOR 133/2026 e 135/2026, a SPLOR informou a trajetória da DTP/RCL e sugeriu "
            "o encaminhamento à SUGESP e à SEF.",
        ],
        "destino": "SUGESP",
        "apoio": "A SPLOR poderá fornecer, quando necessário, subsídios relativos às projeções orçamentárias da "
                 "despesa de pessoal (no PLOA 2027, aumento de R$ 2,572 bilhões no Executivo, associado ao "
                 "crescimento vegetativo) e ao acompanhamento dos limites fiscais.",
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
