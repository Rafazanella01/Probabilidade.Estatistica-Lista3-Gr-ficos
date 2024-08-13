from geraGrafico import graficoDeLinha

meses = ['Jul./2007', 'Ago./2007', 'Set./2007', 'Out./2007', 'Nov./2007', 
         'Dez./2007', 'Jan./2008', 'Fev./2008', 'Mar./2008', 'Abr./2008', 
         'Mai./2008', 'Jun./2008', 'Jul./2008']

taxas = [7.28, 7.25, 7.25, 7.21, 7.23, 7.18, 7.23, 7.25, 7.28, 7.25, 7.29, 7.33, 7.35]

graficoDeLinha(meses, taxas,
               titulo='Evolução da taxa média mensal de juros ao consumidor (2007 a 2008)',
               cor='blue',
               xlabel='Mês',
               ylabel='Taxa mensal (%)')
