import cv2
import matplotlib.pyplot as plt

img = cv2.imread("operacoes_morfologicas/Imagens/placa.PNG")

element_estr = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
print(element_estr)