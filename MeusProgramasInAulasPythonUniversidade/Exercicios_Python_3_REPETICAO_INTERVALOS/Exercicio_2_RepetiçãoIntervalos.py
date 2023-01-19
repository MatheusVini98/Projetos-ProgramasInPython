# (CC1P17)/AUTOR:
#  MATHEUS VINÍCIUS BRASIL MORAES

#Inicializando variavéis

nota=0.0
qtdenotas=0
somanotas=0.0

while nota >= 0:
    nota=float(input("Informe uma nota:"))
    if nota>=0:
        somanotas+=nota
        qtdenotas+=1

media = somanotas/qtdenotas

print("A media das é :", qtdenotas, "notas informadas é :" , media)

