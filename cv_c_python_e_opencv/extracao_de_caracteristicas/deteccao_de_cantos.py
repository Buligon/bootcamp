import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('extracao_de_caracteristicas/Imagens/hospital2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

""" gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 2, 3, 0.01)
element_estr = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dst = cv2.dilate(dst, element_estr)

img[dst > 0.05*dst.max()] = [0, 0, 255]

fig = plt.figure(figsize=(10, 8))
plt.imshow(img)
plt.show()
"""

corners = cv2.goodFeaturesToTrack(gray, 10, 0.05, 0.25)

for item in corners:
    x, y = item[0]

    cv2.circle(img, (int(x), int(y)), 4, (0, 0, 255), -1)

fig = plt.figure(figsize=(10, 8))
plt.imshow(img)
plt.show()
