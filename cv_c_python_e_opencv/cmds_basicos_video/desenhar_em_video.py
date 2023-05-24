import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# duas barras retornam número inteiro
x = width // 2
y = height // 2

w = width // 4
h = height // 4

while True:
    ret, frame = cap.read()

    cv2.rectangle(frame, (x, y), (w+h, y+h), color=(0, 0, 255), thickness=4)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
