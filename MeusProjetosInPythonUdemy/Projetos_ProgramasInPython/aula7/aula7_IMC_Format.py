nome = 'Matheus'  # string
idade = 24  # int
altura = 1.78  # float
e_maior = idade > 18  # bool
peso = 78
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'Anos de Idade e', 'Indíce de Massa Corporal é:', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')