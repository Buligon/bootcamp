import numpy as np
import cv2
import matplotlib.pyplot as plt

full = cv2.imread('extracao_de_caracteristicas/Imagens/ex_template_matching.jpg')
full = cv2.cvtColor(full, cv2.COLOR_BGR2RGB)

face = cv2.imread('extracao_de_caracteristicas/Imagens/rosto_template.JPG')
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

height, width, channels = face.shape

# Todos os 6 métodos para comparação em uma lista
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for m in methods:
    full_copy = full.copy()

    method = eval(m)

    res = cv2.matchTemplate(full_copy, face, method)

    """ plt.imshow(res)
    plt.title(m)
    plt.show() """

for m in methods:
    full_copy = full.copy()

    method = eval(m)

    res = cv2.matchTemplate(full_copy, face, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + width, top_left[1] + height)

    cv2.rectangle(full_copy, top_left, bottom_right, 255, 10)

    plt.subplot(121)
    plt.imshow(res)
    plt.title('Resultado do template matching')

    plt.subplot(122)
    plt.imshow(full_copy)
    plt.title('pts correlacionados')
    plt.suptitle(m)

    plt.show()
