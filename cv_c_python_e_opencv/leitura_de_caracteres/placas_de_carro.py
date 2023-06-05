import cv2
import imutils
import pytesseract

def fverbose(img, verbose):
    if verbose is True:
        cv2.imshow('Imagem', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


verbose = False

img = cv2.imread('leitura_de_caracteres/outros/2.jpg')

image = imutils.resize(img, width=500)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fverbose(gray, verbose)

gray = cv2.bilateralFilter(gray, 11, 17, 17)

fverbose(gray, verbose)

edged = cv2.Canny(gray, 170, 200)

fverbose(edged, verbose)

cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST,
                           cv2.CHAIN_APPROX_SIMPLE)

img1 = image.copy()
cv2.drawContours(img1, cnts, -1, (0, 255, 0), 3)

fverbose(img1, verbose)

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
NumPlacaCnt = None

img2 = image.copy()
cv2.drawContours(img2, cnts, -1, (0, 255, 0), 3)

fverbose(img2, verbose)

count = 0
idx = 1

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02*peri, True)

    if len(approx) == 4:
        NumPlacaCnt = approx
        x, y, w, h = cv2.boundingRect(c)
        new_img = gray[y:y+h, x:x+w]
        cv2.imwrite('Placa' + str(idx) + '.png', new_img)
        break

cv2.drawContours(image, [NumPlacaCnt], -1, (0, 255, 0), 3)

fverbose(image, verbose)

Cropped_img_loc = 'Placa' + str(idx) + '.png'

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' #Linha pra ser usada em amb Windows

text = pytesseract.image_to_string(Cropped_img_loc)

print("Numero é :", text)
