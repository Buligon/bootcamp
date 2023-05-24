import cv2
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(10, 5))

img = cv2.imread("pre_processamento/1.jpg")

lut = np.zeros(256, dtype="uint8")
for i in range(256):
    if i < 200:
        lut[i] = 0
    else:
        lut[i] = 255

# Aplique a LUT na imagem
img_contrast = cv2.LUT(img, lut)

# Exibir a imagem original e a imagem com contraste aumentado
axes[0, 0].imshow(img)
axes[0, 0].set_title('Original')
axes[0, 1].imshow(img_contrast)
axes[0, 1].set_title('Contraste aumentado')

# Crie uma LUT para alterar a cor da imagem para azul
lut = np.zeros((256, 1, 3), dtype="uint8")
# MATRIZ COM 3 DIMENSÕES
# lut[:, 0, 1] = np.arange(256) # VERDE
# lut[:, 0, 0] = np.arange(256) # VERMELHO
lut[:, 0, 2] = np.arange(256)  # AZUL

# Aplique a LUT na imagem
img_blue = cv2.LUT(img, lut)
axes[1, 0].imshow(img_blue)
axes[1, 0].set_title("Azul")

plt.show()
