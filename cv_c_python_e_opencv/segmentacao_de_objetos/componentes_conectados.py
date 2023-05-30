import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

img_names = glob.glob('segmentacao_de_objetos/Imagens/projeto/*jpg')
font = cv2.FONT_HERSHEY_SIMPLEX

print(f'Imagens a serem analisadas: {img_names}')

for fn in img_names:
    areas = list()

    img = cv2.imread(fn, 1)

    B, G, R = cv2.split(img)

    img_bil = cv2.bilateralFilter(G, 1, 90, 90)
    img_blur = cv2.blur(img_bil, (5, 5))

    img_th = cv2.threshold(img_blur, 190, 255, cv2.THRESH_BINARY)[1]

    img_dilate = cv2.dilate(img_th, np.ones((4, 4), np.uint8),
                            iterations=1)

    """ NÃO USAR IDENTAÇÃO, retirar ao descomentar
    plt.figure(figsize=(16, 8))

    plt.subplot(2, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original')

    plt.subplot(2, 3, 2)
    plt.imshow(G, cmap='gray')
    plt.title('Green')

    plt.subplot(2, 3, 3)
    plt.imshow(img_bil, cmap='gray')
    plt.title('Filtro Bilateral')

    plt.subplot(2, 3, 4)
    plt.imshow(img_blur, cmap='gray')
    plt.title('Filtro Blur')

    plt.subplot(2, 3, 5)
    plt.imshow(img_th, cmap='gray')
    plt.title('Imagem Threshold')

    plt.subplot(2, 3, 6)
    plt.imshow(img_dilate, cmap='gray')
    plt.title('Imagem Dilatada')

    plt.show()
    """
    numlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        img_dilate, 4, cv2.CV_8U)

    areas.append(stats)
    df_areas = pd.DataFrame(areas[0], columns=['X', 'Y', 'W', 'H', 'AREA'])
    # primeira linha é o quadrado da imagem em si
    df_areas.drop(df_areas.index[0], inplace=True)
    parafusos = df_areas[df_areas['AREA'] > 900]  # parafusos
    porcas = df_areas[df_areas['AREA'] < 899]  # porcas

    label_hue = np.uint8(179*labels/np.max(labels))
    blank_ch = 255*np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

    labeled_img[label_hue == 0] = 0

    qtde_elemen = numlabels - 1

    flag = True

    if (len(parafusos) != 10):
        print(f'Falta {abs(len(parafusos) - 10)} parafusos')
        cv2.putText(img, f'Falta {abs(len(parafusos) - 10)} parafusos', (50, 700), font, 1.5, (255, 255, 255), 2, cv2.LINE_AA)
        flag = False

    if (len(porcas) != 10):
        print(f'Falta {abs(len(porcas) - 10)} porcas')
        cv2.putText(img, f'Falta {abs(len(porcas) - 10)} porcas', (50, 750), font, 1.5, (255, 255, 255), 2, cv2.LINE_AA)
        flag = False

    if flag is True:
        print('Conjunto aprovado')
        cv2.putText(img, 'Conjunto Aprovado', (200, 750), font, 1.5, (255, 255, 255), 2, cv2.LINE_AA)

    img_concate = cv2.hconcat([cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cv2.cvtColor(labeled_img, cv2.COLOR_BGR2RGB)])
    img_text = np.zeros((img_concate.shape[0], 50), dtype=np.uint8)
    imagem_total = cv2.hconcat([cv2.cvtColor(img_concate, cv2.COLOR_BGR2RGB), cv2.cvtColor(img_text, cv2.COLOR_BGR2RGB)])
    plt.imshow(imagem_total)
    plt.axis('off')
    plt.title('Imagem')
    plt.show()
