import cv2
import pandas as pd
import glob
import os
import re
import matplotlib.pyplot as plt

import pytesseract

import pdf2image
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFPageCountError

path = os.getcwd()

INFO_LIMPO = []
NOME = []
LOGCORROMPIDO = []


def verificar_pasta(caminho: str) -> str:
    if os.path.isdir(caminho) == False:
        print(f'A pasta {caminho} não existe. Criando diretório.')
        os.mkdir(caminho)
    else:
        print(f'A pasta {caminho} existe.')


verificar_pasta(path + r'\leitura_de_caracteres\Repositorio')

pdfs_files = glob.glob(os.path.join(os.getcwd(), path + r'\leitura_de_caracteres\Repositorio\*.pdf'))

for fn in range(len(pdfs_files)):
    try:
        images = convert_from_path(pdfs_files[fn])

    except PDFPageCountError as e:
        print('Não foi possível ler o pdf. Corrompido')
        LOGCORROMPIDO.append(pdfs_files[fn])
        pass

    for i in range(len(images)):
        images[i].save('page.png', 'PNG')

    img = cv2.imread('page.png', cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    try:
        boxes = pytesseract.image_to_data(img)
        INFO = []

        for a, b in enumerate(boxes.splitlines()):
            print(b)
            if a != 0:
                b = b.split()
                if len(b) == 12:
                    INFO.append(b)
                    x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                    cv2.putText(img, b[11], (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
                    cv2.rectangle(img, (x, y), (x+w, y+h), (50, 50, 255), 2)

        plt.imshow(img)
        plt.show()

        INFO_LIMPO = []
        for i in range(len(INFO)):
            INFO_LIMPO.append(INFO[i][-1])

        INFO_LIMPO = ' '.join(INFO_LIMPO)
        print(INFO_LIMPO)

    except:
        print('Não foi possível ler o PDF')

    try:
        NOME.append(re.search(r"certify that (.*[A-Za-z\s]) successfully", INFO_LIMPO).group(1))
    except AttributeError:
        print('Nome nao encotrado')
