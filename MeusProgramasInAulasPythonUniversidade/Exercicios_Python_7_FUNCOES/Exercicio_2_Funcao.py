# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

def VerificaNumero(n):
    if n > 0:
        return("P")
    else:
        return("N")
n = float(input("Digite um valor numérico:"))
res=VerificaNumero(n)
print(res)

