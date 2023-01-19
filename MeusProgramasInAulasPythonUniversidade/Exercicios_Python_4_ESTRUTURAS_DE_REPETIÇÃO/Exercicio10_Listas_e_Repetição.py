# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

#Calcular o Fatorial de um numero 
#termo é o termo do fatorial,pode ser chamado de numero tambem.
#range vai de 5 até 0

termo = 0
while (termo<= 0):
    termo = int(input('Voce quer o Fatorial de qual termo:'))
    if (termo <= 0 ):
        print('O termo deve ser positivo!')

fatorial = 1
for i in range (termo,0,-1):
    fatorial *=i

print(fatorial)
