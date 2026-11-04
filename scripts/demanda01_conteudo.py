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
            "Ponto sensível (data/dados/auxiliares/auxiliar_ipu.csv): o IPU 0 hoje identifica 'Recursos do "
            "Estado aplicados nos investimentos relativos à LC 212/2025 – Propag', ou seja, um código foi "
            "redefinido recentemente. O TCE pode alegar que a 'impossibilidade sistêmica' não impediu essa "
            "reutilização. Preparar a explicação: por que não foi possível reaproveitar ou subdividir códigos "
            "para emendas, ou por que a UPG é a solução transitória.",
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
            "conforme apurado pela própria Cfamge.",
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
            "Dados de 2025 apurados na base data/dados/execucao_2025.csv: a razão liquidado/autorizado foi "
            "86,90% (R$ 127,11 bi / R$ 146,27 bi), abaixo dos 89,96% informados para 2024. O empenhado ficou "
            "4,35% abaixo do crédito inicial (−0,68% em 2023). Esses números não favorecem a resposta, por isso "
            "foram retirados da minuta. Se a equipe quiser citar o indicador 'Sucesso do Planejamento "
            "Orçamentário', confirmar antes a metodologia oficial (escopo de Poderes e intraorçamentárias), "
            "porque a base inclui todos os Poderes.",
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
            "O demonstrativo que acompanha o PLOA 2027 (Volume 1, p. 247-248) foi atualizado com o IMRS 2024 da "
            "Fundação João Pinheiro e com as estimativas populacionais de 2026 do IBGE/TCU. Foram mantidas as "
            "exclusões já adotadas: função 28 (Encargos Especiais), função 99 (Reserva de Contingência) e UOs "
            "1915 e 1916.",
            "Em razão do calendário de elaboração do PLOA 2027, concluído em setembro de 2026, a revisão "
            "qualitativa dos programas anunciada na defesa do BGE 2025 não pôde ser incorporada a esse projeto. "
            "Ela será aplicada na elaboração do PLOA 2028, com os seguintes critérios adicionais: (i) exclusão "
            "dos programas de natureza predominantemente administrativa ou de remuneração de pessoal, como os "
            "Programas 162 e 705; (ii) inclusão de nota metodológica detalhando a proporcionalização "
            "populacional dos localizadores genéricos; (iii) disponibilização, em anexo ou em dados abertos, das "
            "estimativas por município. [Alternativa a avaliar: ajustar o demonstrativo ainda na tramitação do "
            "PLOA 2027 na ALMG.]",
            "Plano de ação: (1) aprovar os novos critérios do demonstrativo (SPLOR/DCPPN, até 31/03/2027); (2) "
            "aplicá-los no PLOA 2028 e publicar as estimativas por município (SPLOR/DCPPN, setembro de 2027); "
            "(3) rever anualmente o rol de programas, como recomendado pela Cfamge.",
        ],
        "atencao": [
            "Constatação no PLOA 2027 (Volume 1, p. 247-248): o compromisso da NT 21/2026 ('já na LOA 2027') não "
            "foi cumprido. A nota metodológica é a mesma da LOA 2026, e o demonstrativo, de R$ 3,550 bi no "
            "total, mantém o Programa 162 (Gestão de Pessoas da Rede Estadual de Ensino), que passou de "
            "R$ 525,6 mi na LOA 2026 para R$ 825,8 mi. Inclui ainda o Programa 705 (Apoio às Políticas "
            "Públicas, onde está a Ação 2417 de pessoal), com R$ 939,6 mi. Os dois somam cerca de 50% do "
            "demonstrativo.",
            "O TCE vai comparar com a promessa da defesa. A resposta precisa reconhecer isso e apresentar prazo "
            "firme (PLOA 2028) ou um ajuste ainda em 2026. Decidir com a DCPPN.",
            "Verificar se o PLOA2027_substitutivo altera o demonstrativo: a busca por 'IMRS' no substitutivo não "
            "retornou ocorrências.",
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
            "Como a LOA 2026 e o PLOA 2027 foram elaborados durante a migração para o GRP-Minas, a Ação 2417 "
            "foi mantida nesses orçamentos. A apropriação da despesa de pessoal nas ações em que os servidores "
            "atuam será restabelecida a partir do PLOA 2028 [confirmar com SPLOR/SUGESP], após a estabilização "
            "do GRP-Minas em 2027. Até lá, a SPLOR publicará [proposta] a distribuição gerencial da despesa da "
            "Ação 2417 por programa e ação, com base na lotação dos servidores, no Relatório Institucional de "
            "Monitoramento e na Avaliação Anual do PPAG. Assim fica preservada a informação de custos exigida "
            "pelo art. 50, § 3º, da LRF. Ver também a resposta à D42/2025.",
        ],
        "atencao": [
            "Constatação nas bases: a Ação 2417 foi mantida e ampliada. Foram R$ 12,585 bi na LOA 2025 (49 UOs) "
            "e R$ 12,957 bi empenhados em 2025; R$ 14,108 bi na LOA 2026 (49 UOs); R$ 15,426 bi no PLOA 2027 "
            "(50 UOs), equivalentes a 16,1% do grupo 1 e 9,9% do orçamento total. O indicador do TCE seguirá "
            "'Não Atendido' em 2026 e 2027. A data de restabelecimento precisa ser definida e informada, pois o "
            "TCE (Defesa 2025, p. 76) rejeitou justificativa sem prazo.",
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
            "Despesa conferida: o QDD fiscal do PLOA 2027 (data/dados/ploa2027_base_qdd_fiscal.xlsx) soma "
            "R$ 155,502 bi, igual ao Relatório de Transição. Conferir a receita no Volume 1 do PLOA 2027 se for "
            "citá-la.",
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
            "Em 2025, 25 dos 164 programas com crédito autorizado (15,2%, excluída a Reserva de Contingência) "
            "tiveram empenho inferior a 50% do crédito autorizado, contra 16% em 2022 e 15% em 2024. Esses "
            "programas representam apenas 4,2% do crédito autorizado total.",
            "Os fatores se concentram nas fontes de financiamento. Do saldo não empenhado desses programas, "
            "38,3% corresponde à Fonte 24 (convênios com a União), 29,4% à Fonte 95 (Acordo de Reparação de "
            "Brumadinho) e 12,1% à Fonte 80 (Acordo de Repactuação do Rio Doce). Ou seja, cerca de 80% do saldo "
            "vem de recursos de convênios e acordos judiciais, cuja execução segue cronogramas próprios de "
            "ingresso dos recursos, licitação e obras, com créditos abertos ao longo do exercício por excesso de "
            "arrecadação ou superávit financeiro. Apenas 15,3% do saldo é de recursos ordinários (Fonte 10). "
            "O caso mais relevante é o Programa 85 – Promoção de Concessões e Parcerias (R$ 3,78 bi autorizados, "
            "19,6% empenhados). O saldo se concentra no Metrô da RMBH (ação 4346, R$ 1,48 bi da Fonte 24 – "
            "convênio com a União) e no Rodoanel Metropolitano (ação 4220, R$ 728 mi da Fonte 95 – Acordo de "
            "Brumadinho). As justificativas constam do Relatório de Avaliação do PPAG 2025 (Volume 2). No Metrô, "
            "a dotação previa eventuais valores devidos à concessionária e a partida e contrapartida de termo de "
            "repasse em negociação com a União para ampliar o serviço. A execução foi afetada pelo limite do "
            "decreto de programação orçamentária e pela negativa da União em celebrar o instrumento (p. 624). "
            "No Rodoanel, os aportes da PPP dependem da comprovação do avanço físico-financeiro da concessão e "
            "serão realizados à medida que os avanços forem atestados (p. 636).",
            "As justificativas por ação são registradas bimestralmente no Sigplan e analisadas pela SEPLAG, que "
            "orienta os órgãos a qualificá-las. A partir de 2027, a integração entre programação e execução no "
            "GRP-Minas deve permitir o realinhamento mais tempestivo de dotações.",
        ],
        "atencao": [
            "Fonte dos números: data/dados/execucao_2025.csv, processada por scripts/analise_demanda01.py "
            "(lista completa em entregas/demanda-01/analises/programas_execucao_2025.csv). Incluindo a Reserva "
            "de Contingência (Programa 999), são 26 de 165 programas (15,76%).",
            "Critério adotado: empenhado/crédito autorizado. Pelo liquidado, seriam 47 programas (28,5%). "
            "Confirmar que o TCE usou o empenho no BGE 2022.",
            "Justificativas do Metrô RMBH e do Rodoanel extraídas do Relatório de Avaliação do PPAG 2025, "
            "Volume 2, p. 624 e 636 (numeração impressa). Não é necessário consultar a SEINFRA, salvo se a "
            "equipe quiser informar a situação atual (2026) do termo de repasse do Metrô.",
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
            "As janelas orçamentárias são utilizadas para ações cuja necessidade ou cujo financiamento não pode "
            "ser estimado com segurança na elaboração da LOA. É o caso de convênios, emendas parlamentares "
            "federais, doações, operações de crédito em contratação, superávit financeiro, precatórios e "
            "sentenças judiciárias. Também entram ações a serem reforçadas conforme a disponibilidade de "
            "recursos ao longo do exercício. Nesses casos, a dotação simbólica preserva a especificidade da "
            "ação e a rastreabilidade da execução, evitando a criação posterior de créditos especiais.",
            "Na LOA 2025, 115 das 950 ações (UO × ação) tinham dotação inicial de até R$ 1 mil. Ao longo do "
            "exercício, 29 delas foram suplementadas (R$ 1,06 bi autorizados) e 25 tiveram empenho (R$ 405 mi). "
            "Isso evidencia a função das janelas: receber recursos cuja disponibilidade se confirma durante o "
            "ano. Entre as janelas há dotações para precatórios e sentenças judiciárias (16 em 2025 e 20 no "
            "PLOA 2027), cujo montante depende de requisições judiciais.",
            "Plano de ação: na elaboração do PLOA 2028, a SPLOR revisará as janelas financiadas com recursos "
            "ordinários (Fonte 10) que não se refiram a precatórios, sentenças ou contrapartidas. A orientação "
            "será programar dotação compatível com o custo estimado ou consolidar a ação, com especial atenção "
            "às ações de Projetos Estratégicos (17 janelas com IAG no PLOA 2027). Responsável: SPLOR/SCPO e "
            "DCPPN. Prazo: setembro de 2027.",
        ],
        "atencao": [
            "Constatação desfavorável nas bases: o número de janelas cresceu, de 115 (LOA 2025) para 121 (LOA "
            "2026) e 130 (PLOA 2027), cerca de 12% a 14% das ações. A maioria é financiada pela Fonte 10 "
            "(recursos ordinários): 91 das dotações-janela no PLOA 2027, o que enfraquece o argumento de que "
            "janelas servem só a receitas incertas. Por isso a minuta não afirma redução e propõe uma revisão "
            "com prazo. Lista em entregas/demanda-01/analises/janelas_*.csv.",
            "Critério: ação (UO × ação) com crédito inicial total entre R$ 1 e R$ 1.000. Ajustar se a SPLOR usa "
            "outro conceito.",
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
            "A LOA 2026 e o PLOA 2027 foram elaborados ainda nesse contexto de transição e mantiveram a Ação "
            "2417. O restabelecimento da apropriação nos programas e ações em que os servidores atuam está "
            "programado para o PLOA 2028 [confirmar], a ser elaborado em 2027, após a entrada em operação do "
            "GRP-Minas (janeiro de 2027) e a estabilização do módulo de pessoal.",
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
            "Confirmado nas bases: o PLOA 2027 manteve a Ação 2417 (R$ 15,426 bi em 50 UOs, Programa 705), "
            "acima da LOA 2026 (R$ 14,108 bi) e da LOA 2025 (R$ 12,585 bi). O restabelecimento só pode ocorrer, "
            "no mínimo, na LOA 2028. Definir com SUGESP e SEF se esse prazo é factível.",
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
            "Conforme compromisso assumido na defesa, o Projeto de LOA 2027 programa a Fonte 52 exclusivamente "
            "nas unidades destinatárias previstas na Lei 14.940/2003. São R$ 23,65 milhões: R$ 13,65 milhões na "
            "SEMAD (ação 4038 – Fiscalização Ambiental) e R$ 10,00 milhões na FEAM (remuneração do pessoal "
            "ativo). Não há programação da fonte para o FFP (inativos da FEAM), para a PMMG ou para outras "
            "unidades.",
            "Inativos da FEAM: em 2026 (até 30/10), dos R$ 4,86 milhões da Fonte 52 programados na Ação 7428 (FFP), foram "
            "empenhados apenas R$ 67 mil, com a complementação transferida para outra fonte [confirmar fonte e "
            "ato]. Para 2027, essa despesa já não está programada com recursos da TFAMG.",
            "Durante a execução de 2027, a SPLOR não acolherá créditos que destinem a Fonte 52 a unidades "
            "diversas de SEMAD, FEAM e IEF. As despesas da PMMG com policiamento ambiental serão financiadas por "
            "outras fontes. Alternativamente, caso o Estado opte pela "
            "desvinculação de que trata o art. 76-A do ADCT, a medida será formalizada e evidenciada nos "
            "registros orçamentários e contábeis, conforme orientação da Cfamge, em articulação com a SEF e a "
            "AGE.",
            "Plano de ação: (1) concluir a substituição de fonte nos inativos da FEAM (SPLOR e FEAM, 2026); (2) "
            "restringir a Fonte 52 às UOs de SEMAD, FEAM e IEF na LOA 2027 (SPLOR/SCPO); (3) decidir sobre a "
            "aplicação formal do art. 76-A do ADCT (SEF e AGE, 1º trimestre de 2027).",
        ],
        "atencao": [
            "Constatação nas bases (data/dados): a prática continuou em 2026. Até 30/10/2026, a PMMG empenhou R$ 7,83 mi da Fonte "
            "52 na ação 4374 (Policiamento Especializado), via crédito de R$ 13 mi anulado da ação 4038 da "
            "SEMAD. A LOA 2026 também programou R$ 1,63 mi na SEPLAG (ação 4466 – TI), com R$ 0,58 mi "
            "empenhados. O TCE verá isso no BGE 2026. Avaliar se ainda é possível corrigir a fonte em 2026 e "
            "preparar a justificativa.",
            "Confirmar a fonte que substituiu a Fonte 52 nos inativos da FEAM em 2026.",
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
            "Situação em 2026 (base de alterações orçamentárias até 30/10/2026): 35 decretos anularam dotações "
            "da UO 1991, somando R$ 1.166,23 milhões, mais que o dobro de 2025. Em 32 deles, a anulação da "
            "Reserva aparece junto com outras anulações e remanejamentos no mesmo ato, exatamente a situação "
            "criticada pela Cfamge. Três decretos concentram 74,8% do valor: na numeração do Siafi, o 110 "
            "(22/06/2026, R$ 527,0 mi para a UO Participação no Aumento de Capital de Empresas), o 38 "
            "(11/03/2026, R$ 228,6 mi para o DER-MG) e o 108 (17/06/2026, R$ 116,7 mi para a SEINFRA).",
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
            "A rastreabilidade já existe no sistema. No Siafi-MG, toda suplementação financiada pela Reserva de "
            "Contingência é registrada com código de origem próprio (origem 19 – Anulação da Reserva de "
            "Contingência Livre – Fonte 10), distinto das demais origens. Em 2026, até 30/10, essas "
            "suplementações somam R$ 1.166,23 milhões, valor idêntico ao anulado na UO 1991, em 35 decretos. "
            "Para dar a evidenciação consolidada apontada pela Cfamge, a SEPLAG passará a publicar, "
            "quadrimestralmente em seu sítio eletrônico, demonstrativo dos créditos adicionais financiados pela "
            "Reserva de Contingência, por decreto, data, valor e unidade orçamentária beneficiada. O "
            "demonstrativo será gerado a partir desse código de origem.",
            "A medida segue a prática já adotada no art. 2º dos decretos, que explicita fonte, origem e valor. "
            "Exige apenas ajuste no modelo de minuta da DCPPN, o que permite a implementação imediata. A partir "
            "de 2027, o GRP-Minas permitirá também a consulta consolidada dos créditos financiados pela Reserva "
            "de Contingência.",
        ],
        "atencao": [
            "Medida de baixo custo e alta chance de 'Atendida': recomenda-se que a DCPPN altere o modelo de "
            "decreto antes do envio da resposta e que a resposta já traga um decreto como evidência.",
            "Relevância em 2026: até 30/10/2026, a UO 1991 teve R$ 1,166 bi anulados (inicial "
            "de R$ 1,178 bi, autorizado de R$ 11,3 mi), mais que o dobro de 2025 (R$ 542,8 mi, valor que confere "
            "com o apurado pelo TCE). O BGE 2026 deve repetir o apontamento se os decretos não mudarem.",
            "O TCE não citou números de decreto. No BGE 2025 (p. 232), apresentou apenas a distribuição por UO "
            "reforçada (FES 51,86%, GDPE-SEF 20,27% etc.).",
            "A resposta não depende dos decretos publicados: a base data/dados/alteracao_orcamentaria_2026.csv "
            "sustenta todos os números (lista completa em "
            "entregas/demanda-01/analises/reserva_contingencia_decretos_2026.csv). A numeração da base é a do "
            "Siafi, não a do decreto publicado.",
            "Vale identificar o normativo publicado de quatro decretos. O Siafi 110 (22/06/2026) é o maior "
            "(45% do total, R$ 527 mi para Participação no Aumento de Capital de Empresas), deve chamar a "
            "atenção do TCE e convém conhecer o objeto. Os Siafi 38 (DER-MG, R$ 228,6 mi) e 108 (SEINFRA, "
            "R$ 116,7 mi), que com o 110 somam 74,8%. Por fim, o Siafi 31 (28/02/2026, R$ 13 mi para o Gabinete "
            "Militar), um dos três decretos financiados só pela Reserva, para comparar a redação de decreto "
            "'puro' com a de decreto misto. Se a equipe quiser anexar um exemplo do novo modelo, usar o primeiro "
            "decreto publicado após a mudança.",
            "Ponto sensível: R$ 545,4 mi da Reserva (47% do total de 2026) foram para a UO Participação no "
            "Aumento de Capital de Empresas. Confirmar o objeto (empresa beneficiada) antes do envio, pois a "
            "Cfamge pode questionar o uso da Reserva de Contingência para aporte de capital.",
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
            ("Ofício SEPLAG/SPLOR nº 08/2025 (ao CEAS)", "07/03/2025", "Não informado",
             "Em resposta ao pedido do CEAS de priorizar o Plano em 2025, relatou a reestruturação do Grupo "
             "Coordenador (agosto de 2024), o Regimento Interno e o Estudo Multidimensional da Pobreza. "
             "Informou o acordo de iniciar a discussão do Plano a partir dos pilares de atuação e de um "
             "cronograma de elaboração, e o esforço de reuniões mais frequentes."),
        ],
        "status": "Em tratamento",
        "sugestao": [
            "Status: Em tratamento.",
            "A elaboração do Plano Mineiro de Combate à Miséria está na pauta do Grupo Coordenador do FEM desde "
            "a sua reinstalação, em outubro de 2024. Desde então, foram realizadas 19 reuniões, até 03/09/2026. "
            "Os insumos já disponíveis são o Estudo Multidimensional da Pobreza, apresentado pela SEDESE na 4ª "
            "reunião (14/11/2024), e as propostas do Fórum Técnico Minas Sem Miséria da ALMG. Na 9ª reunião "
            "(25/06/2025), o Grupo deliberou incorporar as propostas do Fórum ao Plano. O documento final do "
            "Fórum estava em aprovação na Comissão de Direitos Humanos da ALMG em maio de 2026 (17ª reunião, "
            "11/05/2026). Na 19ª reunião (03/09/2026), o relatório ainda contava apenas com o parecer da Comissão "
            "de Direitos Humanos, sem versão final aprovada. Nessa reunião, o Grupo deliberou retomar a "
            "elaboração do Plano a partir do relatório disponível, sem aguardar a versão final, e incluí-la na "
            "pauta da próxima reunião ordinária.",
            "Enquanto o Plano não é concluído, o Grupo Coordenador adotou uma medida intermediária de "
            "planejamento. Na 18ª reunião (26/06/2026), validou previamente a carteira de programas prioritários "
            "que poderão receber recursos do FEM em 2027, apresentada por SEDESE, IDENE, SEAPA, SEE, SES e "
            "pelas unidades de encargos gerais. A carteira considerou as contribuições da sociedade civil e o "
            "relatório preliminar do Fórum, compartilhado pela SEDESE com suas áreas finalísticas. O Grupo também "
            "aprovou os orçamentos do FEM antes do envio dos projetos de LOA: o de 2026 na 12ª reunião "
            "(12/09/2025) e o de 2027, de R$ 627 milhões, na 19ª reunião (03/09/2026), com a programação de "
            "cada órgão executor. Estabeleceu ainda calendário anual de reuniões ordinárias.",
            "Plano de ação proposto ao Grupo Coordenador: (1) apresentação, pela SEDESE, da estrutura e do "
            "cronograma de elaboração do Plano, incorporando o relatório do Fórum Técnico (reunião ordinária de "
            "04/12/2026); (2) elaboração da minuta do Plano (SEDESE, com apoio da SEPLAG; 1º semestre de 2027); "
            "(3) deliberação e aprovação pelo Grupo Coordenador antes da elaboração do PLOA 2028 (até "
            "julho/2027); (4) uso do Plano como referência para a programação da Fonte 71 a partir da LOA 2028. "
            "Responsáveis: Grupo Coordenador do FEM, com a SEDESE na coordenação técnica e a SEPLAG/SPLOR na "
            "secretaria executiva. [Validar prazos com SEDESE e Grupo Coordenador.]",
        ],
        "atencao": [
            "Fontes: atas da 1ª à 18ª reunião e transcrição da 19ª reunião (03/09/2026; ata ainda não "
            "lavrada), em data/atas-fem. Ao citar a 19ª reunião na resposta oficial, preferir a ata assinada, se "
            "disponível até o envio.",
            "Risco a considerar: na 19ª reunião, a SEPLAG alertou que a cobrança do adicional de 2 p.p. do ICMS "
            "(receita do FEM) termina em 31/12/2026 se não houver prorrogação (PL em tramitação na ALMG). Sem "
            "prorrogação, a programação de 2027 (R$ 627 mi) e o próprio Plano ficam sem fonte. Avaliar se "
            "convém mencionar.",
            "O TCE já rejeitou o argumento de 'aguardar o Fórum' (Defesa 2025, p. 87). A resposta precisa trazer "
            "datas. O cronograma é uma proposta e deve ser pautado e validado pelo Grupo Coordenador, "
            "idealmente na reunião de 04/12/2026, que pode ser citada como evidência.",
            "A 'carteira de programas prioritários 2027' é um avanço concreto, mas não substitui o Plano. "
            "Apresentá-la como medida intermediária.",
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
            "Responde-se ao ponto central levantado pela Cfamge: a rastreabilidade das origens de recursos do FEM "
            "e sua compatibilidade com a apuração de ASPS e MDE.",
            "A Fonte 71 tem hoje origem única. Conforme o Classificador Econômico da Despesa, ela abriga "
            "exclusivamente os recursos do adicional de até dois pontos percentuais na alíquota do ICMS (art. "
            "82, § 1º, do ADCT). Não há ingresso das demais origens admitidas pelo art. 2º da Lei 19.990/2011, "
            "como concursos de prognósticos, doações e transferências. Por isso, toda a receita da Fonte 71 é de "
            "natureza tributária e homogênea quanto ao tratamento nos mínimos constitucionais.",
            "Essa receita integra a base de cálculo dos mínimos de MDE (25%) e ASPS (12%), por se tratar de "
            "receita de imposto. Sobre ela incidem ainda a destinação ao Fundeb (20%) e a DREM (30%, art. 76-A do "
            "ADCT). Por "
            "decisão do COFIN, apresentada ao Grupo Coordenador na 12ª reunião (12/09/2025), parte da própria "
            "Fonte 71 é alocada em ações de educação e saúde voltadas ao público do Fundo. Assim, a obrigação "
            "constitucional adicional gerada pelo FEM é coberta pela própria fonte que a origina. No PLOA 2027, "
            "dos R$ 627,4 milhões da Fonte 71, R$ 156,9 milhões estão na função Educação (Trilhas de Futuro) e "
            "R$ 75,3 milhões na função Saúde (Rede de Cuidado à Pessoa com Deficiência). As regras de apuração "
            "de MDE e ASPS identificam essas despesas pela combinação fonte × função × UO, e as memórias de "
            "cálculo foram apresentadas na NT SEPLAG/SPLOR nº 38/2024.",
            "Para assegurar a rastreabilidade caso novas origens passem a ingressar no Fundo, a SPLOR criará, no "
            "Classificador de Fontes do GRP-Minas (em operação a partir de janeiro de 2027), fonte ou "
            "detalhamento de fonte específico para cada origem não tributária prevista no art. 2º da Lei "
            "19.990/2011. Essas origens não serão computadas na base de MDE e ASPS. Quanto à unidade "
            "orçamentária própria, a SPLOR apresentará ao Grupo Coordenador estudo comparando o modelo atual "
            "(execução descentralizada pelos órgãos setoriais, com controle por fonte e deliberação prévia do "
            "Grupo) e a criação de UO específica, para decisão antes do PLOA 2028.",
            "Pelo mesmo fundamento, os recursos da Fonte 71 vêm sendo usados na recomposição do Fundeb. Entre "
            "2012 e 2020, a parcela de 20% da arrecadação do adicional de ICMS devida ao Fundeb não foi "
            "repassada. A receita, que deveria ter sido destinada ao Fundo da educação básica, permaneceu "
            "indevidamente no FEM e gerou superávit financeiro. Trata-se, portanto, de recurso da própria Fonte "
            "71, arrecadado e retido de forma equivocada à época, que agora é incorporado ao Fundeb, seu "
            "destinatário constitucional. Não se trata de financiar com o FEM uma despesa alheia às suas "
            "finalidades. A recomposição atende à determinação do TCEMG (D34 do Parecer Prévio de 2021, BGE "
            "2025, p. 705-706) e ao cronograma pactuado pelo Estado, em discussão na Mesa de Conciliação "
            "(Processo 1.192.382). Foi aprovada pelo Grupo Coordenador: R$ 87,4 milhões em 2025 (13ª reunião) e "
            "R$ 237 milhões em 2026 (19ª reunião), ambos por superávit financeiro, sem redução das políticas já "
            "aprovadas. Desde 2021, o repasse ao Fundeb sobre o adicional de ICMS é feito regularmente.",
            "Plano de ação: (1) documentar a memória de cálculo da parcela da Fonte 71 nos mínimos de MDE e ASPS "
            "e publicá-la nos Relatórios do FEM (SPLOR e SEF, 1º trimestre de 2027); (2) prever no GRP-Minas a "
            "segregação das origens não tributárias do FEM (SPLOR/DCPPN e SEF, 2027); (3) apresentar estudo "
            "sobre UO própria ao Grupo Coordenador (SPLOR, até julho de 2027).",
        ],
        "atencao": [
            "Fontes: Classificador/auxiliar_fonte.csv (Fonte 71 = adicional de ICMS); Ata da 12ª reunião do "
            "FEM, de 12/09/2025 (deduções Fundeb e DREM e decisão do COFIN sobre MDE/ASPS); QDD do PLOA 2027; "
            "NT 38/2024 (memórias de MDE e ASPS com a fonte 71). Nota: a ata menciona 'RCL' como base, mas os "
            "mínimos incidem sobre a receita de impostos. A minuta usa o termo correto.",
            "Confirmado pela equipe: a Fonte 71 entra na base de cálculo dos 25% (MDE) e dos 12% (ASPS). A "
            "metodologia foi contestada pela sociedade civil e pela ALMG na 12ª reunião. A resposta deve "
            "apresentá-la com fundamento técnico e jurídico claro.",
            "Passivo do Fundeb: a execução pela EGE-SEF (ação 2049, Fonte 71) foi de R$ 87,4 mi em 2025 e "
            "R$ 215,5 mi empenhados em 2026, até 30/10/2026. A parcela aprovada na 19ª reunião é de R$ 237 mi, "
            "e a diferença deve ser confirmada com a SEF. Harmonizar o período citado: o TCE (D34/2021) fala em "
            "2012 a 2020, a ata da 13ª reunião em 2010 a 2021 e a transcrição da 19ª reunião em 'quase 10 anos' "
            "desde 2011. A minuta adota o período do TCE. Confirmar o número de parcelas restantes (a "
            "transcrição menciona recomposições em 2026, 2027 e 2028).",
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
     "Defesa 2025, p. 80-82. Informar à SUGER que o PLOA 2027 tem 17 ações com IAG de Projeto Estratégico "
     "com dotação de até R$ 1 mil (7 na LOA 2025). Alinhar com a resposta da SPLOR à R40/2022."),
]

