import cv2
import time

cap = cv2.VideoCapture('Teste.mp4')

if cap.isOpened() is False:
    print('Erro!')

while cap.isOpened():
    ret, frame = cap.read()

    if ret is True:
        time.sleep(1/25)
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
