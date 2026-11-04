"""Resumos revisados (04/11/2026) dos itens 4 (R10/2020), 7 (R1/2021) e 18 (R49/2025).

Estrutura: origem/questionamento do TCEMG → o que o Estado respondeu → o que o TCEMG não acatou.
Os rótulos antes de ':' são exibidos em negrito nos documentos Word.
Usado por demanda01_conteudo.py (documento principal) e por aplicar_resumos_compacto.py (versão compacta).
"""

RESUMOS = {
    "R10 (2020)": [
        "Origem do apontamento: na análise das contas de 2020 (BGE 2020, p. 123-124), a Cfamge verificou que os "
        "créditos especiais abertos para o enfrentamento da Covid-19 somaram R$ 280,7 milhões, acima do limite "
        "de R$ 260,4 milhões autorizado pela Lei 23.362/2020. Só o Decreto 206/2020 excedeu o limite em R$ 20,3 "
        "milhões. A Lei 23.633/2020 autorizava suplementar esses créditos especiais (até 2% da despesa fixada), "
        "mas o reforço foi aberto e registrado no Siafi como novo crédito especial, e não como crédito "
        "suplementar. Nas palavras da Cfamge, 'o Executivo não fez uso da suplementação, mas, sim, de novos "
        "créditos especiais'. O registro sistêmico, portanto, não refletia o que a norma autorizava nem o que o "
        "ato pretendia.",
        "Questionamento do TCEMG: que o Estado aprimore os controles internos, por meio de sistema, para que os "
        "registros dos créditos adicionais correspondam à autorização legal e ao decreto publicado: tipo de "
        "crédito, fonte e origem dos recursos. Na análise da defesa de 2020, a Cfamge acolheu só parcialmente "
        "as justificativas e sugeriu que 'os registros e as regras sistêmicas fossem corrigidos' (BGE 2023, "
        "p. 591).",
        "O que o Estado respondeu: a SEPLAG informou ter aprimorado os controles para mitigar erros formais nas "
        "suplementações. Reconheceu também a impossibilidade sistêmica de registrar como suplementar a "
        "suplementação de dotação criada por crédito especial, o que exigiria alterar o Siafi e o Armazém, ou "
        "esperar o GRP-Minas (RCI 2023). A partir de 2024, os decretos passaram a explicitar fonte, origem e "
        "valor no art. 2º (NT SEPLAG/SPLOR 38/2024).",
        "O que o TCEMG não acatou (BGE 2023, p. 591; BGE 2024, p. 616): (i) os erros formais têm sido "
        "corrigidos, 'contudo, nem sempre com a publicidade e transparência necessárias'; (ii) 'ainda não há uma "
        "solução definitiva', pois a correção sistêmica continua dependente do GRP; (iii) a SEF registrou que "
        "caberia à SEPLAG 'definir detalhadamente o escopo das alterações pretendidas' no Siafi/GRP, e não há "
        "registro de que isso tenha sido feito. Situação: Parcialmente Atendida. O item não foi reavaliado no "
        "BGE 2025.",
    ],
    "R1 (2021)": [
        "Questionamento do TCEMG: reitera para 2021 a R10/2020 (correspondência entre o decreto, a autorização "
        "legal e o registro no Siafi), mas admite que o controle seja feito 'seja por meio de sistema, seja via "
        "planilha Excel'. A flexibilização deixa claro que o Tribunal não exige esperar um novo sistema. Ele "
        "espera um controle interno, ainda que manual, que concilie decreto a decreto o que o ato autoriza "
        "(tipo de crédito, fonte, origem e valor) com o que foi registrado e com os saldos.",
        "O que o Estado respondeu: na NT SEPLAG/SPLOR 38/2024, informou que o art. 2º dos decretos passou a "
        "trazer fonte, origem e valor, mesmo quando há uma única fonte e origem, e considerou a recomendação "
        "atendida. No RCI 2023, mencionou o aprimoramento dos controles e a limitação do Siafi para "
        "suplementação de crédito especial.",
        "O que o TCEMG não acatou (BGE 2024, p. 616-617): a Cfamge considerou 'pertinente o detalhamento das "
        "fontes das suplementações nos decretos', mas registrou que 'ainda não aconteceu a implementação de "
        "sistema ou planilha de excel recomendadas' e que o aprimoramento dos controles 'segue sem solução "
        "definitiva'. Reproduziu ainda a avaliação da CGE: 'não houve demonstração da forma de controle interno "
        "acerca dos saldos e das informações das origens dos recursos'. Ou seja, o detalhamento no texto do "
        "decreto foi aceito como transparência, mas não substitui o controle de conciliação pedido. Situação: "
        "Parcialmente Atendida. O item não foi reavaliado no BGE 2025.",
    ],
    "R49 (2025)": [
        "Questionamento do TCEMG (BGE 2025, p. 230-232): a Lei 4.320/64 prevê como fontes de créditos "
        "adicionais o superávit financeiro, o excesso de arrecadação, a anulação de dotações e as operações de "
        "crédito. O Decreto-Lei 200/67 admite a Reserva de Contingência como fonte própria. Em 2025, os créditos "
        "financiados por anulação somaram R$ 20,452 bilhões, dos quais R$ 542,795 milhões vieram da UO 1991 – "
        "Reserva de Contingência (FES 51,9%, GDPE-SEF 20,3%). Os decretos, porém, apresentaram esse valor como "
        "'anulação de dotações' em sentido amplo, sem consignar expressamente o uso da Reserva. Para o Tribunal, "
        "isso 'compromete a transparência' e pode levar o leitor 'a entender que se trata de anulação genérica de "
        "dotações'.",
        "O que o Estado respondeu (NT SEPLAG/SPLOR 21/2026): o uso da Reserva já é identificado de forma "
        "específica, porque o anexo de cada decreto evidencia individualmente a dotação anulada da UO 1991, em "
        "observância à Lei 4.320/64, à LRF e às normas de contabilidade. Por isso, a sistemática já asseguraria "
        "transparência e rastreabilidade.",
        "O que o TCEMG não acatou (Defesa 2025, p. 84-85): reconheceu que o valor 'pode ser identificado nos "
        "anexos dos respectivos decretos' e que isso atende 'ao menos em parte' à rastreabilidade. Manteve, "
        "porém, a recomendação porque a informação não aparece 'de forma destacada ou consolidada', o que "
        "'limita a transparência e a compreensão do montante efetivamente utilizado da Reserva de Contingência "
        "em cada ato'. O Tribunal não questiona a legalidade do uso da Reserva, mas a forma de evidenciação: quer "
        "a Reserva identificada como fonte própria no corpo do decreto, separada das demais anulações.",
    ],
}

ROTULOS = ("Origem do apontamento:", "Questionamento do TCEMG", "O que o Estado respondeu", "O que o TCEMG não acatou",
           "Situação em 2026", "Situação:")
