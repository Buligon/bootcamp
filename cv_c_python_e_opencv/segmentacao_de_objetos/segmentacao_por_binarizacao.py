import cv2
import matplotlib.pyplot as plt

img = cv2.imread('segmentacao_de_objetos/Imagens/cafe.jpg')

metodo = cv2.THRESH_BINARY_INV
ret, imgBin = cv2.threshold(img, 150, 255, metodo)

fig = plt.figure(figsize=(10, 10))

ax1 = fig.add_subplot(121)
plt.imshow(img)

ax2 = fig.add_subplot(122)
plt.imshow(imgBin)

plt.show()
