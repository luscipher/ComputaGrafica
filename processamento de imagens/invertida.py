import cv2

# Vertical
    # Carrega a imagem
img = cv2.imread("teste.jpg")
    # Inverte a imagem verticalmente
img_invertida = cv2.flip(img, 0)
    # Mostra a imagem original e a imagem invertida verticalmente
cv2.imshow("Imagem Original", img)
cv2.imshow("Imagem Invertida", img_invertida)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Horizontal
    # Carrega a imagem
img = cv2.imread("teste.jpg")
    # Inverte a imagem horizontalmente
img_invertida = cv2.flip(img, 1)
    # Mostra a imagem invertida horizontalmente
cv2.imshow("Imagem Invertida", img_invertida)
cv2.waitKey(0)
cv2.destroyAllWindows()