# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

qtde=int(input("Informe a quantidade macas:"))

if qtde>12:
    preco=0.25
else:
    preco=0.30

precoFinal=preco*qtde

print("O preco a ser pago é:", precoFinal )