BASES_NECESSARIAS = [
    "[Incluída] Execução 2025 e 2026 (data/dados/execucao_2025.csv e execucao_2026.csv) e QDD fiscal do PLOA "
    "2027 (data/dados/ploa2027_base_qdd_fiscal.xlsx), usados nos itens R6, R29/D39, R40, D33/D42, D44 e R49. "
    "Resultados em entregas/demanda-01/analises/ (gerados por scripts/analise_demanda01.py).",
    "[Incluída] Volumes do PLOA 2027 e do PPAG 2027 (data/legislacao-basica), com o demonstrativo do IMRS no "
    "Volume 1, p. 247-248 (D22/2021).",
    "[Incluída] Atas da 1ª à 18ª reunião do Grupo Coordenador do FEM (data/atas-fem), usadas nos itens R51 e "
    "R52.",
    "[Incluída] Relatório de Avaliação do PPAG 2025, Volume 2 (justificativas de desempenho por ação, item R6) e "
    "bases auxiliares de classificação orçamentária (data/dados/auxiliares).",
    "[Incluída] Alterações orçamentárias 2026 por decreto Siafi e origem do crédito "
    "(data/dados/alteracao_orcamentaria_2026.csv), usadas no R49. Pendente: número do normativo publicado dos "
    "decretos Siafi 110, 38, 108 e 31.",
    "[Incluída] Transcrição da 19ª reunião do Grupo Coordenador do FEM (03/09/2026). A ata oficial ainda está "
    "pendente.",
        "[Futuro] RGF do 3º quadrimestre de 2026, quando publicado (R28/2020).",
]
