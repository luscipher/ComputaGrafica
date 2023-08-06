import cv2

img = cv2.imread('teste.jpg', 0)
    # Equaliza o histograma
img_eq = cv2.equalizeHist(img)
    # Exibe as imagens
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem com Equalizacao de Histograma', img_eq)
cv2.waitKey(0)
cv2.destroyAllWindows()
