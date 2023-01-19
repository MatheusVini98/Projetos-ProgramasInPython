# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

def executar(n):
    for i in range (n+1):
        saida = ''
        for j in range(i):
            saida += str(i) +"\t"
        print(saida)
n= int(input("Digite n: "))
executar(n)    