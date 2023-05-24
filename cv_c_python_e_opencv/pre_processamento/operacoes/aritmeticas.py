import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread('pre_processamento/Superman.png', 0)
img2 = cv.imread('pre_processamento/batman.png', 0)

imgSomada = cv.add(img1, img2)
imgSub = cv.subtract(img1, img2)
# mesclar imagens
imgTotal = cv.addWeighted(img1,  0.4, img2, 0.8, 0)
fig, axes = plt.subplots(3, 2, figsize=(20, 10))

axes[0, 0].imshow(img1, cmap=plt.cm.gray)
axes[0, 0].set_title('Imagem 1')
axes[0, 1].imshow(img2, cmap=plt.cm.gray)
axes[0, 1].set_title('Imagem 2')

# imagens são limatadas por cima (branco) ou por baixo (preto)
axes[1, 0].imshow(imgSomada, cmap=plt.cm.gray)
axes[1, 0].set_title('Adição')
axes[1, 1].imshow(imgSub, cmap=plt.cm.gray)
axes[1, 1].set_title('Subtração')
axes[2, 0].imshow(imgTotal, cmap=plt.cm.gray)
axes[2, 0].set_title('Mesclagem')

plt.tight_layout()
plt.show()
