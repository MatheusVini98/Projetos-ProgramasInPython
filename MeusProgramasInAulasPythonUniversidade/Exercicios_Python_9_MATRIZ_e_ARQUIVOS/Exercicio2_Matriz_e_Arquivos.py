# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

print("Matriz A")
A = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input('Digite o valor de [' + str(i) + ',' + str(j) + ']:')))
    A.append(linha)
print("Matriz B")
B= []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input('Digite o valor de [' + str(i) + ',' + str(j) + ']:')))
    B.append(linha)
C = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(A[i][j]+B[i][j])
        C.append(linha)

print("Resultado - Matriz A")
for i in range (2):
    print(A[i])
print("Resultado - Matriz B")
for i in range(2):
    print(B[i])
print("Resultado - Matriz C (A+B)")
for i in range (2):
    print(C[i])

