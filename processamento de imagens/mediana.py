import cv2
import numpy as np

img = cv2.imread('teste.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Aplica o filtro da mediana com um kernel de tamanho ksize x ksize
filtro_mediana = cv2.medianBlur(img_gray, 5)
    # Mostra a imagem original e a imagem filtrada
cv2.imshow('Original', img)
cv2.imshow("Imagem em tons de cinza", img_gray)
cv2.imshow('Filtro da Mediana', filtro_mediana)
cv2.waitKey(0)
cv2.destroyAllWindows()
