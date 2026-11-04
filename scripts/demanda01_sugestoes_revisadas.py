"""Sugestões de resposta revisadas (04/11/2026) dos itens 4 (R10/2020), 7 (R1/2021) e 18 (R49/2025).

Base: nova varredura de data/respostas-splor (OF SPLOR 33/2024, 40/2024 e 63/2024; Memo 170/2025; NT 38/2024;
NT 21/2026; Memo 149/2026) e a base data/dados/alteracao_orcamentaria_2026.csv.
Usado por demanda01_conteudo.py (documento principal) e por aplicar_sugestoes_compacto.py (versão compacta).
"""

SUGESTOES = {
    "R10 (2020)": [
        "Status: Em tratamento.",
        "Atos publicados: desde 2024, o art. 2º dos decretos de alteração orçamentária explicita fonte de "
        "recurso, origem e valor, mesmo quando há uma só fonte e uma só origem. A Cfamge considerou essa prática "
        "'pertinente' (BGE 2024, p. 617). As inconsistências formais apontadas nos decretos de 2023 foram "
        "reconhecidas pelo Estado, com compromisso de retificação no Diário Oficial (OF SEPLAG/SPLOR nº 33/2024 "
        "e nº 40/2024): Decretos 385 e 455 e Decretos de Transposição 497, 510, 538 e 559 [informar datas de "
        "publicação das retificações]. Nos casos posteriores, verificou-se que os atos do Executivo estavam "
        "corretos no Diário Oficial e que a divergência estava na transcrição do sítio da ALMG (Decretos 683 e "
        "690/2023 e 577 e 632/2025, Memo SEPLAG/SPLOR nº 170/2025), ou no registro tardio no Siafi, regularizado "
        "(Decreto 483/2024, OF SEPLAG/SPLOR nº 63/2024).",
        "Para dar a publicidade apontada pela Cfamge, toda retificação de decreto orçamentário passará a ser "
        "publicada no Diário Oficial e comunicada formalmente à ALMG para atualização do seu sítio. As "
        "ocorrências serão relacionadas na manifestação aos Relatórios Temáticos de Créditos Adicionais.",
        "Registro sistêmico: o Siafi-MG já registra, por decreto, a lei autorizativa (LOA ou lei específica) e "
        "a origem do crédito. Por exemplo, em 2026 há códigos próprios para créditos autorizados por lei "
        "específica e para o uso da Reserva de Contingência. Permanece a limitação já reconhecida pela Cfamge: o "
        "Siafi-MG não registra como crédito suplementar o reforço de dotação criada por crédito especial. "
        "Atendendo à observação da SEF de que caberia à SEPLAG definir o escopo da alteração (BGE 2023, p. 591), "
        "a SPLOR formalizará à SEF os requisitos para o GRP-Minas (em operação a partir de janeiro de 2027): "
        "identificação do tipo de crédito (suplementar, especial ou extraordinário), vínculo do reforço ao "
        "crédito especial de origem, lei autorizativa e origem dos recursos.",
        "Plano de ação: (1) encaminhar à SEF o documento de requisitos do registro de créditos adicionais no "
        "GRP-Minas (SPLOR/DCPPN, até 15/12/2026); (2) validar a parametrização com a SEF/SCCG (janeiro de 2027); "
        "(3) publicar no Diário Oficial e comunicar à ALMG as retificações de decretos (SPLOR/DCMEFO, contínuo); "
        "(4) informar à Cfamge, após o 1º quadrimestre de 2027, o resultado do registro no novo sistema.",
    ],
    "R1 (2021)": [
        "Status: Em tratamento [ou 'Atendida', se a conciliação de 2026 for anexada à resposta].",
        "Reitera-se a resposta à R10/2020, que tem o mesmo objeto, e solicita-se o monitoramento conjunto.",
        "Quanto ao ponto registrado pela Cfamge e pela CGE, de que não foi demonstrada a forma de controle "
        "interno dos saldos e das origens dos recursos (BGE 2024, p. 617): a SPLOR mantém, a partir dos registros "
        "do Siafi-MG, base de controle das alterações orçamentárias por decreto. A base traz número do decreto no "
        "Siafi, data, lei autorizativa, unidade orçamentária, ação, fonte, IPU, origem do crédito e valores "
        "suplementados e anulados. Em 2026, até 30/10, são 209 decretos e 3.427 registros.",
        "Sobre essa base, a SPLOR passará a fazer conciliação mensal com os decretos publicados no Diário Oficial "
        "e no sítio da ALMG, em planilha. Serão verificados: (a) a correspondência entre o número do decreto no "
        "Siafi e o número publicado, e entre os valores; (b) o equilíbrio entre anulações e suplementações nos "
        "remanejamentos; (c) a coerência entre a origem do crédito e a lei autorizativa, inclusive nos reforços "
        "de créditos especiais; (d) a identificação das anulações da Reserva de Contingência. As divergências "
        "serão corrigidas e, quando for o caso, retificadas com publicação no Diário Oficial. Esse é o controle "
        "por planilha admitido na própria recomendação. Ele vigorará até que o GRP-Minas incorpore as "
        "verificações ao sistema.",
        "Plano de ação: (1) elaborar a conciliação de 2026 (janeiro a outubro) e anexá-la como evidência "
        "(SPLOR/DCPPN e DCMEFO, até o envio ou até 31/12/2026); (2) conciliar mensalmente a partir de "
        "novembro de 2026; (3) migrar as verificações para o GRP-Minas em 2027.",
    ],
    "R49 (2025)": [
        "Status: Em tratamento, com implementação a partir de [data, por exemplo, 01/12/2026].",
        "A utilização da Reserva de Contingência como fonte de créditos adicionais tem amparo no art. 43, § 1º, "
        "III, da Lei 4.320/1964, no art. 91 do Decreto-Lei 200/1967 e no art. 12 da LDO 2026 (Lei 25.440/2025), "
        "como já esclarecido ao TCEMG no Memo SEPLAG/SPLOR nº 149/2026. A recomendação, ainda pendente de "
        "deliberação do Tribunal Pleno, trata apenas da forma de evidenciação desse uso nos atos. O Estado "
        "antecipa sua adoção.",
        "Evidenciação no ato: os decretos que utilizarem a Reserva de Contingência passarão a indicar, no artigo "
        "que trata da origem dos recursos, inciso próprio com o montante anulado da UO 1991, separado das demais "
        "anulações de dotações. Exemplo de redação: 'II – anulação de dotação da Reserva de Contingência (UO "
        "1991), no valor de R$ ...'. A medida exige apenas ajuste no modelo de minuta e pode ser implementada de "
        "imediato.",
        "Evidenciação consolidada: a rastreabilidade já existe no Siafi-MG, que registra as suplementações "
        "financiadas pela Reserva com código de origem próprio (origem 19 – Anulação da Reserva de Contingência "
        "Livre). Em 2026, até 30/10, foram 35 decretos e R$ 1.166,23 milhões, valor idêntico ao anulado na UO "
        "1991. A SEPLAG publicará em seu sítio eletrônico, quadrimestralmente, demonstrativo dos créditos "
        "adicionais financiados pela Reserva de Contingência, por decreto, data, valor e unidade beneficiada. A "
        "primeira edição trará os decretos de 2026.",
        "Plano de ação: (1) ajustar o modelo de minuta de decreto (SPLOR/DCPPN, até [data]); (2) publicar a "
        "primeira edição do demonstrativo, com os decretos de 2026 (SPLOR, até 31/01/2027); (3) atualizar "
        "quadrimestralmente o demonstrativo, que será gerado também no GRP-Minas a partir de 2027.",
    ],
}

