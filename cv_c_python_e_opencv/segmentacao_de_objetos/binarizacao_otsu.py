import cv2

img = cv2.imread('segmentacao_de_objetos/Imagens/cafe.jpg', 0)

metodo = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
ret, imgBin = cv2.threshold(img, 0, 255, metodo)

print('O melhor limiar é: ', ret)

cv2.imshow('Original', img)
cv2.imshow('Otsu', imgBin)

cv2.waitKey(0)
cv2.destroyAllWindows()
