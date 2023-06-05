import cv2
import pytesseract

img = cv2.imread('leitura_de_caracteres/outros/teste_tesseract.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

boxes = pytesseract.image_to_boxes(img)

print(boxes)
hImg, wImg, _ = img.shape

for b in boxes.splitlines():
    b = b.split(' ')

    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])

    cv2.rectangle(img, (x, hImg-y), (w, hImg - h), (50, 50, 255), 2)

cv2.imshow('adjbhs', img)
cv2.waitKey(0)
