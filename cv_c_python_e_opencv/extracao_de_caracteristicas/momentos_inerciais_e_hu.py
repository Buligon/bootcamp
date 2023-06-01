import cv2

img = cv2.imread('extracao_de_caracteristicas/Imagens/circle.JPG', 0)

momentos = cv2.moments(img)
"""
print(len(momentos))
print(momentos)

area = momentos['m00']
print(area)
print('\n')

x = momentos['m10']/area
y = momentos['m01']/area

print('Medias')
print(x)
print(y)

cx = int(momentos['m10']/momentos['m00'])
cy = int(momentos['m01']/momentos['m00'])

print('Centroide')
print(cx)
print(cy) """

momentosHu = cv2.HuMoments(momentos)

print(momentosHu.flatten())
