# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

inicial = int(input('Informe o valor inicial'))
final=inicial
while (final <=inicial):
    final = int(input('Informe o valor final'))
    if (final <=inicial):
        print('O valor final deve ser maior que o valor inicial')

for i in range(inicial, final + 1):
    print (i)

