import imutils
import cv2
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import random
import time

path_repositorio_captcha_cut = 'extracao_de_caracteristicas/Imagens/Captcha_cut'
filelist_captcha_cut = [f for f in os.listdir(path_repositorio_captcha_cut)
                        if f.endswith('.png')]

for f in filelist_captcha_cut:
    os.remove(os.path.join(path_repositorio_captcha_cut, f))

path_repositorio_captcha = 'extracao_de_caracteristicas/Imagens/templates'
filelist_captcha = [f for f in os.listdir(path_repositorio_captcha)
                    if f.endswith('.png')]

captcha_random = random.choice(filelist_captcha)
main_image = cv2.imread(f'extracao_de_caracteristicas/Imagens/templates/{captcha_random}')

hsv = cv2.cvtColor(main_image, cv2.COLOR_BGR2HSV)

lim_inf = np.array([15, 0, 0])
lim_sup = np.array([103, 255, 255])

color_mask = cv2.inRange(hsv, lim_inf, lim_sup)

img_mediano = cv2.medianBlur(color_mask, 3)

img_bilateral = cv2.bilateralFilter(img_mediano, 9, 75, 75)

elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
img_erode = cv2.erode(img_bilateral, elementoEstruturante, iterations=1)

img_th = cv2.adaptiveThreshold(img_erode, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 11, 1)

img_th1 = img_th[0:71, 0:79]
img_th2 = img_th[0:71, 80:159]
img_th3 = img_th[0:71, 160:238]
img_th4 = img_th[0:71, 239:317]
img_th5 = img_th[0:71, 318:]

cv2.imwrite('extracao_de_caracteristicas/Imagens/Captcha_cut/captcha_pt_0.png',
            img_th1)
cv2.imwrite('extracao_de_caracteristicas/Imagens/Captcha_cut/captcha_pt_1.png',
            img_th2)
cv2.imwrite('extracao_de_caracteristicas/Imagens/Captcha_cut/captcha_pt_2.png',
            img_th3)
cv2.imwrite('extracao_de_caracteristicas/Imagens/Captcha_cut/captcha_pt_3.png',
            img_th4)
cv2.imwrite('extracao_de_caracteristicas/Imagens/Captcha_cut/captcha_pt_4.png',
            img_th5)

path_repositorio_captcha_cut = 'extracao_de_caracteristicas/Imagens/Captcha_cut/'
filelist_captcha_cut = [f for f in os.listdir(path_repositorio_captcha_cut)
                        if f.endswith(".png")]

path_repositorio = 'extracao_de_caracteristicas/Imagens/template_th_bk'
filelist = [f for f in os.listdir(path_repositorio)
            if f.endswith('.png')]

vetor_letras = []
max_valor_template = []


for j in range(len(filelist_captcha_cut)):
    img_captcha = cv2.imread(f'extracao_de_caracteristicas/Imagens/Captcha_cut/{filelist_captcha_cut[j]}')

    for i in range(len(filelist)):
        template = cv2.imread(f'extracao_de_caracteristicas/Imagens/template_th_bk/{filelist[i]}')

        (height, width) = template.shape[:2]

        temp_found = None

        match = cv2.matchTemplate(img_captcha, template, cv2.TM_CCOEFF_NORMED)
        (_, val_max, _, loc_max) = cv2.minMaxLoc(match)
        max_valor_template.append([j, {filelist[i]:val_max}])

        print(f'O valor de correspondencia e: {val_max}')

mat = pd.DataFrame(max_valor_template)

list_mat = list(mat.groupby([0]))

campeoes=[]

for i in range(len(list_mat)):
    a = list_mat[i][1]
    pontos = [list(valor.values()) for valor in a[1]]
    pontuacao = [ponto[0] for ponto in pontos]
    campea = np.flip(np.argsort(pontuacao))

    campeoes.append(campea[0])

letras_captchas = []
for j in range(len(campeoes)):
    letras_captchas.append(filelist[campeoes[j]].split('.')[0])

letras_captchas_total = pd.Series(letras_captchas)

letras_captchas_total = letras_captchas_total.str.replace('C-Dilha', 'Ç')

letras_captchas_total = letras_captchas_total.tolist()
print(letras_captchas_total)
print(captcha_random)


plt.subplot(3, 2, 1), plt.imshow(main_image)
plt.subplot(3, 2, 2), plt.imshow(color_mask)
plt.subplot(3, 2, 3), plt.imshow(img_bilateral, cmap='gray')
plt.subplot(3, 2, 4), plt.imshow(img_erode, cmap='gray')
plt.subplot(3, 2, 5), plt.imshow(img_th, cmap='gray')
plt.show()
