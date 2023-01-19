# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

#print ('Informe 10 numeros')
#preciso de uma variavel que armazene os pares e impares
#range vai de 1 até 10.
#input serve para mostrar na tela oque quer e receber o que deseja!
#identação ou recuo da parte de for,vai ser repetido 10 vezes.
#depois de print numerso pares:,colocar a variavel de pares

pares = 0
impares = 0
for i in range(1,11):
    numero = int(input('Informe um numero'))
    if(numero % 2 ==0):
        pares += 1
    else:
        impares +=1

print('Numeros pares:',pares)
print('Numeros impares:',impares)

