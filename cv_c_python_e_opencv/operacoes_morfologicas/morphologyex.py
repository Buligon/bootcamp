import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("operacoes_morfologicas/Imagens/moeda.png")
img2 = cv2.imread("operacoes_morfologicas/Imagens/esqueleto.tif")

element_est1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
element_est2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21, 21))

imgProc1 = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, element_est1)
imgProc2 = cv2.morphologyEx(img2, cv2.MORPH_TOPHAT, element_est2)
imgProc3 = cv2.morphologyEx(img2, cv2.MORPH_BLACKHAT, element_est2)

fig = plt.figure(figsize=(15, 15))

""" ax1 = fig.add_subplot(221)
plt.imshow(img1)

ax2 = fig.add_subplot(222)
plt.imshow(img2) """

ax1 = fig.add_subplot(131)
plt.imshow(imgProc1)
plt.title("Gradiente Morfológico")

ax2 = fig.add_subplot(132)
plt.imshow(imgProc2)
plt.title("TOPHAT")

ax3 = fig.add_subplot(133)
plt.imshow(imgProc3)
plt.title("BLACKHAT")

plt.tight_layout()
plt.show()
