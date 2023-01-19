# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

def executar(n, saida):
    for i in range(n):
        saida += str(i+1)+"\t"
        print(saida)
saida = ''
n = int(input("Digite n: "))
executar(n, saida)