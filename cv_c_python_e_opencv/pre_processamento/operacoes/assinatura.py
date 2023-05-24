import os
import cv2
import matplotlib.pyplot as plt

path = os.getcwd()
img = cv2.imread(path + r'/pre_processamento/assinatura/exemplo_doc.png', cv2.IMREAD_UNCHANGED)

# fazer a copia do pdf-imagem
img1 = img.copy()

# ler a assinatura
img2 = cv2.imread(path + r'/pre_processamento/assinatura/ex_assinatura.png')

# plot da imagem
fig, axes = plt.subplots(3, 2, figsize=(20, 10))
axes[0, 0].imshow(img, cmap='gray')
axes[0, 1].imshow(img2, cmap='gray')

rows, cols, channels = img2.shape
print(f'Assinatura: {rows} pixels de altura e {cols} de largura')

# determinar o ROI que a assinatura irá ficar
roi = img1[100:rows+100, 100:cols+100]

# Processamento para insercao da assinatura
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 0, 255, cv2.THRESH_BINARY_INV)

# Uso do bitwise NOT para inverter os pixels
mask_inv = cv2.bitwise_not(mask)

# Uso do bitwise AND para pegar os pixels em comum das máscaras criadas
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

axes[1, 0].imshow(mask, cmap='gray')
axes[1, 0].set_title('Máscara assinatura invertida')
axes[1, 1].imshow(mask_inv, cmap='gray')
axes[1, 1].set_title('Bitwise - NOT')
axes[2, 0].imshow(img1_bg)

# Apenas a regiao da assinatura da imagem da assinatura
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# Coloque a assinatura no ROI e modifique a imagem principal
dst1 = cv2.add(img1_bg, img2_fg)
img1[2000:rows+2000, 500:cols+500] = dst1

axes[2, 1].imshow(img1)

plt.tight_layout()
plt.show()
