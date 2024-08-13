from geraGrafico import graficoDeColunas

servicos = ['TV', 'Celular', 'Telefone fixo', 'PC', 'Acesso à Internet']
brasil = [91, 59, 48, 18, 14]
uniaoEuropeia = [93, 80, 78, 52, 40]

#Gráfico para o Brasil
graficoDeColunas(servicos, brasil,
                titulo='Penetração de serviços nos domicílios (2005) - Brasil', 
                cor='blue', 
                xlabel='Serviços', 
                ylabel='Penetração (%)')

#Gráfico para a União Europeia
graficoDeColunas(servicos, uniaoEuropeia,
                titulo='Penetração de serviços nos domicílios (2005) - União Europeia', 
                cor='green', 
                xlabel='Serviços', 
                ylabel='Penetração (%)')