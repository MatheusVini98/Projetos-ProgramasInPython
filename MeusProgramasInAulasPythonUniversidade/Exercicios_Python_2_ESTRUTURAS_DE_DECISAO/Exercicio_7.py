# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

nota1=float(input("Digite a 1.a nota"))
nota2=float(input("Digite a 2.a nota"))
nota3=float(input("Digite a 3.a nota"))

media=(nota1+nota2+nota3)/3

if media==10:
    print("Aprovado com Distincao")
elif media<7:
    print("Reprovado.")
else:
    print("Aprovado")

print("A media do aluno é:", media)

