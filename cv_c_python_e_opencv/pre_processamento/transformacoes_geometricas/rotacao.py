import cv2 as cv
import matplotlib.pyplot as plt

imgOriginal = cv.imread('pre_processamento/einstein.jpg', 0)

totalLinhas, totalColunas = imgOriginal.shape
print(f'total linhas: {totalLinhas} total colunas: {totalColunas}')

# gera uma matriz de transformação
# (meio linhas, meio colunas, quantia em graus para rotação, padrão de escala)
mat = cv.getRotationMatrix2D((totalLinhas/2, totalColunas/2), 45, 1)
# aplica a transformação na matriz
imgRotacionada = cv.warpAffine(imgOriginal, mat, (totalColunas, totalLinhas))

fig = plt.figure(figsize=(10, 8))
plt.imshow(imgRotacionada, cmap=plt.cm.gray)

plt.show()
