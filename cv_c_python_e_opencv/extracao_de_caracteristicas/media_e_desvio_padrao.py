import cv2
import numpy as np

img = cv2.imread('extracao_de_caracteristicas/Imagens/tampa_azul.jpg', 1)
img_gray = cv2.imread('extracao_de_caracteristicas/Imagens/tampa_azul.jpg', 0)

cv2.imshow('Imagem em RGB', img)
cv2.imshow('Imagem em tons de cinza', img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

valorMedio = cv2.mean(img)
valorMedioGray = cv2.mean(img_gray)

(mean, std) = cv2.meanStdDev(img)
(meangray, stdgray) = cv2.meanStdDev(img_gray)

RGB = np.concatenate([(mean, std)]).flatten()
Gray = np.concatenate([(meangray, stdgray)]).flatten()

print('Valores da média e desvio padrão RGB')
print(valorMedio)
print(RGB)
print('Valores da média e desvio padrão tons de cinza')
print(valorMedioGray)
print(Gray)
