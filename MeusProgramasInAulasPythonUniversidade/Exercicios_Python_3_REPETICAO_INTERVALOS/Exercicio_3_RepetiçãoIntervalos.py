# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

#Inicializando Variavéis

num=0
jovem_0_25=0
adulto_26_50=0
idoso_51_75=0
muitoidoso_76_100=0

idadefinaljovem=0

while num >= 0:
    num=int(input("Informe um número positivo:"))
    if num>=0 and num<=25:
        jovem_0_25+=1
    elif num>=26 and num<=50:
        adulto_26_50+=1
    elif num>51 and num<=75:
        idoso_51_75+=1
    elif num>76 and num<=100:
        muitoidoso_76_100+=1

print("A quantidade de números no intervalo[0-25]é:", jovem_0_25)
print("A quantidade de números no intervalo[26-50]é:", adulto_26_50)
print("A quantidade de números no intervalo[51-75]é:", idoso_51_75)
print("A quantidade de números no intervalo[76-100]é:", muitoidoso_76_100)