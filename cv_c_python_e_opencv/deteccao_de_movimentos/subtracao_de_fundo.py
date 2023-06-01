import numpy as np
import cv2

cap = cv2.VideoCapture(0)

mog = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold=10,
                                         detectShadows=True)
knn = cv2.createBackgroundSubtractorKNN(history=100, dist2Threshold=40,
                                        detectShadows=True)

while (True):
    ret, frame = cap.read()

    fgmask1 = mog.apply(frame)
    fgmask2 = knn.apply(frame)

    cv2.imshow('MOG2', fgmask1)
    cv2.imshow('KNN', fgmask2)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
