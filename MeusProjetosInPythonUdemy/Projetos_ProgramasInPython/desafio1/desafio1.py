ano_atual = 2022  # Ano_Atual Vigente
nome = 'Matheus'  # Nome String do Usuario
idade = 24  # Idade do Usuario
altura = 1.78  # Altura do Usuario
peso = 78  # Peso do Usuario
imc = peso / (altura ** 2)  # Seu IMC do Usuario
ano_de_nascimento = (ano_atual - idade)  # Seu Ano de Nascimento do Usuario

print(f'O ano é {ano_atual} e {nome} tem {idade} anos e {altura} de altura e pesa {peso} kg,')
print(f'o imc de {nome} é {imc:.2f},')
print(f'{nome} nasceu em {ano_de_nascimento}')


