# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

matriz = []
for i in range(3):
    linha= []
    for j in range(3):
        linha.append(int(input('Digite o valor de [' + str(i)+ ',' + str(j) + ']:')))
    matriz.append(linha)

#imprimir em formato de matriz
for i in range(3):
    print(matriz[i])

#soma diagonal
soma = 0
k=3
print("\n\n")
for i in range(3):
    for j in range (3):
        if i==j: #diagonal
            matriz[i][j]=matriz[i][j]*k

#imprimir em formato de matriz
for i in range (3):
    print(matriz[i])
