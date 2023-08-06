import cv2

img = cv2.imread("teste.jpg")
    # Converte a imagem para tons de cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Aplica o filtro da média
img_media = cv2.blur(img_gray, (5,5))
    # Mostra as imagens
cv2.imshow("Imagem original", img)
cv2.imshow("Imagem em tons de cinza", img_gray)
cv2.imshow("Imagem com filtro da média", img_media)
cv2.waitKey(0)
cv2.destroyAllWindows()