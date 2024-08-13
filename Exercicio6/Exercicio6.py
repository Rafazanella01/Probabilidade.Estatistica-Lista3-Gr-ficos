from geraGrafico import graficoDeLinha

anos = ['1998', '1999', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008']
taxaDeDesemprego = [9.0, 9.6, 9.3, 9.1, 9.7, 9.0, 9.4, 8.5, 8.2, 7.2]

graficoDeLinha(anos, taxaDeDesemprego,
               titulo='Evolução da taxa de desemprego (1998 a 2008)',
               cor='green',
               xlabel='Ano',
               ylabel='Taxa de desemprego (%)')