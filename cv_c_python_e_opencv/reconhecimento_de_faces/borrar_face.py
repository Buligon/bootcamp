import cv2

cascade = cv2.CascadeClassifier('reconhecimento_de_faces/Outros/Haarcascades/haarcascade_frontalface_default.xml')


def faceBlur(gray, frame):
    faces = cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        roi_frame = frame[y:y+h, x:x+w]
        blur = cv2.GaussianBlur(roi_frame, (101, 101), 0)
        frame[y:y+h, x:x+w] = blur
    return frame


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = faceBlur(gray, frame)
    cv2.imshow('Video', blur)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
