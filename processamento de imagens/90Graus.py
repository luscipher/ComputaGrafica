import cv2
    # carrega a imagem
img = cv2.imread("teste.jpg")
    # rotaciona a imagem em 90 graus
img_rotacionada = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    # exibe a imagem original e a imagem rotacionada
cv2.imshow("Imagem original", img)
cv2.imshow("Imagem rotacionada", img_rotacionada)
    # aguarda pressionar qualquer tecla e encerra janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