ATENCAO_EXTRA = {
    "R10 (2020)": [
        "Confirmar com a DCMEFO se as retificações prometidas para os Decretos 385, 455, 497, 510, 538 e 559 "
        "(de 2023) foram de fato publicadas no Diário Oficial. Os relatórios do TCE de 2024 e 2025 não registram "
        "a correção, e a Cfamge informou em 2024 que não as encontrou no sítio da ALMG (OF SPLOR 40/2024). Se "
        "não foram publicadas, isso explica a crítica de 'publicidade e transparência' e precisa ser resolvido "
        "antes do envio.",
    ],
    "R1 (2021)": [
        "A base de alterações de 2026 mostra 14 números de decreto no Siafi sem registro (14, 23, 27, 50, 56, "
        "88, 123, 135, 139, 151, 152, 156, 219, 220). Mostra também 6 decretos com anulações diferentes das "
        "suplementações por remanejamento. Podem ser minutas canceladas ou decretos de outra natureza, mas devem "
        "ser explicados na conciliação antes de ela ser anexada.",
        "Se a conciliação de 2026 puder ser concluída e anexada até 12/11, o status pode ser 'Atendida'. Esse "
        "é o controle cuja falta a CGE apontou.",
    ],
}

OUTRAS = {
    "R10 (2020)": "OF SPLOR 33/2024 (defesa BGE 2023: erros materiais nos Decretos 385 e 455 e nos Decretos de "
                  "Transposição 497, 510, 538 e 559, com retificação prometida; transcrição da ALMG nos Decretos "
                  "683 e 690); OF SPLOR 40/2024 (Relatório Temático 04/2024: retificações a publicar em 2024); "
                  "OF SPLOR 63/2024 (Decreto 483/2024 registrado no Siafi após o apontamento); manifestação SEPLAG "
                  "no RCI 2023 (BGE 2023, p. 591).",
    "R1 (2021)": "OF SPLOR 33/2024, 40/2024 e 63/2024 (inconsistências decreto × Siafi × ALMG em 2023-2024); "
                 "manifestação SEPLAG no RCI 2023 (BGE 2024, p. 616).",
}
