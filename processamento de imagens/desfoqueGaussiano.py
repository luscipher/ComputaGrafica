import cv2

img = cv2.imread("teste.jpg")
    # Aplica o filtro de desfoque gaussiano
img_blur = cv2.GaussianBlur(img, (5, 5), 0)
    # Mostra a imagem original e a imagem com o filtro de desfoque gaussiano aplicado
cv2.imshow("Imagem original", img)
cv2.imshow("Imagem com filtro de desfoque gaussiano", img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
