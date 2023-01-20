"""
Variáveis inicia com uma letra, pode conter Números, separar _,letras minúsculas
"""
nome = 'Matheus'  # string
idade = 24  # int
altura = 1.78  # float
e_maior = idade > 18  # bool
peso = 78
imc = peso / (altura ** 2)

print('Nome:', nome, type('nome'))
print('Idade:', idade, type('idade'))
print('Altura:', altura, type('altura'))
print('É maior:', e_maior, type('e_maior'))
# print('Nome:', nome,'Anos de Idade:', idade, 'Indíce de Massa Corporal:', imc)
print(nome, 'tem', idade, 'Anos de Idade e', 'Indíce de Massa Corporal é:', imc)

# print(idade * altura)  # vai sempre pegar os valores atribuidos para fazer o calcúlo !

ola = """34"""
print(ola, type('ola'))
