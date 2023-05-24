import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("pre_processamento/colorida.jpg", 1)
azul, verde, vermelho = cv.split(img)

imgEqualizada_r = cv.equalizeHist(vermelho)
imgEqualizada_g = cv.equalizeHist(verde)
imgEqualizada_b = cv.equalizeHist(azul)

fig, axes = plt.subplots(3, 3, figsize=(20, 10))

axes[0, 0].hist(imgEqualizada_b.ravel(), 256, [0, 256])
axes[0, 0].set_title('Histrograma cor canal azul')

axes[0, 1].hist(imgEqualizada_g.ravel(), 256, [0, 256])
axes[0, 1].set_title('Histrograma cor canal verde')

axes[0, 2].hist(imgEqualizada_r.ravel(), 256, [0, 256])
axes[0, 2].set_title('Histrograma cor canal vermelho')

axes[1, 0].hist(azul.ravel(), 256, [0, 256])
axes[1, 0].set_title('Histrograma cor canal azul')

axes[1, 1].hist(verde.ravel(), 256, [0, 256])
axes[1, 1].set_title('Histrograma cor canal verde')

axes[1, 2].hist(vermelho.ravel(), 256, [0, 256])
axes[1, 2].set_title('Histrograma cor canal vermelho')

imgEqualizada = cv.merge([imgEqualizada_b, imgEqualizada_g, imgEqualizada_r])

axes[2, 0].imshow(img)
axes[2, 0].set_title('Imagem original')
axes[2, 2].imshow(imgEqualizada)
axes[2, 2].set_title('Imagem equalizada')

plt.tight_layout()
plt.show()
