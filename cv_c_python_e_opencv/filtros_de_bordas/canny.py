import cv2
import matplotlib.pyplot as plt

img = cv2.imread("filtros_de_bordas/Imagens/predio.JPG")

canny = cv2.Canny(img, 60, 85)

fig = plt.figure(figsize=(20, 50))

ax1 = fig.add_subplot(121)
plt.imshow(img)

ax2 = fig.add_subplot(122)
plt.imshow(canny)

plt.show()
