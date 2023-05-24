import cv2
import matplotlib.pyplot as plt

img = cv2.imread("filtros_de_bordas/Imagens/por_sol.png")

fig = plt.figure(figsize=(20, 50))

edgePreservingImage = cv2.edgePreservingFilter(img, flags=2, sigma_s=50, sigma_r=0.4)
cartoon_image = cv2.stylization(img, sigma_s=150, sigma_r=0.25)

ax1 = fig.add_subplot(131)
plt.imshow(img)

ax2 = fig.add_subplot(132)
plt.imshow(edgePreservingImage)

ax3 = fig.add_subplot(133)
plt.imshow(cartoon_image)

plt.show()
