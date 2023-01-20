# (CC5P17 e CC6P17)/AUTORES:
#  THIAGO DE PAULA SOUZA
#  MATHEUS VINÍCIUS BRASIL MORAES
#  MATEUS GARCIA SANTOS
#  GABRIELE CRISTINE DA SILVA CASARI
#  HENRIQUE ALONSO
#  GUILHERME AKIO OCHI

# Modificar o canal de tons de cinza de uma imagem colorida

import cv2

def main():
  # Lê e armazena na variavel  img a imagem original e mostra na tela
  img = cv2.imread('src/img00.JPG')
  cv2.imshow('Original', img)

  # Converte a imagem de BGR para HSV
  img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  # Segmentação dos canais HSV
  matriz, saturation, intensity = cv2.split(img_hsv)

  # Altera a intensidade
  intensityChanged = intensity + 20

  # Junta os canais novamente com a intensidade alterada, e converte para BGR
  img_plus = cv2.merge((matriz, saturation, intensityChanged))
  img_bgr = cv2.cvtColor(img_plus, cv2.COLOR_HSV2BGR)

  # Converte a imagem para escala de cinza e mostra na tela
  grayscale = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
  cv2.imshow('Grayscale', grayscale)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == "__main__":
  main()