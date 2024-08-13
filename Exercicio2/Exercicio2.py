from geraGrafico import graficoDeBarras, graficoDeColunas, graficoDePizza

modelos = ['Vectra', 'Fox', 'Montana', 'Eco Sport', 'Peugeot', 'Total']
numeroDeCarros = [650, 450, 400, 350, 550, 2400]

graficoDeBarras(modelos, numeroDeCarros,
                titulo='Carros segurados pela seguradora Fortal S.A. (ago 2010) - Barra', 
                cor='purple', 
                xlabel='N° de carros', 
                ylabel='Modelos')

graficoDeColunas(modelos, numeroDeCarros, 
                titulo='Carros segurados pela seguradora Fortal S.A. (ago 2010) - Coluna', 
                cor='red', 
                xlabel='Modelos', 
                ylabel='N° de carros')

graficoDePizza(modelos, numeroDeCarros, 
              titulo='Carros segurados pela seguradora Fortal S.A. (ago 2010) - Pizza', 
              cores=['red', 'blue', 'yellow', 'purple', 'green', 'orange'])