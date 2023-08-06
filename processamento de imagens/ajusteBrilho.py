import cv2
    # carrega a imagem em escala de cinza
img = cv2.imread('teste.jpg', cv2.IMREAD_GRAYSCALE)
    # adiciona 50 ao valor de cada pixel da imagem
img_bright = cv2.add(img, 50)
    # mostra as imagens
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem com Brilho Ajustado', img_bright)
cv2.waitKey(0)
cv2.destroyAllWindows()
