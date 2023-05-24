"""
Superexpostas: histogramas com a maior parte dos elementos na direita;
Subexpostas: histogramas com a maior parte dos elementos na esquerda.

imagens divididas em:
- Shadows
- mid-tones
- highlights
"""

import cv2 as cv
from matplotlib import pyplot as plt

"""
Le a img como:
- 1: colorida
- 0: grayscale
- 1: incluindo o canal alfa
"""
img = cv.imread("pre_processamento/einstein.jpg", 0)
imgEqualizada = cv.equalizeHist(img)

# define tamanho da img
fig = plt.figure(figsize=(15, 5))

"""
ax1 = fig.add_subplot(121)
# argumento para mostrar a imagem em tom de cinza
plt.imshow(img, cmap=plt.cm.gray)

ax1 = fig.add_subplot(122)
# argumento para mostrar a imagem em tom de cinza
plt.imshow(imgEqualizada, cmap=plt.cm.gray)

plt.show()
"""

ax1 = fig.add_subplot(121)
plt.hist(img.ravel(), 256,  [0, 256])

ax1 = fig.add_subplot(122)
plt.hist(imgEqualizada.ravel(), 256,  [0, 256])

plt.show()
