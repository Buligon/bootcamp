import cv2

img = cv2.imread('segmentacao_de_objetos/Imagens/olho.PNG', 0)

imgGauss = cv2.medianBlur(img, 3)

th2 = cv2.adaptiveThreshold(imgGauss, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
th3 = cv2.adaptiveThreshold(imgGauss, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 3)

cv2.imshow('Original', img)
cv2.imshow('Imagem Média', th2)
cv2.imshow('Imagem Gaussiana', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
