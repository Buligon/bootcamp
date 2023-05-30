import numpy as np
import cv2

amarelo = np.uint8([[[255, 247, 125]]])
hsv_amarelo = cv2.cvtColor(amarelo, cv2.COLOR_BGR2HSV)
print(hsv_amarelo)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # CONVERSÃO DOS FRAMES PARA HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # CONFIGURADO PARA AMARELO DO POST-IT
    # EXTRAIR COR EM https://color.adobe.com/pt/create/image-gradient HSB
    lim_inf = np.array([40, 30, 90])
    lim_sup = np.array([60, 70, 170])

    color_mask = cv2.inRange(hsv, lim_inf, lim_sup)

    (couts, hir) = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cout in couts:
        area = cv2.contourArea(cout)

        if (area > 800):
            x, y, w, h = cv2.boundingRect(cout)
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('Mascara', color_mask)
    cv2.imshow('ObjectDetectionTrack', frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()
