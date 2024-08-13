from geraGrafico import graficoDeBarras, graficoDeColunas, graficoDeLinha, graficoDePizza

#Dados da Tabela 1
empresas = ['HP', 'IBM', 'Samsung', 'Positivo', 'LG', 'Xerox', 'Serpro', 'Dell', 'Microsoft', 'Cisco']
receitas = [2283, 2004, 934, 815, 751, 716, 673, 533, 496, 441]

#Gerar os gráficos com os dados da Tabela 1
#Gráfico de Linha
graficoDeLinha(empresas, receitas, 
               titulo='Receita Líquida das Empresas de Tecnologia (2007) - Linha', 
               cor='purple', 
               xlabel='Empresas', 
               ylabel='Receita Líquida (em US$ milhões)')

#Gráfico de Colunas
graficoDeColunas(empresas, receitas, 
                 titulo='Receita Líquida das Empresas de Tecnologia (2007) - Coluna', 
                 cor='green', 
                 xlabel='Empresas', 
                 ylabel='Receita Líquida (em US$ milhões)')

#Gráfico de Barras
graficoDeBarras(empresas, receitas, 
                titulo='Receita Líquida das Empresas de Tecnologia (2007) - Barra', 
                cor='orange', 
                xlabel='Receita Líquida (em US$ milhões)', 
                ylabel='Empresas')