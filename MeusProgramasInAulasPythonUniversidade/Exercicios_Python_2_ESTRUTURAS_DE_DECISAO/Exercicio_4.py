# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

print("Calculo do IMC")
sexo=input("Digite seu sexo (M,F):")
altura_=float(input("Digite sua altura em metros:"))

if sexo == 'M':
    pesoIdeal= (72.7*altura_)-58
elif sexo =='F':
    pesoIdeal= (62.1*altura_)-44,7
else:
    print("Entrada Invalida")

print("o peso ideal do IMC e:",pesoIdeal)

