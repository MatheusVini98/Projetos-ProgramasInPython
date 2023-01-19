# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

#Inicializando variáveis

num=0
intevalo_0_25=0
intervalo_26_50=0
intervalo_51_75=0
intervalo_76_100=0

while num >= 0:
    num=int(input("Informe um número positivo:"))
    if num >=0 and num<=25:
        intevalo_0_25+=1
    elif num>=26 and num<=50:
        intervalo_26_50+=1
    elif num>51 and num<=75:
        intervalo_51_75+=1
    elif num>76 and num<=100:
        intervalo_76_100+=1

print("A quantida de números no intevalo[0-25]é:", intevalo_0_25)
print("A quantida de números no intevalo[26-50]é:", intervalo_26_50)
print("A quantida de números no intevalo[51-75]é:", intervalo_51_75)
print("A quantida de números no intevalo[76-100]é:", intervalo_76_100)
