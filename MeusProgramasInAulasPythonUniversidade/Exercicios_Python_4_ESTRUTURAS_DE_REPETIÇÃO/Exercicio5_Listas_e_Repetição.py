# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

letras = []
vogais = ['A','E','I','O','U']

for i in range (0,10):
    letras.append(input('Informe um caracter:').upper())

totalConsoantes = 0
consoantes =[]
for i in range(0,10):
    if letras[i]not in vogais:
        consoantes.append(letras[i])
        totalConsoantes +=1

print('Voce digitou', totalConsoantes, 'consoantes')
print(consoantes)

