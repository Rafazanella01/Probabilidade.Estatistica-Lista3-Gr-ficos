from geraGrafico import graficoDeBarrasMultiplas

categorias = ['Rede de água', 'Rede de esgoto', 'Fossa séptica', 'Coleta de lixo', 'Energia elétrica', 'Telefone']
valores_2007 = [83.2, 51.1, 22.3, 87.3, 98.2, 76.8]
valores_2008 = [83.9, 52.5, 20.7, 87.9, 98.6, 82.1]

graficoDeBarrasMultiplas(categorias, valores_2007, valores_2008, 
                         titulo='Infraestrutura nos domicílios (2007 vs 2008)', 
                         xlabel='Infraestrutura', 
                         ylabel='Números de domicílios (%)',
                         legenda=['2007', '2008'])