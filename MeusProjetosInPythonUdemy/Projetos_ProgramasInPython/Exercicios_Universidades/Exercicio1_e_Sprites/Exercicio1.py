# (CC5P17 e CC6P17)/AUTORES:
#  THIAGO DE PAULA SOUZA
#  MATHEUS VINÍCIUS BRASIL MORAES
#  MATEUS GARCIA SANTOS
#  GABRIELE CRISTINE DA SILVA CASARI
#  HENRIQUE ALONSO
#  GUILHERME AKIO OCHI

"""Programa em Python GIF || Processamento de Imagens Digitais e Visão Computacional """

#Esse é o Início do Código do Desenvolvimento do Programa


import cv2
import imageio

# 1.Carregando e Gravando as Sprites

sprites = []

if sprites == True:
    for i,j in zip(range(21) , range(21)):
        sprites.append(cv2.imread("src/sprites_" + str(i) + "ryu" + str(j) + ".png"))
    print("Gerando GIF do Street Fighter :"+ str(len (sprites)))
else: (print("não deu certo"))

# 2.Lendo e Salvando as Sprites

with imageio.get_writer("ultimate.gif", mode= "I")as writer:
    for k in sprites:
        print("Unindo Imagens em um GIF !")
        rgb_frame = cv2.cvtColor(k, cv2.COLOR_BGR2RGB)
        writer.append_data(rgb_frame)

# 3.Exibir imagem final (GIF) !

Gif_Final_Captura = cv2.VideoCapture("ultimate.gif")

testebooleano = True
while testebooleano:
    Ret,frame = Gif_Final_Captura.read()
    cv2.imshow("src/sprites", frame)

    if cv2.waitKey(1500) & 0xFF == ord ("q"):
        testebooleano = False

cv2.imshow("ultimate.gif")
cv2.waitKey(0)
Gif_Final_Captura.release()
cv2.destroyAllWindows()

"""import cv2
import imageio

# 1. Gravar as imagens
imagens = []

for i in range(10):
    imagens.append(cv2.imread("imagem_" + str(i) + ".jpg"))

print("Numero de imagens: " + str(len(imagens)))

# 2. Salvar como GIF

with imageio.get_writer("final.gif", mode="I") as writer:
    for j in imagens:
        print("Juntando imagens em GIF")
        rgb_frame = cv2.cvtColor(j, cv2.COLOR_BGR2RGB)
        writer.append_data(rgb_frame)

# 3. Mostrar Gif

captura = cv2.VideoCapture("final.gif")

bollteste = True
while bollteste:
    Ret, frame = captura.read()
    cv2.imshow("imagem", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
      bollteste = False

captura.release()
# cv2.destroyAllWindows()
"""