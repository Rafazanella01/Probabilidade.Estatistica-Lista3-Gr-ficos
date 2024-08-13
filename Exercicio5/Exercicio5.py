from geraGrafico import graficoDePizza

origemDasAutuacoes = ['Agentes do CET', 'Equipamentos eletrônicos', 'Policiais militares']
percentuais = [52.9, 29.2, 17.9]

graficoDePizza(origemDasAutuacoes, percentuais,
               titulo='Origem das autuações em São Paulo (julho de 2008)',
               cores=['blue', 'orange', 'green'])