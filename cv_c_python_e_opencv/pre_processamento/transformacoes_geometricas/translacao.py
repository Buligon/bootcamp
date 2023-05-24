import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

imgOriginal = cv.imread('pre_processamento/einstein.jpg', 0)

totalLinhas, totalColunas = imgOriginal.shape
# move 100 pixels em cada direção
matriz = np.float32([[1, 0, 100], [0, 1, 100]])
imgDeslocada = cv.warpAffine(imgOriginal, matriz, (totalColunas, totalLinhas))

fig = plt.figure(figsize=(10, 8))
plt.imshow(imgDeslocada, cmap=plt.cm.gray)

plt.show()
