import cv2
    # Carrega a imagem
img = cv2.imread("teste.jpg")
    # Separa os canais de cores
r, g, b = cv2.split(img)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(b, 'B: ' + str(round(cv2.mean(b)[0])), (10, 30), font, 1, (255, 255, 255), 1)
cv2.putText(g, 'G: ' + str(round(cv2.mean(g)[0])), (10, 30), font, 1, (255, 255, 255), 1)
cv2.putText(r, 'R: ' + str(round(cv2.mean(r)[0])), (10, 30), font, 1, (255, 255, 255), 1)
    # Mostra cada canal de cor
cv2.imshow("Canal R: ", r)
cv2.imshow("Canal G", g)
cv2.imshow("Canal B", b)
cv2.waitKey(0)
cv2.destroyAllWindows()