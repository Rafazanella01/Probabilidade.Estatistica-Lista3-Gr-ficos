from geraGrafico import graficoDeColunas

estados = ['São Paulo', 'Minas Gerais', 'Paraná', 'Rio Grande do Sul', 
           'Santa Catarina', 'Goiás', 'Pernambuco', 'Bahia']

producaoOvos = [773.237, 325.989, 276.420, 245.655, 172.026, 113.129, 109.725, 105.144]

graficoDeColunas(estados, producaoOvos,
                 titulo='Avicultura de postura em 2003 – principais Estados produtores',
                 cor='orange',
                 xlabel='Estados',
                 ylabel='Produção de ovos (milhões de dúzias)')