import cv2
import pytesseract
import imutils
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Carregue a imagem e execute o pré-processamento
image = cv2.imread('car2.jpg')
#image = imutils.resize(image, height=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)
#cv2.imshow('edged', edged)

# Encontra os contornos das arestas detectadas
contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
screenCnt = None
# Verifique se o contorno tem 4 cantos (se tiver provavelmente é uma placa de carro)
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    if len(approx) == 4:
        screenCnt = approx
        break
if screenCnt is None:
    detected = 0
    print("No contour detected")
else:
    detected = 1
    cv2.drawContours(image, [screenCnt], -1, (0, 0, 255), 3)


# Corta a região da placa
x, y, w, h = cv2.boundingRect(screenCnt)
Crop = gray[y:y+h, x:x+w]
cv2.imshow('crop', Crop)

# Execute o OCR na região da placa cortada usando o Tesseract
text = pytesseract.image_to_string(Crop, config='--psm 11')
print("NUMERO DA PLACA:", text)

cv2.waitKey(0)