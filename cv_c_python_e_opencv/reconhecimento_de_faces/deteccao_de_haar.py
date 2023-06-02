import cv2

face_cascade = cv2.CascadeClassifier('reconhecimento_de_faces/Outros/Haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow('Face detectada', img)

    k = cv2.waitKey(30)
    if (k == 27):
        break

cap.release()
cv2.destroyAllWindows()
