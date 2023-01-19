# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

operador=input("Digite o operador (+,-,*,/):")
A = int(input("Digite o primeiro numero:"))
B = int(input("Digite o segundo numero:"))

if operador == '+':
    resultado=A+B

elif operador == '-':
    resultado=A-B

elif operador == '*':
    resultado=A*B

elif operador == '/':
    resultado=A/B

print("O resultado da operacao é:", resultado)

