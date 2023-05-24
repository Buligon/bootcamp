import cv2 as cv
from matplotlib import pyplot as plt

# importa a imagem
img = cv.imread("pre_processamento/Cinza.jpg")

# plt.imshow(img)
# render and display all figures created during a Python session
# plt.show()

# ravel() transforma a imagem em um array
plt.hist(img.ravel(), 256, [0, 256])
plt.show()
