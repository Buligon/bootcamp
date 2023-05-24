import cv2 as cv
from matplotlib import pyplot as plt

# caminho depende do nível em que está sendo executado no terminal
img = cv.imread("pre_processamento/colorida.jpg")
# função split separa canais de cor
azul, verde, vermelho = cv.split(img)

""" plt.imshow(img)
plt.show() """

fig = plt.figure(figsize=(20, 5))
# (primeira linha, três colunas, referente a primeira img)
ax1 = fig.add_subplot(131)
ax1.hist(azul.ravel(), 256, [0, 256])
plt.title('Histrograma cor canal azul')

ax2 = fig.add_subplot(132)
ax2.hist(verde.ravel(), 256, [0, 256])
plt.title('Histrograma cor canal verde')

ax3 = fig.add_subplot(133)
ax3.hist(vermelho.ravel(), 256, [0, 256])
plt.title('Histrograma cor canal vermelho')

plt.show()
