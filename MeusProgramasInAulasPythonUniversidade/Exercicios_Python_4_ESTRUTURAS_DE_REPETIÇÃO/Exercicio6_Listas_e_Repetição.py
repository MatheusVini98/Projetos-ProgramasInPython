# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

meses =('Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
temperaturas ={}

for mes in meses:
    temperaturas[mes]=float(
        input('Informe a temperatura media do mes de %s:' % mes))

somaTemperaturas = 0.0
for temp in temperaturas.values():
    somaTemperaturas += temp

mediaTemperaturaAnual =somaTemperaturas /12.0

print ('Temperaturas acima da media anual:', round(mediaTemperaturaAnual,2))
for mes in meses:
    if (temperaturas[mes] >= mediaTemperaturaAnual):
        print ('Mês:', mes, '-',temperaturas[mes], 'ºC')

