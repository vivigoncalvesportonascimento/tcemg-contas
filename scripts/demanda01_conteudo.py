"""Conteúdo da Demanda 01 – Ofício SEF/STE nº 288/2026 (monitoramento TCEMG, 1º ciclo de 2026).

Cada item corresponde a uma linha do quadro
data/demandas-resposta/oficio_sef_288_2026_quadro_recomendacoes_determinacoes.csv
cujo direcionamento SPLOR é "Responder" (ou variantes "Verificar..."/"Responder, mas verificar...").

Siglas das fontes (páginas = numeração impressa nos relatórios do TCEMG):
  BGE 2025   – data/analise-contas/2025_tcemg_analise_contas.pdf (Relatório sobre a Macrogestão, exercício 2025)
  Defesa 2025 – data/analise-contas/2025_tcemg_analise_defesa_estado.pdf (Análise da defesa, exercício 2025)
  BGE 2024 / BGE 2023 – data/analise-contas/2024_... e 2023_tcemg_analise_contas.pdf
"""

PRAZO = "12/11/2026"

ITENS = [
    # ------------------------------------------------------------------ 1
    {
        "ref": "D2 (2019) · R13 (2020) · DEA5 (2021)",
        "tema": "IPU exclusivos para emendas impositivas",
        "origem": "Parecer Prévio", "anos": "2019, 2020, 2021",
        "texto": "Criar Identificadores de Procedência e Uso – IPU exclusivos para emendas impositivas, "
                 "segregando-os em emendas individuais, de blocos e de bancadas.",
        "visao_tce": "Não Atendida", "direcionamento": "Responder",
        "paginas": "BGE 2025, p. 715 · BGE 2024, p. 624-625",
        "resumo": [
            "O TCEMG pede que a execução das emendas parlamentares estaduais impositivas possa ser identificada "
            "por tipo (individual, de bloco e de bancada) já no IPU. Hoje o IPU tem um único dígito (0 a 9), "
            "todas as posições estão em uso e as emendas estaduais são identificadas genericamente pelo IPU 8.",
            "No BGE 2025 (p. 715), a Cfamge manteve a determinação como Não Atendida. A Cfamge reconheceu as "
            "melhorias no Portal de Emendas, mas registrou que a solução depende do GRP-Minas e ainda não foi "
            "implantada. A Cfamge já havia oficiado o Estado pedindo cronograma independente do GRP. No BGE "
            "2024 (p. 624), registrou a proposta da SPLOR (Memo SEPLAG/SPLOR nº 14/2025) de distinguir os tipos "
            "de emenda pela variável 'Unidade de Programação do Gasto – UPG', em discussão com a SEGOV.",
        ],
        "competencia": "Competência da SPLOR: a definição do IPU integra o Classificador Econômico da Despesa, "
                       "sob a DCPPN (art. 39 do Decreto 48.636/2023). A gestão das emendas impositivas cabe à "
                       "SEGOV, e o sistema (GRP-Minas) é coordenado pela SEF. A resposta deve ser da SPLOR, "
                       "citando SEGOV e SEF como parceiras. Atenção: no OF SPLOR 13/2025, a SPLOR encaminhou à "
                       "SEGOV o item correlato R7/2022 (indicador contábil de emendas). Convém manter coerência.",
        "respostas": [
            ("Memo SEPLAG/SPLOR nº 195/2025", "19/12/2025", "Sem novidade",
             "Reiterou a NT 38/2024: não há capacidade operacional para novos IPUs no sistema atual. Com o "
             "GRP-Minas, o IPU ganhará um dígito adicional, o que permitirá códigos específicos por tipo de "
             "emenda."),
            ("Nota Técnica SEPLAG/SPLOR nº 38/2024", "11/10/2024", "Em tratamento",
             "Informou que as 10 variações do IPU já estão em uso. As emendas federais passaram a ser "
             "segregadas por novas fontes de recursos em 2023 (01, 02, 03, 04, 07, 08, 62 a 65). As emendas "
             "estaduais (IPU 8) dependem do GRP-Minas."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "A limitação estrutural do Siafi-MG permanece: o IPU tem apenas uma posição, com os dez códigos "
            "possíveis (0 a 9) já em uso. A solução definitiva está vinculada ao GRP-Minas, cuja entrada em "
            "operação está prevista para janeiro de 2027. Os órgãos e entidades já estão sendo treinados no "
            "módulo de Programação Orçamentária, que a SEPLAG desenvolve com a SEF. No GRP, o IPU passará a "
            "ter um dígito adicional, o que permitirá criar identificadores próprios para emendas individuais, "
            "de bloco e de bancada.",
            "Até a implantação, a SPLOR mantém, em articulação com a SEGOV, a identificação do tipo de emenda "
            "pela Unidade de Programação do Gasto (UPG), consultável no Armazém de Informações – Siafi, e a "
            "divulgação no Portal de Emendas.",
            "Plano de ação: (1) definir no Classificador Econômico da Despesa 2027 a nova estrutura do IPU, com "
            "códigos específicos para emendas individuais, de bloco e de bancada. Responsável: SPLOR/DCPPN. "
            "Prazo: até a carga da LOA 2027 no GRP-Minas (1º trimestre de 2027). (2) Validar a parametrização "
            "no GRP com a SEF. Prazo: janeiro de 2027. (3) Comunicar à Cfamge a implantação, com evidências "
            "(classificador publicado e consulta de execução por tipo de emenda). Prazo: até 30/04/2027.",
        ],
        "atencao": [
            "Confirmar com a SEF/equipe GRP se o IPU de dois dígitos já está parametrizado e se a LOA 2027 será "
            "carregada com os novos códigos.",
            "Confirmar com a SEGOV se a UPG foi de fato adotada na execução de 2026 (o TCE registrou apenas que "
            "estava 'em discussão').",
            "O TCE critica a dependência reiterada do GRP. Prazos firmes reduzem o risco de nova avaliação "
            "'Não Atendida'.",
        ],
    },
    # ------------------------------------------------------------------ 2
    {
        "ref": "R29 (2019)",
        "tema": "Discrepância entre programação e execução orçamentárias",
        "origem": "Parecer Prévio", "anos": "2019",
        "texto": "Atentar para a discrepância verificada entre a programação e a execução orçamentárias.",
        "visao_tce": "Parcialmente Atendida", "direcionamento": "Responder",
        "paginas": "BGE 2025, p. 700 (D21/2021) e p. 708-709 (D39 e D47/2021) · BGE 2024, p. 613",
        "resumo": [
            "A recomendação tem o mesmo objeto da D39/2021 e da D21/2021: aderência entre o planejado (LOA/PPAG) "
            "e o executado. O TCEMG mede essa aderência pelo Índice de Avaliação do Planejamento (IAP).",
            "No BGE 2025 (p. 700), a Cfamge registrou a evolução do IAP consolidado de 43,13 (2021) para 50,57 "
            "(2025), ainda no grau de eficácia 'Razoável'. Considerou o item parcialmente atendido e apontou "
            "áreas temáticas com eficácia reiteradamente 'Baixa'. Na p. 708-709, propôs que D39 e D47 sejam "
            "monitoradas dentro da D21, para racionalizar o rol de deliberações.",
        ],
        "competencia": "Competência da SPLOR: elaboração, monitoramento e avaliação do planejamento e do "
                       "orçamento (arts. 35, 37 e 39 do Decreto 48.636/2023).",
        "respostas": [
            ("Nota Técnica SEPLAG/SPLOR nº 21/2026 (D21 e D39/2021)", "19/06/2026", "Atendida",
             "Informou a evolução do IAP, que chegou a 51,04% em 2025 (43,13% em 2021), como evidência do "
             "aperfeiçoamento do planejamento. Para a D39, remeteu à D21."),
            ("Nota Técnica SEPLAG/SPLOR nº 38/2024 (D39/2021)", "11/10/2024", "Atendida",
             "Comparou crédito inicial e despesa empenhada. Excluída a fonte 20 (mudança de metodologia das "
             "transferências a municípios), a execução de 2022 ficou 1,19% acima do planejado. Em 2023, ficou "
             "0,68% abaixo."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento (aprimoramento contínuo).",
            "O Estado mantém trajetória consistente de melhoria da aderência entre programação e execução. O "
            "Índice de Avaliação do Planejamento (IAP) consolidado passou de 43,13 em 2021 para 50,57 em 2025, "
            "conforme apurado pela própria Cfamge. A SEPLAG acompanha ainda, no PPAG 2024-2027, o indicador "
            "'Sucesso do Planejamento Orçamentário' (Programa 0157), que mede a despesa liquidada em relação ao "
            "crédito autorizado e atingiu 89,96% em 2024 [atualizar 2025].",
            "Os desvios entre o planejado e o executado são monitorados e justificados bimestralmente no "
            "Sigplan e divulgados nos Relatórios Institucionais de Monitoramento. O Orçamento Base Zero está "
            "aplicado em todos os órgãos. Com a implantação do GRP-Minas em 2027, o módulo de Programação "
            "Orçamentária integrará a programação e a execução numa mesma base.",
            "Considerando a proposta da própria Cfamge (BGE 2025, p. 708-709), solicita-se que esta "
            "recomendação (R29/2019) seja monitorada em conjunto com as deliberações D21, D39 e D47/2021, que "
            "têm o mesmo objeto.",
        ],
        "atencao": [
            "Harmonizar o valor do IAP 2025: a NT 21/2026 informou 51,04%, e o TCE apurou 50,57. Usar o valor do "
            "TCE ou explicar a diferença.",
            "Atualizar o indicador 'Sucesso do Planejamento Orçamentário' para 2025 (dado não disponível no "
            "repositório).",
        ],
    },
    # ------------------------------------------------------------------ 3
    {
        "ref": "R3 (2020)",
        "tema": "Alinhamento do PPAG à Agenda 2030 (ODS)",
        "origem": "Parecer Prévio", "anos": "2020",
        "texto": "Recomendar que aprimore o alinhamento do PPAG à Agenda 2030, além da vinculação dos programas aos "
                 "ODS relacionados, explicitando se o programa tem potencial de contribuição direta ou indireta "
                 "para os ODS e suas metas.",
        "visao_tce": "Parcialmente Atendida", "direcionamento": "Responder",
        "paginas": "BGE 2023, p. 586 · BGE 2025, p. 699-700 (D18/2021, mesmo tema)",
        "resumo": [
            "O TCEMG reconhece que todos os programas finalísticos do PPAG estão vinculados a ao menos um ODS "
            "desde 2017. Falta, porém, explicitar a natureza da contribuição (direta ou indireta) e monitorar "
            "as metas.",
            "No BGE 2025 (p. 699-700), a Cfamge observou que o painel de monitoramento da FJP "
            "(shiny.fjp.mg.gov.br/ODS) está indisponível desde 2024. As iniciativas relatadas (capacitações, "
            "Sapp-MG, painel Power BI em desenvolvimento) 'ainda não se traduziram em mecanismos efetivos e "
            "permanentes de monitoramento e avaliação'.",
        ],
        "competencia": "Competência da SPLOR: normas e metodologias de elaboração, revisão e monitoramento do "
                       "PPAG (art. 39, I e III, do Decreto 48.636/2023).",
        "respostas": [
            ("Memo SEPLAG/SPLOR nº 198/2025 (R3 e D6/2020)", "22/12/2025", "Atendida (D6)",
             "Descreveu a vinculação aos ODS desde 2017, o Sapp-MG (Decreto 48.298/2021), o Relatório de "
             "Percurso da FJP, as oficinas de 2022 e 2024, o benchmarking e o painel em Power BI 'em fase de "
             "estruturação'. Atenção: classificou a D6 como 'Atendida', embora o texto informe que o painel "
             "não estava concluído."),
            ("Ofício SEPLAG/SPLOR nº 13/2025", "19/05/2025", "Em tratamento",
             "Mesmos fundamentos: vinculação aos ODS, Sapp-MG, Relatório FJP, capacitações (6º Ciclo de "
             "Assessoramento – Mapa de Indicadores) e PL 335/2019 na ALMG."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "Desde a revisão de 2017, todos os programas finalísticos do PPAG estão vinculados a pelo menos um "
            "dos 17 ODS, o que se mantém obrigatório no PPAG 2024-2027. Para avançar no alinhamento e explicitar "
            "a natureza da contribuição dos programas, a SEPLAG, em parceria com a Fundação João Pinheiro, está "
            "desenvolvendo um painel interativo de indicadores. O painel relaciona programas e ações do PPAG às "
            "metas dos ODS, com base em microdados oficiais (IBGE e FJPdados), e tem implantação prevista para "
            "31/03/2027. A ferramenta substituirá o painel anterior da FJP, hoje indisponível.",
            "Complementarmente, propõe-se incluir na metodologia de elaboração do PPAG 2028-2031, cuja "
            "elaboração ocorrerá em 2027, a indicação, por programa, das metas ODS relacionadas e do tipo de "
            "contribuição (direta ou indireta). Isso atende ao núcleo da recomendação.",
            "Plano de ação: (1) concluir e publicar o painel PPAG × metas ODS (SPLOR/DCPPN e FJP, até "
            "31/03/2027); (2) incluir na metodologia do PPAG 2028-2031 o campo 'contribuição direta/indireta "
            "às metas ODS' (SPLOR/DCPPN, no Manual de Elaboração do PPAG, 2º trimestre de 2027); (3) comunicar "
            "à Cfamge a implantação, com o link público do painel.",
        ],
        "atencao": [
            "Não repetir o status 'Atendida' usado no Memo 198/2025 para a D6: o próprio texto reconhecia que o "
            "painel não estava concluído, e o TCE mantém 'Parcialmente Atendida'.",
            "Validar com a DCPPN a proposta do campo 'contribuição direta/indireta' no PPAG 2028-2031 antes de "
            "assumir o compromisso.",
            "Verificar a situação atual do PL 335/2019 na ALMG, se for citado.",
        ],
    },
    # ------------------------------------------------------------------ 4
    {
        "ref": "R10 (2020)",
        "tema": "Controles internos por sistema (decretos de créditos)",
        "origem": "Parecer Prévio", "anos": "2020",
        "texto": "Recomendar o aprimoramento dos controles internos do estado, por meio de sistema, para que sejam "
                 "realizados de forma que reflitam o que dispõem a norma e o ato jurídico exarado pelo estado.",
        "visao_tce": "Parcialmente Atendida", "direcionamento": "Responder",
        "paginas": "BGE 2023, p. 591 · BGE 2024, p. 616 (R1/2021, mesmo objeto)",
        "resumo": [
            "A recomendação nasceu de divergências, no BGE 2020, entre o que os decretos de abertura de "
            "créditos adicionais dispunham (tipo de crédito, fonte e origem dos recursos) e o registro no "
            "Siafi-MG.",
            "Nos BGE 2023 (p. 591) e 2024 (p. 616), a Cfamge manteve o item como Parcialmente Atendido. A "
            "Cfamge registrou que a SEPLAG aprimorou os controles para mitigar erros formais, mas que persiste a "
            "impossibilidade sistêmica de registrar como créditos suplementares as suplementações de dotações "
            "criadas por crédito especial. A correção depende de alteração no Siafi/Armazém, prevista para o "
            "GRP-Minas.",
        ],
        "competencia": "Competência da SPLOR quanto aos decretos de alteração orçamentária e às regras de "
                       "programação (art. 37, III e VI, do Decreto 48.636/2023). A sustentação e as regras do "
                       "Siafi/GRP são da SEF, que deve ser citada como corresponsável pela solução sistêmica.",
        "respostas": [
            ("Nota Técnica SEPLAG/SPLOR nº 38/2024 (R1/2021, mesmo objeto)", "11/10/2024", "Atendida",
             "Informou que os decretos orçamentários passaram a trazer, no art. 2º, fonte de recurso, origem e "
             "valor, mesmo quando há uma única fonte e origem."),
            ("Manifestação SEPLAG no RCI 2023 (citada no BGE 2023/2024)", "2024", "Em tratamento",
             "Aprimoramento dos controles para evitar erros formais nas suplementações. A limitação do Siafi "
             "para registrar a suplementação de crédito especial será tratada no GRP-Minas."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "A SPLOR adotou controles para que os atos reflitam fielmente o que é registrado. Desde 2024, o "
            "art. 2º dos decretos de alteração orçamentária explicita fonte de recurso, origem e valor, mesmo "
            "quando há uma só fonte e uma só origem. Os decretos são conferidos previamente pela DCPPN contra "
            "os registros do Siafi-MG.",
            "Resta a limitação sistêmica, já reconhecida pela Cfamge: o Siafi-MG não registra como crédito "
            "suplementar a suplementação de dotação criada por crédito especial. A solução foi incorporada ao "
            "escopo do GRP-Minas, cuja entrada em operação está prevista para janeiro de 2027. Nele, o tipo de "
            "crédito e a origem dos recursos serão registrados conforme o ato normativo.",
            "Plano de ação: (1) validar com a SEF, na parametrização do GRP, as regras de registro por tipo de "
            "crédito (SPLOR/DCPPN e SEF/SCCG, janeiro de 2027); (2) manter a conferência prévia decreto × "
            "sistema (DCPPN, contínuo); (3) informar à Cfamge, após o 1º quadrimestre de 2027, o resultado do "
            "registro no novo sistema.",
        ],
        "atencao": [
            "Esta recomendação e a R1/2021 têm o mesmo objeto. Sugere-se pedir ao TCE monitoramento conjunto.",
            "Confirmar com a equipe GRP se a regra de crédito especial/suplementar está no escopo da entrada em "
            "janeiro de 2027.",
        ],
    },
    # ------------------------------------------------------------------ 5
    {
        "ref": "R28 (2020)",
        "tema": "Notas explicativas no RGF sobre medidas de recondução da despesa com pessoal",
        "origem": "Parecer Prévio", "anos": "2020",
        "texto": "Recomendar que inclua notas explicativas nos RGF para informar as medidas corretivas, adotadas ou "
                 "a adotar, de recondução ao limite de despesa com pessoal, visando conferir maior transparência "
                 "em relação à situação fiscal do Poder ou órgão, tanto à sociedade como aos Tribunais de Contas, "
                 "que têm a atribuição de fiscalizar o cumprimento da LRF.",
        "visao_tce": "Não Atendida",
        "direcionamento": "Verificar antes de responder se deve ser recomendado a SUGESP/SEPLAG e SEF",
        "paginas": "BGE 2025, p. 712 (R13/2021) · BGE 2024, p. 620",
        "resumo": [
            "No BGE 2024 (p. 620), a SEF/SCAF informou que o RGF publica apenas a trajetória de retorno ao "
            "limite, não as medidas corretivas. Comprometeu-se a inserir as notas e ressalvou que as medidas são "
            "de competência da SEPLAG e do Governo.",
            "No BGE 2025 (p. 712), a CGE registrou que, ao longo de 2026, SEF e SEPLAG promoveriam os ajustes "
            "para incluir as notas. A Cfamge manteve o item como Não Atendido.",
            "Constatação no repositório: no RGF do 2º quadrimestre de 2026, a DTP do Executivo foi de 47,36% da "
            "RCL, acima do limite prudencial de 46,55%, e o campo 'MEDIDAS CORRETIVAS' continua em branco.",
        ],
        "competencia": "Competência compartilhada. A elaboração e publicação do RGF são da SEF/STE (o "
                       "demonstrativo é emitido pela SEF/STE/SCCG). A definição das medidas de contenção da "
                       "despesa de pessoal é da SUGESP/SEPLAG (art. 77 do Decreto 48.636/2023). A SPLOR "
                       "contribui no monitoramento de indicadores fiscais (art. 37, IV). Recomenda-se responder "
                       "informando o fluxo conjunto e encaminhar à SUGESP e à SEF para complementação.",
        "respostas": [
            ("Memo SEPLAG/SPLOR nº 198/2025", "22/12/2025", "Não informado",
             "'Matéria de competência da SEF.'"),
            ("Ofício SEPLAG/SPLOR nº 13/2025", "19/05/2025", "Não informado",
             "'Demanda deve ser respondida pela Secretaria de Estado de Fazenda.'"),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento (atuação conjunta SEF e SEPLAG).",
            "A elaboração e a publicação do Relatório de Gestão Fiscal competem à Secretaria de Estado de "
            "Fazenda. A SEPLAG, por meio da Subsecretaria de Gestão de Pessoas, é responsável pela definição e "
            "pelo acompanhamento das medidas de contenção da despesa com pessoal do Poder Executivo.",
            "Para atender à recomendação, a SEPLAG encaminhará à SEF, a cada quadrimestre, a relação das "
            "medidas adotadas e a adotar para a recondução ao limite. Essa relação será inserida no campo "
            "'Medidas Corretivas' do Anexo 1 do RGF. Entre as medidas: concessão de reajustes restrita às "
            "hipóteses do parágrafo único do art. 22 da LRF; nomeações em cargos comissionados criteriosas; "
            "criação de cargos efetivos apenas com extinção de equivalentes; análise prévia de concursos e "
            "nomeações quanto à LRF; monitoramento do crescimento vegetativo da folha. Essas medidas já foram "
            "informadas ao TCE na defesa do BGE 2025 (Análise da defesa, p. 19).",
            "Plano de ação: (1) SUGESP elabora o texto das medidas corretivas (até 15/01/2027); (2) SEF insere a "
            "nota no RGF do 3º quadrimestre de 2026, publicado até 30/01/2027; (3) rotina quadrimestral a "
            "partir de então. Responsáveis: SEPLAG/SUGESP e SEF/STE.",
        ],
        "atencao": [
            "Encaminhar à SUGESP e à SEF antes do envio: o prazo e o fluxo propostos dependem de ambas.",
            "Evitar resposta apenas 'competência da SEF': a própria SEF já declarou ao TCE que as medidas são da "
            "SEPLAG. Sem um fluxo conjunto, o item continuará Não Atendido.",
        ],
    },
    # ------------------------------------------------------------------ 6
    {
        "ref": "R30 (2020) · R11 (2021)",
        "tema": "Limites de despesa com pessoal e vedações do art. 22 da LRF",
        "origem": "Parecer Prévio", "anos": "2020, 2021",
        "texto": "Observar com rigor os limites máximos de gastos com pessoal, atentando para as vedações "
                 "estabelecidas no parágrafo único do art. 22 da Lei de Responsabilidade Fiscal, caso extrapolado "
                 "o limite prudencial, ressaltando-se, todavia, que a vedação prevista no inciso I do mencionado "
                 "dispositivo legal não alcança o pagamento e a atualização anual do piso nacional do magistério, "
                 "assegurados pela Lei nº 11.738, de 2008.",
        "visao_tce": "Não Atendida", "direcionamento": "Responder",
        "paginas": "BGE 2025, p. 712 · Defesa 2025, p. 19 (medidas de pessoal)",
        "resumo": [
            "No BGE 2025 (p. 712), a Cfamge ratificou o não atendimento porque o Poder Executivo continuou acima "
            "do limite prudencial da LRF durante 2025.",
            "No RGF do 2º quadrimestre de 2026, a DTP do Executivo foi de R$ 55,757 bilhões, ou 47,36% da RCL "
            "ajustada. O limite prudencial é 46,55% e o máximo, 49,00%. Na defesa do BGE 2025 (p. 19), o Estado "
            "listou as medidas de contenção adotadas.",
        ],
        "competencia": "A observância das vedações do art. 22 da LRF (reajustes, nomeações, horas extras etc.) é "
                       "da SUGESP (art. 77 do Decreto 48.636/2023). A SPLOR contribui pela programação "
                       "orçamentária, pelo monitoramento dos indicadores fiscais (art. 37, IV) e pelo apoio ao "
                       "COFIN. O CSV indica 'Responder'. Sugere-se resposta da SPLOR sobre a parcela "
                       "orçamentária, complementada pela SUGESP.",
        "respostas": [
            ("Nota Técnica SEPLAG/SPLOR nº 21/2026 (R11/2021)", "19/06/2026", "Não informado",
             "'A manifestação acerca do pagamento do piso nacional do magistério é de competência da SUGESP.'"),
            ("Ofício SEPLAG/SPLOR nº 13/2025 (R30/2020)", "19/05/2025", "Não informado",
             "'Demanda deve ser respondida pela Subsecretaria de Gestão de Pessoas.' Antes disso, a NT 38/2024 "
             "transcreveu a AEI/SEPLAG: 'Atendida', sem reajustes em 2021."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "Enquanto a despesa com pessoal permanecer acima do limite prudencial (47,36% da RCL no 2º "
            "quadrimestre de 2026), o Poder Executivo observa as vedações do parágrafo único do art. 22 da LRF. "
            "Todas as proposições com impacto na folha passam por análise técnica prévia da SEPLAG quanto à "
            "compatibilidade com a LRF, preservadas as exceções legais, como o pagamento e a atualização do "
            "piso nacional do magistério (Lei 11.738/2008).",
            "No âmbito orçamentário, a SPLOR: (i) dimensiona a despesa de pessoal na LOA com base no "
            "crescimento vegetativo, sem incorporar reajustes não autorizados; (ii) monitora quadrimestralmente "
            "o indicador DTP/RCL e subsidia o COFIN nas decisões de programação orçamentária e financeira; (iii) "
            "condiciona a liberação de cotas de pessoal à compatibilidade com os limites. As medidas de gestão "
            "de pessoal são detalhadas pela SUGESP [inserir complemento da SUGESP].",
        ],
        "atencao": [
            "Encaminhar à SUGESP para complementar com as medidas de 2026 (reajustes concedidos, nomeações, "
            "piso do magistério).",
            "Confirmar os itens (ii) e (iii) da parcela orçamentária com a SCPO/DCPPN antes de enviar.",
        ],
    },
    # ------------------------------------------------------------------ 7
    {
        "ref": "R1 (2021)",
        "tema": "Aprimoramento dos controles internos (sistema ou planilha)",
        "origem": "Parecer Prévio", "anos": "2021",
        "texto": "Aprimorar os controles internos, seja por meio de sistema, seja via planilha Excel, para que sejam "
                 "realizados de forma que reflitam o que dispõem a norma e o ato jurídico praticado.",
        "visao_tce": "Parcialmente Atendida",
        "direcionamento": "Responder, mas verificar se esbarra em competência da SPLOR/SEPLAG",
        "paginas": "BGE 2024, p. 616 · BGE 2023, p. 591",
        "resumo": [
            "Desdobramento da R10/2020. O TCEMG admite controle por sistema ou por planilha, para que os "
            "registros de créditos adicionais reflitam o ato normativo (tipo de crédito, fonte, origem e "
            "valor).",
            "No BGE 2024 (p. 616), a Cfamge manteve o item como Parcialmente Atendido: houve melhoria nos "
            "controles formais, mas persiste a limitação sistêmica de registro das suplementações de crédito "
            "especial, a ser resolvida no GRP-Minas.",
        ],
        "competencia": "Competência da SPLOR quanto aos decretos de alteração orçamentária e seus controles "
                       "(art. 37, III e VI, Decreto 48.636/2023). A alteração do Siafi/GRP é da SEF. Não há "
                       "impedimento de competência para a SPLOR responder; basta citar a SEF na parte "
                       "sistêmica.",
        "respostas": [
            ("Nota Técnica SEPLAG/SPLOR nº 38/2024", "11/10/2024", "Atendido",
             "Os decretos passaram a explicitar, no art. 2º, fonte de recurso, origem e valor, mesmo com uma "
             "única fonte e origem, cumprindo o disposto na norma e no ato praticado."),
            ("Manifestação SEPLAG no RCI 2023 (citada no BGE 2024, p. 616)", "2024", "Em tratamento",
             "Controles aprimorados para mitigar erros formais. A limitação do Siafi para crédito especial será "
             "solucionada no GRP-Minas."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "Reitera-se a resposta à R10/2020, que tem o mesmo objeto. Como controle complementar e transitório "
            "até o GRP-Minas, a DCPPN mantém controle em planilha com o registro de cada decreto de alteração "
            "orçamentária: tipo de crédito, fonte, origem e valor. Esse controle permite conciliar o ato "
            "publicado com o registro no Siafi-MG e identificar suplementações de dotações criadas por crédito "
            "especial [confirmar existência e formato do controle com a DCPPN]. Com o GRP-Minas (janeiro de "
            "2027), o registro passará a refletir diretamente o tipo de crédito e a origem previstos no ato.",
            "Solicita-se monitoramento conjunto com a R10/2020.",
        ],
        "atencao": [
            "A existência do controle em planilha precisa ser confirmada pela DCPPN. Se não existir, retirar o "
            "parágrafo ou criar o controle antes do envio, pois é uma solução simples e a própria recomendação "
            "o admite.",
        ],
    },
    # ------------------------------------------------------------------ 8
    {
        "ref": "R12 (2021)",
        "tema": "Redução estrutural das despesas com pessoal",
        "origem": "Parecer Prévio", "anos": "2021",
        "texto": "Manter-se pertinaz nos esforços para redução das despesas com pessoal, adotando medidas "
                 "estruturantes, com vistas ao equilíbrio dos dispêndios dessa natureza.",
        "visao_tce": "Não Atendida", "direcionamento": "Responder",
        "paginas": "BGE 2025, p. 712 · Defesa 2025, p. 19",
        "resumo": [
            "No BGE 2025 (p. 712), a Cfamge registrou que a CGE considerou a recomendação implementada, diante "
            "das medidas de contenção informadas pela SEPLAG. A Cfamge, porém, ratificou o não atendimento: a "
            "despesa com pessoal segue crescendo e o Executivo continuou acima do limite prudencial.",
            "Segundo o Relatório de Transição da SPLOR, o PLOA 2027 projeta aumento de R$ 2,572 bilhões na "
            "despesa de pessoal do Executivo, associado ao crescimento vegetativo da folha. Essa despesa "
            "representa 47,2% da despesa total, excluídas as intraorçamentárias.",
        ],
        "competencia": "Competência principal da SUGESP (política de recursos humanos e pagamento de pessoal, "
                       "art. 77 do Decreto 48.636/2023). A SPLOR responde pela parcela orçamentária e pelo "
                       "monitoramento fiscal (art. 37, IV).",
        "respostas": [
            ("Nota Técnica SEPLAG/SPLOR nº 21/2026", "19/06/2026", "Não informado",
             "'A manifestação acerca das medidas adotadas com vistas à redução do percentual de despesas de "
             "pessoal é de competência da SUGESP.'"),
            ("Nota Técnica SEPLAG/SPLOR nº 38/2024 (transcrição AEI/SEPLAG)", "11/10/2024", "Atendida",
             "Informou o cumprimento das vedações da LRF, a ausência de reajustes em 2021 e as restrições a "
             "concursos, nomeações e contratações temporárias."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "O equilíbrio da despesa com pessoal é perseguido com medidas de contenção e estruturantes, "
            "coordenadas pela SEPLAG: análise prévia de impacto de todas as proposições com efeito na folha; "
            "criação de cargos condicionada à extinção de equivalentes; critérios para nomeações; monitoramento "
            "do crescimento vegetativo. No orçamento, a SPLOR projeta a despesa de pessoal no PLOA 2027 "
            "considerando apenas o crescimento vegetativo, sem incorporação de reajustes não autorizados.",
            "Há também os efeitos fiscais esperados do Programa de Pleno Pagamento de Dívidas dos Estados "
            "(Propag), que ampliam a margem fiscal do Estado [confirmar com a SEF o enquadramento a ser citado]. "
            "As medidas estruturantes de gestão de pessoas serão detalhadas pela SUGESP [inserir complemento].",
        ],
        "atencao": [
            "Responder em conjunto com o item R30/R11 e encaminhar à SUGESP para complementar.",
            "Avaliar se convém citar o Propag. Validar com a SEF.",
        ],
    },
    # ------------------------------------------------------------------ 9
    {
        "ref": "D18 (2021)",
        "tema": "Implementação da Agenda 2030",
        "origem": "Parecer Prévio", "anos": "2021",
        "texto": "Envidar esforços para a implementação da Agenda 2030, tornando possível, assim, alcançar as metas "
                 "nela previstas.",
        "visao_tce": "Não Atendida (Ofício) / Parcialmente Atendida (BGE 2025)", "direcionamento": "Responder",
        "paginas": "BGE 2025, p. 699-700",
        "resumo": [
            "No BGE 2025 (p. 699-700), a Cfamge classificou o item como Parcialmente Atendido, divergindo do "
            "'Não Atendida' que consta do Ofício 288. Reconheceu a vinculação dos programas aos ODS, o Sapp-MG, "
            "o Relatório de Percurso da FJP e o painel em Power BI em desenvolvimento. Concluiu que essas "
            "iniciativas ainda não formam um mecanismo efetivo e permanente de monitoramento das metas. O link "
            "do painel da FJP segue indisponível.",
        ],
        "competencia": "Competência da SPLOR: planejamento e monitoramento do PPAG (art. 39 do Decreto "
                       "48.636/2023). A articulação de políticas com metas ODS envolve os órgãos setoriais e a "
                       "FJP.",
        "respostas": [
            ("Nota Técnica SEPLAG/SPLOR nº 21/2026", "19/06/2026", "Em tratamento",
             "Destacou o painel interativo em desenvolvimento, as capacitações e a conferência sobre a Agenda "
             "2030 sediada em Minas Gerais em 2026."),
            ("Memo SEPLAG/SPLOR nº 198/2025", "22/12/2025", "Em tratamento",
             "Benchmarking da União e de outros estados. Priorização de painel em Power BI com microdados do "
             "IBGE e da FJPdados, por objetivo, indicador, órgão, programa e território."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "A SEPLAG, em parceria com a Fundação João Pinheiro, está concluindo o painel interativo que "
            "relaciona programas e ações do PPAG às metas dos ODS, com implantação prevista para 31/03/2027. O "
            "painel permitirá acompanhar periodicamente a evolução dos indicadores das metas e o alinhamento dos "
            "programas estaduais, de forma pública. Ele constituirá o mecanismo permanente de monitoramento "
            "apontado pela Cfamge.",
            "Somam-se a isso: a vinculação obrigatória de todos os programas finalísticos aos ODS desde 2017; o "
            "Sistema Estadual de Monitoramento e Avaliação de Políticas Públicas (Sapp-MG, Decreto "
            "48.298/2021); as capacitações periódicas de gestores; a realização em Minas Gerais, em 2026, de "
            "conferência sobre a Agenda 2030.",
            "Solicita-se considerar o tratamento conjunto com a R3/2020 e a D6/2020.",
        ],
        "atencao": [
            "Registrar a divergência de status: o Ofício traz 'Não Atendida', e o BGE 2025 traz 'Parcialmente "
            "Atendida'.",
            "Se o painel tiver versão preliminar publicada, incluir o link como evidência.",
        ],
    },
    # ------------------------------------------------------------------ 10
    {
        "ref": "D22 (2021)",
        "tema": "Demonstrativo dos 50 municípios com pior IMRS",
        "origem": "Parecer Prévio", "anos": "2021",
        "texto": "Evidenciar, no demonstrativo relativo aos Municípios classificados nas cinquenta últimas posições "
                 "do IMRS, projetos que possam efetivamente contribuir para o desenvolvimento dos Municípios mais "
                 "carentes do Estado e reduzir as desigualdades regionais.",
        "visao_tce": "Parcialmente Atendida", "direcionamento": "Responder",
        "paginas": "BGE 2025, p. 700-702 · BGE 2025, p. 68-73 (análise do demonstrativo)",
        "resumo": [
            "A Cfamge reconheceu como aprimoramento relevante a exclusão, a partir da LOA 2025, das UOs 1915 e "
            "1916 e das funções 28 e 99 do demonstrativo. Ainda assim, apontou duas fragilidades (BGE 2025, "
            "p. 701-702):",
            "Primeira: a inclusão do Programa 162 (Desenvolvimento e Gestão de Pessoas da Rede Estadual de "
            "Ensino, R$ 441,46 milhões), por se tratar de despesa obrigatória de pessoal. Segunda: a ausência de "
            "valores por município, o que impede validar a metodologia de proporcionalização populacional. "
            "Recomendou revisão anual criteriosa dos programas que compõem o demonstrativo.",
        ],
        "competencia": "Competência da SPLOR: elaboração da LOA e de seus demonstrativos exigidos pela LDO "
                       "(art. 37, II, e art. 39, II e IV, do Decreto 48.636/2023).",
        "respostas": [
            ("Nota Técnica SEPLAG/SPLOR nº 21/2026 (D22 e C3)", "19/06/2026", "Em tratamento",
             "Comprometeu-se a aperfeiçoar, já na LOA 2027, a seleção dos programas, priorizando os de impacto "
             "mais direto e evitando despesas de relação apenas indireta. Também avaliaria explicitar a "
             "metodologia de proporcionalização populacional e as estimativas por município."),
            ("Nota Técnica SEPLAG/SPLOR nº 38/2024", "11/10/2024", "Atendida",
             "Explicou a proporcionalização populacional dos localizadores genéricos e a retirada, a partir de "
             "2025, das UOs 1915/1916 e das funções 28 e 99. Defendeu a manutenção de proventos de inativos."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "Em cumprimento ao compromisso assumido na defesa do BGE 2025, o demonstrativo que acompanha o PLOA "
            "2027 foi aperfeiçoado [descrever as mudanças efetivamente feitas no PLOA 2027, por exemplo: "
            "exclusão de programas de remuneração de pessoal como o Programa 162; inclusão de nota "
            "metodológica sobre a proporcionalização populacional; anexo com estimativas por município].",
            "Os critérios do demonstrativo passam a ser: (1) despesas municipalizadas nos 50 municípios; (2) "
            "despesas em localizadores genéricos, proporcionalizadas pela população (estimativas oficiais do "
            "IBGE); (3) exclusão das UOs 1915 e 1916, das funções 28 e 99 e dos programas de natureza "
            "predominantemente administrativa ou de remuneração de pessoal [confirmar]. A seleção será revista "
            "anualmente, como recomendado pela Cfamge.",
        ],
        "atencao": [
            "Item dependente de informação: verificar no PLOA 2027 (enviado à ALMG em 30/09/2026) o que mudou no "
            "demonstrativo do IMRS. O texto entre colchetes deve refletir apenas o que foi feito.",
            "Se o PLOA 2027 manteve o Programa 162, a resposta deve explicar o motivo ou programar a exclusão "
            "para a LOA 2028.",
        ],
    },
    # ------------------------------------------------------------------ 11
    {
        "ref": "D33 (2021)",
        "tema": "Concentração de gastos em atividades-meio e operações especiais",
        "origem": "Parecer Prévio", "anos": "2021",
        "texto": "Envidar esforços para adotar medidas necessárias visando a diminuir a concentração de gastos com "
                 "atividades-meio e com operações especiais, de forma a combater o déficit orçamentário e liberar "
                 "orçamento para ações finalísticas.",
        "visao_tce": "Não Atendida", "direcionamento": "Responder",
        "paginas": "BGE 2025, p. 705 · BGE 2024, p. 606",
        "resumo": [
            "No BGE 2024 (p. 606), a Cfamge considerou a determinação atendida: a participação de "
            "atividades-meio e operações especiais caiu de 66,90% (2021) para 58,60% (2024), graças à "
            "apropriação da despesa de pessoal nas ações finalísticas.",
            "No BGE 2025 (p. 705), reverteu para Não Atendida. Em 2025, o Estado criou a Ação 2417 – "
            "Remuneração de Pessoal Ativo e Encargos Sociais (Programa 705, atividade-meio), com R$ 12,585 "
            "bilhões fixados, e a participação voltou a 66,49%. O tema é o mesmo da proposta D42/2025.",
        ],
        "competencia": "Competência da SPLOR: estrutura programática da LOA e apropriação orçamentária (arts. "
                       "37 e 39 do Decreto 48.636/2023), com dependência do sistema de folha (SUGESP) e do "
                       "GRP-Minas (SEF).",
        "respostas": [
            ("Nota Técnica SEPLAG/SPLOR nº 21/2026", "19/06/2026", "Em tratamento",
             "Atribuiu o retrocesso à ação padronizada 2417, transitória por exigência da implantação do novo "
             "sistema de pessoal no GRP. Sem a 2417, a concentração em atividades-meio seria 7,67% do crédito "
             "inicial e 2,33% da despesa realizada, em vez de 45,08% e 39,71%. A apropriação seria "
             "restabelecida após a implantação do GRP."),
            ("Nota Técnica SEPLAG/SPLOR nº 38/2024", "11/10/2024", "Não tratado",
             "Não abordou a D33 (o item foi incluído no monitoramento posteriormente)."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "Entre 2021 e 2024, o Estado reduziu a participação das atividades-meio e operações especiais de "
            "66,90% para 58,60%, como reconheceu a Cfamge no BGE 2024. O aumento verificado em 2025 decorre "
            "exclusivamente de mudança na forma de apropriação da despesa de pessoal (Ação 2417), adotada de "
            "forma transitória para a migração da folha ao GRP-Minas. Não houve realocação efetiva de recursos "
            "das áreas finalísticas para as administrativas.",
            "A apropriação da despesa de pessoal nas ações em que os servidores atuam será restabelecida "
            "[informar se no PLOA 2027 ou em data definida, conforme decisão da SPLOR/SUGESP], após a "
            "estabilização do GRP-Minas, prevista para 2027. Até lá, a SPLOR publicará [proposta] a distribuição "
            "gerencial da despesa da Ação 2417 por programa e ação, com base na lotação dos servidores, no "
            "Relatório Institucional de Monitoramento e na Avaliação Anual do PPAG. Assim fica preservada a "
            "informação de custos exigida pelo art. 50, § 3º, da LRF. Ver também a resposta à D42/2025.",
        ],
        "atencao": [
            "Decisão necessária: o PLOA 2027 manteve a Ação 2417? A data de restabelecimento precisa ser "
            "definida e informada, pois o TCE (Defesa 2025, p. 76) rejeitou justificativa sem prazo.",
            "A proposta de publicar o rateio gerencial responde à crítica do TCE de que não foram apresentadas "
            "medidas alternativas na transição. Validar a viabilidade com a SUGESP.",
        ],
    },
    # ------------------------------------------------------------------ 12
    {
        "ref": "D39 (2021)",
        "tema": "Discrepância entre programação e execução orçamentárias",
        "origem": "Parecer Prévio", "anos": "2021",
        "texto": "Atentar para a discrepância verificada entre a programação e a execução orçamentárias.",
        "visao_tce": "Parcialmente Atendida", "direcionamento": "Responder",
        "paginas": "BGE 2025, p. 708-709 · BGE 2024, p. 613",
        "resumo": [
            "No BGE 2025 (p. 708-709), a Cfamge remeteu à análise da D21/2021, Parcialmente Atendida pela "
            "melhoria gradativa do IAP: 43,13 em 2021 e 50,57 em 2025. Sugeriu que o objeto passe a ser "
            "monitorado no âmbito da D21. O mesmo entendimento consta do BGE 2024 (p. 613).",
        ],
        "competencia": "Competência da SPLOR (arts. 35, 37 e 39 do Decreto 48.636/2023).",
        "respostas": [
            ("Nota Técnica SEPLAG/SPLOR nº 21/2026", "19/06/2026", "Remete à D21 (Atendida)",
             "'Vide justificativa apresentada na D21': evolução do IAP para 51,04% em 2025."),
            ("Nota Técnica SEPLAG/SPLOR nº 38/2024", "11/10/2024", "Atendida",
             "Variação entre crédito inicial e empenho de +1,19% em 2022 (excluída a fonte 20) e de −0,68% em "
             "2023."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "Reitera-se a resposta apresentada para a R29/2019, de mesmo objeto. Concorda-se com a proposta da "
            "Cfamge (BGE 2025, p. 708-709) de monitorar esta determinação no âmbito da D21/2021, com base na "
            "evolução do IAP: 43,13 em 2021 e 50,57 em 2025.",
        ],
        "atencao": ["Mesmas observações da R29/2019 (harmonizar o IAP 2025)."],
    },
    # ------------------------------------------------------------------ 13
    {
        "ref": "R1 (2022)",
        "tema": "Equilíbrio fiscal e orçamentário nos projetos de LOA",
        "origem": "Parecer Prévio", "anos": "2022",
        "texto": "Busque o equilíbrio fiscal e orçamentário nos projetos de Lei Orçamentária Anual – LOA que venham "
                 "a ser apresentados.",
        "visao_tce": "— (sem posicionamento do TCE sobre o Parecer 2022)", "direcionamento": "Responder",
        "paginas": "Sem página: o TCEMG ainda não se posicionou sobre o Parecer Prévio de 2022 (Ofício 288)",
        "resumo": [
            "A recomendação pede que o Executivo envie projetos de LOA equilibrados. Desde 2015, as LOAs mineiras "
            "são aprovadas com déficit previsto. Segundo o Relatório de Transição da SPLOR, entre 2019 e 2025 o "
            "déficit previsto variou de R$ 3,6 bilhões (2023) a R$ 16,2 bilhões (2021). O resultado apurado, "
            "porém, foi sempre melhor que o previsto, com superávits de 2021 a 2025.",
            "O PLOA 2027 projeta receita de R$ 144,999 bilhões, despesa de R$ 155,502 bilhões e déficit de "
            "R$ 10,503 bilhões.",
        ],
        "competencia": "Competência da SPLOR: elaboração e consolidação do projeto de LOA e monitoramento dos "
                       "indicadores fiscais (art. 37, II e IV, do Decreto 48.636/2023). As metas fiscais (LDO) e "
                       "a dívida têm participação da SEF.",
        "respostas": [
            ("Memo SEPLAG/SPLOR nº 198/2025", "22/12/2025", "Em tratamento",
             "O déficit na LOA decorre dos princípios da transparência e da prudência (MCASP), diante do déficit "
             "estrutural desde 2013. O déficit projetado vem caindo ao longo dos anos."),
            ("Ofício SEPLAG/SPLOR nº 13/2025", "19/05/2025", "Em tratamento",
             "Esforços de equilíbrio, especialmente pelas tratativas de adesão ao Propag, com transparência e "
             "prudência nas estimativas."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "Desde 2015, o Executivo elabora a LOA com estimativas realistas de receita e despesa, pelos "
            "princípios da transparência e da prudência (MCASP) e diante da elevada rigidez da despesa. Isso "
            "evidencia déficits que, de outro modo, ficariam ocultos por superestimativa de receitas.",
            "A gestão fiscal tem produzido resultados superiores aos previstos. As LOAs de 2019 a 2025 foram "
            "aprovadas com déficit previsto, mas houve superávits orçamentários de R$ 103,7 milhões (2021), "
            "R$ 2,2 bilhões (2022), R$ 299,4 milhões (2023), R$ 5,2 bilhões (2024) e R$ 1,1 bilhão (2025). Em "
            "2019 e 2020, os déficits efetivos (R$ 8,6 e R$ 2,9 bilhões) ficaram bem abaixo dos previstos.",
            "O PLOA 2027 prevê receita de R$ 144,999 bilhões e despesa de R$ 155,502 bilhões, com déficit de "
            "R$ 10,503 bilhões. Isso decorre principalmente do crescimento vegetativo da folha (+R$ 2,572 "
            "bilhões), da elevação das despesas constitucionais (+R$ 908 milhões), das amortizações da dívida "
            "(+R$ 1,417 bilhão) e das despesas dos demais Poderes (+R$ 2,421 bilhões). O equilíbrio segue como "
            "objetivo, apoiado na adesão ao Propag e na programação orçamentária e financeira com "
            "contingenciamento via COFIN.",
        ],
        "atencao": [
            "Confirmar os números do PLOA 2027 com o texto final enviado à ALMG (fonte: Relatório de Transição "
            "SPLOR de 28/10/2026).",
            "O déficit de 2027 (R$ 10,5 bi) é maior que o de 2026. Convém explicar a variação.",
        ],
    },
    # ------------------------------------------------------------------ 14
    {
        "ref": "R6 (2022)",
        "tema": "Programas com execução inferior a 50%",
        "origem": "Parecer Prévio", "anos": "2022",
        "texto": "Realize um planejamento mais assertivo ou pelo menos esclareça fatores que conduziram a 16% dos "
                 "programas terem execução inferior a 50%, de acordo com dados do Siafi.",
        "visao_tce": "— (sem posicionamento do TCE sobre o Parecer 2022)", "direcionamento": "Responder",
        "paginas": "Sem página: Parecer 2022 sem posicionamento do TCEMG",
        "resumo": [
            "No BGE 2022, 16% dos programas tiveram execução inferior a 50% do crédito. A SPLOR informou 15% em "
            "2024 (OF 13/2025). Os fatores recorrentes são as fontes de convênios e acordos, que têm fluxo "
            "próprio de arrecadação, e as janelas orçamentárias.",
        ],
        "competencia": "Competência da SPLOR: monitoramento e avaliação do PPAG/LOA (art. 39, III, do Decreto "
                       "48.636/2023).",
        "respostas": [
            ("Memo SEPLAG/SPLOR nº 198/2025", "22/12/2025", "Em tratamento",
             "O desempenho inferior a 50% decorreu, sobretudo, de fatores exógenos e limitações operacionais. "
             "Intensificação do monitoramento das metas físicas e orçamentárias."),
            ("Ofício SEPLAG/SPLOR nº 13/2025", "19/05/2025", "Em tratamento",
             "Janelas orçamentárias evitadas quando possível. Convênios e acordos seguem como desafio. 15% dos "
             "programas abaixo de 50% em 2024."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "Em 2025, [X]% dos programas tiveram execução inferior a 50% do crédito autorizado, contra 16% em "
            "2022 e 15% em 2024 [apurar no Armazém Siafi]. Os principais fatores são: (i) programas financiados "
            "por convênios, acordos e operações de crédito, cuja execução depende do ingresso dos recursos e do "
            "andamento de licitações e obras; (ii) dotações abertas por superávit financeiro no fim do exercício; "
            "(iii) contingenciamentos determinados pelo COFIN conforme a disponibilidade financeira.",
            "As justificativas por ação são registradas bimestralmente no Sigplan e analisadas pela SEPLAG, que "
            "orienta os órgãos a qualificá-las. A partir de 2027, a integração entre programação e execução no "
            "GRP-Minas deve permitir o realinhamento mais tempestivo de dotações.",
        ],
        "atencao": [
            "Base de dados necessária: execução orçamentária 2025 por programa (crédito autorizado × empenhado), "
            "do Armazém Siafi, para calcular o percentual e listar os programas.",
        ],
    },
    # ------------------------------------------------------------------ 15
    {
        "ref": "R40 (2022)",
        "tema": "Janelas orçamentárias",
        "origem": "Parecer Prévio", "anos": "2022",
        "texto": "Evite a utilização de dotações orçamentárias com valores inferiores aos custos de implementação da "
                 "respectiva ação governamental, as chamadas 'janelas orçamentárias'.",
        "visao_tce": "— (sem posicionamento do TCE sobre o Parecer 2022)", "direcionamento": "Responder",
        "paginas": "Parecer 2022 sem posicionamento · tema correlato: Defesa 2025, p. 80-82 (R46) e BGE 2025, p. 38-42",
        "resumo": [
            "Janelas orçamentárias são dotações simbólicas (em geral, R$ 1 mil) abertas na LOA para receber "
            "suplementações. Na análise do BGE 2025 (Defesa 2025, p. 80-82), a Cfamge aceitou o uso para "
            "receitas incertas, mas o criticou em ações prioritárias (Projetos Estratégicos). Daí a proposta "
            "R46/2025, direcionada à SUGER.",
        ],
        "competencia": "Competência da SPLOR: elaboração da LOA e normas de programação (arts. 37 e 39 do "
                       "Decreto 48.636/2023).",
        "respostas": [
            ("Memo SEPLAG/SPLOR nº 198/2025", "22/12/2025", "Em tratamento",
             "Mecanismo essencial para receitas de previsão incerta (convênios, emendas, superávit). "
             "Suplementar dotação existente é mais ágil que abrir crédito especial. Esforço para minimizar o "
             "uso, como nos precatórios (ação 7004)."),
            ("Ofício SEPLAG/SPLOR nº 13/2025", "19/05/2025", "Em tratamento",
             "Mesma linha: finalidade estratégica, uso criterioso e excepcional, e a estimativa de receitas na "
             "LDO feita em maio do ano anterior."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "O Executivo restringe as janelas orçamentárias às ações financiadas por receitas cujo ingresso não "
            "pode ser estimado com segurança na elaboração da LOA: convênios, emendas parlamentares federais, "
            "doações, operações de crédito em contratação e superávit financeiro. Nesses casos, a dotação "
            "simbólica preserva a especificidade da ação e a rastreabilidade da execução, evitando a criação "
            "posterior de créditos especiais.",
            "No PLOA 2027, [N] ações foram programadas com dotação simbólica, contra [N] na LOA 2026 [apurar]. "
            "Para ações de recursos ordinários e Projetos Estratégicos, a orientação da SPLOR é programar dotação "
            "compatível com o custo estimado.",
        ],
        "atencao": [
            "Base de dados necessária: quantidade de ações com dotação inicial de R$ 1 mil na LOA 2026 e no PLOA "
            "2027, por fonte, para dar evidência objetiva.",
            "Alinhar com a resposta da SUGER à R46/2025 (Projetos Estratégicos) para não haver contradição.",
        ],
    },
    # ------------------------------------------------------------------ 16
    {
        "ref": "D42 (2025)",
        "tema": "Apropriação da despesa de pessoal nos programas finalísticos (Ação 2417)",
        "origem": "Relatório da Análise (proposta)", "anos": "2025",
        "texto": "Determinar ao Poder Executivo Estadual o restabelecimento da apropriação das despesas com Pessoal e "
                 "Encargos Sociais nos programas e ações orçamentárias em que os servidores efetivamente "
                 "desempenham suas atividades, em conformidade com disposto no art. 50, § 3º, da LC 101/2000, "
                 "cessando a utilização de ação ou programa padronizado para a centralização dessas despesas.",
        "visao_tce": "Proposta mantida pela Cfamge (pendente do Pleno)", "direcionamento": "Responder",
        "paginas": "Defesa 2025, p. 76 · BGE 2025, p. 179 e 235 (origem) · BGE 2025, p. 705 (D33)",
        "resumo": [
            "Em 2025, a despesa de pessoal do Executivo foi centralizada na Ação 2417 – Remuneração de Pessoal "
            "Ativo e Encargos Sociais, com R$ 12,585 bilhões fixados (BGE 2025, p. 235). Isso interrompeu a "
            "apropriação descentralizada praticada desde 2020 por recomendação do próprio TCE.",
            "Na análise da defesa (p. 76), a Cfamge manteve a determinação. A justificativa do GRP não demonstrou "
            "a impossibilidade concreta de manter a sistemática anterior, nem apresentou medidas alternativas "
            "para a transição. A apropriação descentralizada já era feita nos sistemas anteriores, sob as mesmas "
            "limitações.",
        ],
        "competencia": "Competência da SPLOR (estrutura programática e alocação na LOA, arts. 37 e 39 do "
                       "Decreto 48.636/2023), em conjunto com a SUGESP (sistema de folha) e a SEF (GRP-Minas e "
                       "sistema de custos).",
        "respostas": [
            ("Nota Técnica SEPLAG/SPLOR nº 21/2026 (D42)", "19/06/2026", "Não informado",
             "A alteração decorreu da compatibilização com o novo sistema de pessoal no GRP. A apropriação "
             "seria restabelecida 'tão logo o GRP esteja implantado e testado, e considerando a viabilidade do "
             "sistema'."),
            ("Nota Técnica SEPLAG/SPLOR nº 21/2026 (D33)", "19/06/2026", "Em tratamento",
             "Caráter transitório, sem mudança na destinação efetiva dos recursos. Indicadores recalculados "
             "sem a 2417."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "A centralização da despesa de pessoal na Ação 2417, em 2025, decorreu da migração da folha de "
            "pagamento para o novo sistema de pessoal integrado ao GRP-Minas. Nesse período, a folha passou a "
            "ser processada [descrever o motivo técnico concreto, por exemplo: sem o vínculo de cada servidor a "
            "uma funcional programática, exigido pela integração automática com a execução orçamentária]. "
            "Essa é a razão pela qual a sistemática anterior não pôde ser mantida.",
            "O restabelecimento da apropriação nos programas e ações em que os servidores atuam está programado "
            "para [LOA 2027 / LOA 2028 – definir], após a estabilização do GRP-Minas, cuja entrada em operação "
            "está prevista para janeiro de 2027.",
            "Como medida alternativa durante a transição, a SEPLAG publicará [proposta] a distribuição gerencial "
            "da despesa da Ação 2417 por programa e ação do PPAG, com base na lotação dos servidores, nos "
            "Relatórios Institucionais de Monitoramento e na Avaliação Anual do PPAG. Assim fica assegurada a "
            "avaliação de custos prevista no art. 50, § 3º, da LRF.",
            "Plano de ação: (1) definir a data de restabelecimento (SPLOR e SUGESP, até 31/12/2026); (2) "
            "publicar o rateio gerencial de 2025 e 2026 (SPLOR/DCPPN, até 31/03/2027); (3) parametrizar no GRP "
            "o vínculo servidor × ação (SUGESP e SEF, 2027).",
        ],
        "atencao": [
            "Ponto mais sensível desta demanda: o TCE já rejeitou justificativa genérica (Defesa 2025, p. 76). "
            "Sem a explicação técnica concreta e sem prazo, a determinação tende a ser aprovada pelo Pleno e "
            "avaliada como não atendida.",
            "Verificar se o PLOA 2027 manteve a Ação 2417. Se a manteve, o restabelecimento ficará, no mínimo, "
            "para a LOA 2028.",
            "Validar com a SUGESP e a SEF a viabilidade do rateio gerencial antes de assumir o compromisso.",
        ],
    },
    # ------------------------------------------------------------------ 17
    {
        "ref": "D44 (2025)",
        "tema": "Destinação da TFAMG (Fonte 52) exclusivamente a SEMAD, FEAM e IEF",
        "origem": "Relatório da Análise (proposta)", "anos": "2025",
        "texto": "Determinar que os recursos arrecadados a título de TFAMG sejam utilizados exclusivamente pela "
                 "SEMAD, pela FEAM e pelo IEF, em estrita observância à destinação estabelecida na legislação de "
                 "regência, em especial na Lei nº 14.940/2003, e no Decreto nº 44.045/2005.",
        "visao_tce": "Proposta mantida pela Cfamge (pendente do Pleno)", "direcionamento": "Responder",
        "paginas": "Defesa 2025, p. 77-79 · BGE 2025, p. 622-623 (origem)",
        "resumo": [
            "Em 2025, recursos da Fonte 52 (TFAMG) foram executados fora das UOs previstas na Lei 14.940/2003: "
            "pela PMMG, na Ação 4374 – Policiamento Especializado (meio ambiente); pelo FFP, na Ação 7428 – "
            "Benefícios Previdenciários – FEAM (inativos); e em outras funções (BGE 2025, p. 622-623).",
            "Na defesa (p. 77-79), o Estado alegou a finalidade ambiental dos gastos da PMMG, a vinculação via "
            "IPU à UO 2091 – FEAM, a tese do STF de que taxas não têm destinação vinculada (ADI 6145) e, "
            "subsidiariamente, a DRU estadual (art. 76-A do ADCT). A Cfamge manteve a determinação: a vinculação "
            "decorre de lei estadual, o IPU não substitui o destinatário legal e cabe ao Executivo formalizar "
            "eventual uso do art. 76-A.",
        ],
        "competencia": "Competência da SPLOR na alocação de fontes na LOA e nos créditos (art. 37, II e III, do "
                       "Decreto 48.636/2023). A classificação da receita e a eventual aplicação da DRU envolvem "
                       "a SEF e a AGE. A execução envolve SEMAD, FEAM, IEF, PMMG e FFP/IPSEMG.",
        "respostas": [
            ("Nota Técnica SEPLAG/SPLOR nº 21/2026 (D44)", "19/06/2026", "Não informado",
             "Defendeu a finalidade ambiental dos gastos da PMMG (Companhias de Meio Ambiente, cooperação com o "
             "SISEMA) e a vinculação pelo IPU à UO 2091. Comprometeu-se a reavaliar o uso da Fonte 52 nos "
             "inativos da FEAM."),
            ("Nota Técnica SEPLAG/SPLOR nº 21/2026 (C33)", "19/06/2026", "Não informado",
             "Informou que está sendo providenciada, ainda em 2026, a substituição da Fonte 52 por outra fonte "
             "própria da FEAM na complementação das despesas com inativos."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "Inativos da FEAM: conforme compromisso assumido na defesa, a utilização da Fonte 52 na Ação 7428 "
            "foi substituída por outra fonte de recursos próprios da FEAM [confirmar: data e decreto de "
            "alteração orçamentária em 2026]. No PLOA 2027, essa despesa não está programada com a Fonte 52 "
            "[confirmar].",
            "Demais execuções fora de SEMAD, FEAM e IEF: no PLOA 2027, a Fonte 52 foi programada exclusivamente "
            "nas unidades orçamentárias de SEMAD, FEAM e IEF [confirmar]. As despesas da PMMG com policiamento "
            "ambiental serão financiadas por outras fontes. Alternativamente, caso o Estado opte pela "
            "desvinculação de que trata o art. 76-A do ADCT, a medida será formalizada e evidenciada nos "
            "registros orçamentários e contábeis, conforme orientação da Cfamge, em articulação com a SEF e a "
            "AGE.",
            "Plano de ação: (1) concluir a substituição de fonte nos inativos da FEAM (SPLOR e FEAM, 2026); (2) "
            "restringir a Fonte 52 às UOs de SEMAD, FEAM e IEF na LOA 2027 (SPLOR/SCPO); (3) decidir sobre a "
            "aplicação formal do art. 76-A do ADCT (SEF e AGE, 1º trimestre de 2027).",
        ],
        "atencao": [
            "Confirmar com a SCPO/DCPPN a alocação da Fonte 52 no PLOA 2027 e se a troca de fonte dos inativos "
            "da FEAM foi efetivada em 2026.",
            "A decisão entre restringir a fonte ou formalizar a DRU (art. 76-A) é estratégica e precisa da SEF e "
            "da AGE. Não assumir as duas opções sem decisão.",
        ],
    },
    # ------------------------------------------------------------------ 18
    {
        "ref": "R49 (2025)",
        "tema": "Evidenciação da Reserva de Contingência nos decretos de créditos adicionais",
        "origem": "Relatório da Análise (proposta)", "anos": "2025",
        "texto": "Recomenda-se que, em conformidade com o arcabouço normativo vigente, os decretos de abertura de "
                 "créditos adicionais que utilizarem recursos da Reserva de Contingência identifiquem essa fonte "
                 "de forma segregada, distinguindo-a das demais anulações de dotações apresentadas em sentido "
                 "amplo.",
        "visao_tce": "Proposta mantida pela Cfamge (pendente do Pleno)", "direcionamento": "Responder",
        "paginas": "Defesa 2025, p. 84-85 · BGE 2025, p. 231-232 (origem)",
        "resumo": [
            "Em 2025, os créditos adicionais financiados por anulação somaram R$ 20,452 bilhões. Desse total, "
            "R$ 542,795 milhões vieram da UO 1991 – Reserva de Contingência, mas os decretos não informaram "
            "isso de forma explícita (BGE 2025, p. 231).",
            "Na defesa (p. 84-85), a Cfamge reconheceu que a informação pode ser rastreada nos anexos dos "
            "decretos (UO 1991). Manteve a recomendação porque a informação não aparece de forma destacada ou "
            "consolidada no ato.",
        ],
        "competencia": "Competência da SPLOR: elaboração dos decretos de alteração orçamentária (art. 37, III "
                       "e VI, do Decreto 48.636/2023).",
        "respostas": [
            ("Nota Técnica SEPLAG/SPLOR nº 21/2026 (R49)", "19/06/2026", "Não informado",
             "A utilização da Reserva já é identificada de forma específica: o anexo do decreto evidencia "
             "individualmente a dotação da UO 1991. Entendeu que a sistemática atende à transparência."),
            ("Nota Técnica SEPLAG/SPLOR nº 38/2024 (R1/2021, prática análoga)", "11/10/2024", "Atendido",
             "Precedente: o art. 2º dos decretos passou a explicitar fonte, origem e valor do recurso."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento, com implementação a partir de [data, por exemplo, 01/12/2026].",
            "Em atenção à recomendação, os decretos de abertura de créditos adicionais que utilizem recursos da "
            "Reserva de Contingência passarão a indicar, no artigo que trata da origem dos recursos, inciso "
            "próprio e destacado com o montante anulado da UO 1991 – Reserva de Contingência. Esse montante "
            "ficará separado das demais anulações de dotações. Exemplo de redação: 'II – anulação de dotação "
            "da Reserva de Contingência (UO 1991), no valor de R$ ...'.",
            "A medida segue a prática já adotada no art. 2º dos decretos, que explicita fonte, origem e valor. "
            "Exige apenas ajuste no modelo de minuta da DCPPN, o que permite a implementação imediata. A partir "
            "de 2027, o GRP-Minas permitirá também a consulta consolidada dos créditos financiados pela Reserva "
            "de Contingência.",
        ],
        "atencao": [
            "Medida de baixo custo e alta chance de 'Atendida': recomenda-se que a DCPPN altere o modelo de "
            "decreto antes do envio da resposta e que a resposta já traga um decreto como evidência.",
        ],
    },
    # ------------------------------------------------------------------ 19
    {
        "ref": "R51 (2025)",
        "tema": "Plano Mineiro de Combate à Miséria (FEM)",
        "origem": "Relatório da Análise (proposta)", "anos": "2025",
        "texto": "Recomenda-se a priorização da elaboração e implementação do Plano Mineiro de Combate à Miséria, em "
                 "atendimento ao art. 8º, § 4º, I, da Lei 19.990/11.",
        "visao_tce": "Proposta mantida pela Cfamge (pendente do Pleno)", "direcionamento": "Responder",
        "paginas": "Defesa 2025, p. 86-87 · BGE 2025, p. 614 (origem)",
        "resumo": [
            "O Plano Mineiro de Combate à Miséria, previsto desde 2011 e atribuído ao Grupo Coordenador do FEM, "
            "ainda não foi elaborado. A Cfamge mapeou a LOA 2025 e verificou que 52,16% do empenhado na Fonte 71 "
            "(R$ 318,1 milhões) foi para ações de público abrangente ou universal (BGE 2025, p. 614).",
            "Na defesa (p. 86-87), a Cfamge reconheceu as iniciativas relatadas: Estudo Multidimensional da "
            "Pobreza (SEDESE), discussões no Grupo Coordenador e acompanhamento do Fórum Técnico Minas Sem "
            "Miséria (ALMG). Manteve a recomendação porque o Plano segue pendente e os recursos continuam sendo "
            "executados sem ele.",
        ],
        "competencia": "O Plano cabe ao Grupo Coordenador do FEM (Lei 19.990/2011, art. 8º, § 4º, I). A SEPLAG "
                       "integra o Grupo e exerce sua secretaria executiva (Relatório de Transição SPLOR). A SEDESE "
                       "conduz a parte técnica do diagnóstico. A SPLOR pode responder como secretaria executiva, "
                       "com insumos da SEDESE.",
        "respostas": [
            ("Nota Técnica SEPLAG/SPLOR nº 21/2026 (R51)", "19/06/2026", "Não informado",
             "Histórico: 4ª reunião (14/11/2024), com o Estudo Multidimensional da Pobreza; 9ª reunião "
             "(25/06/2025), que deliberou acompanhar o Fórum Técnico Minas Sem Miséria; relatório final em "
             "tramitação na ALMG."),
            ("Ofício SEPLAG/SPLOR nº 08/2025 (à SEDESE/CEAS)", "2025", "Não informado",
             "Tratou do FEM e do Plano Mineiro de Combate à Miséria com a SEDESE [consultar o documento para "
             "detalhar]."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "A elaboração do Plano Mineiro de Combate à Miséria está na pauta do Grupo Coordenador do FEM desde "
            "a sua reinstalação, em outubro de 2024. Os insumos técnicos já disponíveis incluem o Estudo "
            "Multidimensional da Pobreza, apresentado pela SEDESE em 14/11/2024, e as contribuições do Fórum "
            "Técnico Minas Sem Miséria, cujo relatório final [informar situação atual na ALMG].",
            "Para priorizar o tema, propõe-se o seguinte cronograma ao Grupo Coordenador: (1) apresentação da "
            "minuta do Plano pela SEDESE, incorporando as propostas do Fórum Técnico [data]; (2) deliberação e "
            "aprovação pelo Grupo Coordenador [data, preferencialmente antes da elaboração do PLOA 2028]; (3) "
            "uso do Plano como referência obrigatória para a programação da Fonte 71 a partir da LOA 2028. "
            "Responsáveis: Grupo Coordenador do FEM, com a SEDESE na coordenação técnica e a SEPLAG/SPLOR na "
            "secretaria executiva.",
        ],
        "atencao": [
            "Obter com a SEDESE e a secretaria executiva do FEM a situação atual do Fórum Técnico e das reuniões "
            "do Grupo Coordenador em 2026 (atas da 13ª reunião em diante).",
            "O cronograma precisa ser validado pelo Grupo Coordenador. Na resposta, apresentá-lo como proposta.",
        ],
    },
    # ------------------------------------------------------------------ 20
    {
        "ref": "R52 (2025)",
        "tema": "Modelo de controle orçamentário do FEM (UO própria ou segregação de fontes)",
        "origem": "Relatório da Análise (proposta)", "anos": "2025",
        "texto": "Recomenda-se a implementação de melhorias no modelo de controle orçamentário do FEM, "
                 "preferencialmente com a instituição de Unidade Orçamentária específica; caso tal medida não seja "
                 "possível, recomenda-se que sejam adotados mecanismos destinados ao fortalecimento do controle "
                 "por Fonte de Recursos, segmentando as diversas origens previstas na Lei 19.990/11, de modo a "
                 "assegurar a rastreabilidade e compatibilidade com a legislação aplicável à ASPS e MDE, "
                 "notadamente no que se refere à receita vinculável.",
        "visao_tce": "Proposta mantida pela Cfamge (pendente do Pleno)", "direcionamento": "Responder",
        "paginas": "Defesa 2025, p. 87-88 · BGE 2025, p. 614-615 (origem)",
        "resumo": [
            "O FEM é executado de forma descentralizada nos órgãos pela Fonte 71, sem UO própria (BGE 2025, "
            "p. 614-615). A Lei 19.990/2011 (art. 2º) admite múltiplas origens de recursos: concursos de "
            "prognósticos, dotações orçamentárias, transferências, doações, auxílios e o adicional de ICMS. "
            "Essas origens podem ter efeitos distintos no cálculo de ASPS e MDE.",
            "Na defesa (p. 87-88), a Cfamge registrou que a resposta do Estado não enfrentou o ponto central. "
            "O Estado alegou que a lei não fixa percentuais para ASPS/MDE, mas a recomendação trata da "
            "rastreabilidade das diferentes origens, não de percentuais. A Cfamge aceitou como compreensível a "
            "limitação do Siafi para novas fontes e manteve a recomendação.",
        ],
        "competencia": "Competência da SPLOR: estrutura de unidades orçamentárias e classificador de fontes na "
                       "LOA (art. 39 do Decreto 48.636/2023). O ementário de receitas e o cálculo de ASPS/MDE "
                       "ficam com a SEF.",
        "respostas": [
            ("Nota Técnica SEPLAG/SPLOR nº 21/2026 (R52)", "19/06/2026", "Não informado",
             "A Lei 19.990/2011 não fixa percentuais em ASPS/MDE, que podem ser cumpridos com outras fontes. O "
             "Siafi não permite criar novas fontes, o que só será possível no GRP."),
            ("Nota Técnica SEPLAG/SPLOR nº 21/2026 (C26)", "19/06/2026", "Não informado",
             "A execução do FEM já tem controles por fonte, programação, órgão, programa e ação, com "
             "aperfeiçoamento contínuo das informações gerenciais sobre o público atendido."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "Responde-se ao ponto central levantado pela Cfamge: a rastreabilidade das diferentes origens de "
            "recursos do FEM. Atualmente, a principal origem de recursos da Fonte 71 é o adicional de alíquota "
            "do ICMS destinado ao Fundo [confirmar composição com a SEF]. As receitas de cada origem são "
            "identificadas por naturezas de receita específicas no Ementário da Receita, o que já permite "
            "segregá-las na arrecadação.",
            "Para o lado da despesa, a SPLOR propõe, no GRP-Minas (2027), um detalhamento da Fonte 71 por "
            "origem prevista no art. 2º da Lei 19.990/2011. Esse detalhamento será ativado sempre que ingressar "
            "receita de origem distinta do adicional de ICMS. Isso garante a identificação correta na base de "
            "cálculo de ASPS e MDE. Será avaliada também, para o PLOA 2028, a criação de unidade orçamentária "
            "própria do FEM, ponderando o modelo de execução descentralizada pelos órgãos setoriais.",
            "Plano de ação: (1) mapear as origens de receita da Fonte 71 e seu tratamento no cálculo de ASPS/MDE "
            "(SPLOR e SEF, 1º trimestre de 2027); (2) parametrizar no GRP o detalhamento da fonte por origem "
            "(SPLOR/DCPPN e SEF, 2027); (3) apresentar ao Grupo Coordenador do FEM estudo sobre UO própria "
            "(SPLOR, até a elaboração do PLOA 2028).",
        ],
        "atencao": [
            "Confirmar com a SEF a composição atual das receitas da Fonte 71 (naturezas de receita) e se o GRP "
            "comporta detalhamento de fonte.",
            "Evitar repetir o argumento de 'percentuais de ASPS/MDE': o TCE disse expressamente que ele não "
            "enfrenta o ponto.",
        ],
    },
]

# Itens do Ofício que, pelo CSV, devem ser encaminhados a outras áreas (não respondidos pela SPLOR).
ENCAMINHAMENTOS = [
    ("R13 (2019) · D32 (2021)", "Aportes em Acompanhamento Intensivo / aderência da execução",
     "SUGER", "Projetos Estratégicos; NT 21/2026 e Memo 198/2025 já direcionaram à SUGER."),
    ("R19 (2019) · D36 (2021)", "Recomendações da CPI da Barragem de Brumadinho", "SUGER",
     "Acordo de Brumadinho; competência da Subsecretaria de Gestão Estratégica e Reparação."),
    ("R20 (2019)", "Piso Salarial Profissional Nacional do magistério", "SUGESP",
     "Política remuneratória (art. 77 do Decreto 48.636/2023)."),
    ("R1 (2020) · D17 (2021) · D1 (2022)", "Aprimoramento do PMDI", "SUGER",
     "Planejamento de longo prazo; o TCE registrou que a revisão do PMDI não foi iniciada (BGE 2025, p. 699)."),
    ("D28 (2021)", "Baixo comprometimento com o planejamento dos Projetos Estratégicos", "SUGER",
     "BGE 2025, p. 703-704: IAP dos Projetos Estratégicos caiu para 28,03 em 2025."),
    ("R34 (2022)", "Legalidade da ação 4554 – Rodovias – Reparação Brumadinho", "SUGER (e CGE/DER)",
     "Acordo de Brumadinho e controle interno."),
    ("R46 (2025)", "Projetos Estratégicos com dotação compatível e sem janelas", "SUGER",
     "Defesa 2025, p. 80-82. Recomenda-se alinhar com a resposta da SPLOR à R40/2022 (janelas)."),
]

BASES_NECESSARIAS = [
    "Execução orçamentária 2025 por programa e ação (crédito inicial, autorizado, empenhado, liquidado), "
    "extraída do Armazém Siafi: para o item R6/2022 (percentual de programas abaixo de 50%) e para atualizar "
    "o indicador 'Sucesso do Planejamento Orçamentário' (R29/D39).",
    "LOA 2026 e PLOA 2027 em base de dados (QDD), com dotação por ação, fonte e IPU: para contar as janelas "
    "orçamentárias (R40/2022), verificar a Fonte 52 (D44/2025) e a Ação 2417 (D42/2025 e D33/2021).",
    "Demonstrativo dos 50 municípios com pior IMRS que acompanha o PLOA 2027 (D22/2021).",
    "Decretos de alteração orçamentária de 2026 que utilizaram a UO 1991 – Reserva de Contingência (R49/2025).",
    "Atas do Grupo Coordenador do FEM de 2026 e situação do relatório do Fórum Técnico Minas Sem Miséria (R51/2025).",
    "Relatórios de Gestão Fiscal do 3º quadrimestre de 2026, quando publicados (R28/2020).",
]
