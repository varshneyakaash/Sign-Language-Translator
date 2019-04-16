import cv2
import numpy as np

face_class = cv2.CascadeClassifier('../XML/haarcascade_frontalface_default.xml')

def face_cutter(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_class.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        cv2.putText(image, 'No Face Found', (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
        return None

    else:
        for (x, y, w, h) in faces:
            crop = image[y:y+h, x:x+w]

        return crop


cap = cv2.VideoCapture(0)
count = 0

while True:
    _, frame = cap.read()

    if face_cutter(frame) is not None:
        count += 1
        img = cv2.resize(face_cutter(frame), (200, 200))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imwrite('./shiv/{}.jpg'.format(count), img)
        cv2.putText(img, str(count), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Cutter', img)

    else:
        print('Not found')
        pass
    if cv2.waitKey(1) == 32 or count == 200:
        break

cap.release()
cv2.destroyAllWindows()
