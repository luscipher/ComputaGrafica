import cv2

    # Carrega a imagem em tons de cinza
img_gray = cv2.imread('teste.jpg', cv2.IMREAD_GRAYSCALE)
    # Define o valor de limiar
threshold = 100
    # Aplica a limiarização
ret, img_bw = cv2.threshold(img_gray, threshold, 255, cv2.THRESH_BINARY)
    # Mostra a imagem em tons de cinza e a imagem preto e branco resultante
cv2.imshow('Imagem em tons de cinza', img_gray)
cv2.imshow('Imagem preto e branco', img_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
