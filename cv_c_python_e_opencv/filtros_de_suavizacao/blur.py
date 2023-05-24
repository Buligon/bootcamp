# filtro do tipo passa-baixa
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("filtros_de_suavizacao/Imagens/einstein.png")

imgM = cv2.blur(img, (5, 5))

fig, axes = plt.subplots(3, 2, figsize=(20, 20))

axes[0, 0].imshow(img)
axes[0, 0].set_title('Imagem com ruído')

axes[0, 1].imshow(imgM)
axes[0, 1].set_title('Imagem filtrada (cv2.blur)')

img2 = cv2.imread("filtros_de_suavizacao/Imagens/formas.png")

imgG = cv2.GaussianBlur(img2, (5, 5), 0)

axes[1, 0].imshow(img2)
axes[1, 0].set_title('Imagem com ruído')
axes[1, 1].imshow(imgG)
axes[1, 1].set_title('Imagem filtrada (cv2.GaussianBlur)')

img3 = cv2.imread("filtros_de_suavizacao/Imagens/head.png")

imgM = cv2.medianBlur(img3, 5)

axes[2, 0].imshow(img3)
axes[2, 0].set_title('Imagem com ruído')
axes[2, 1].imshow(imgM)
axes[2, 1].set_title('Imagem filtrada (cv2.medianBlur)')

plt.tight_layout()
plt.show()
