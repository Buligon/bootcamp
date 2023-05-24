import cv2
import matplotlib.pyplot as plt

img = cv2.imread("operacoes_morfologicas/Imagens/placa.PNG")

element_estr = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
# print(element_estr)

img_process = cv2.dilate(img, element_estr, iterations=2)

fig = plt.figure(figsize=(10, 8))

ax1 = fig.add_subplot(211)
plt.imshow(img)

ax2 = fig.add_subplot(212)
plt.imshow(img_process)

plt.show()
