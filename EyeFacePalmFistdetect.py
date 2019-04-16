import numpy as np
import cv2

def face(image):

    face = cv2.CascadeClassifier('./XML/haarcascade_frontalface_default.xml')
    eye = cv2.CascadeClassifier('./XML/haarcascade_eye.xml')
    fist = cv2.CascadeClassifier('./XML/fist.xml')
    palm = cv2.CascadeClassifier('./XML/palm.xml')


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, 1.5, 3)
    eyes = eye.detectMultiScale(gray, 1.5, 3)
    fists = fist.detectMultiScale(gray, 1.5, 3)
    palms = palm.detectMultiScale(gray, 1.5, 3)


    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (127, 0, 255), 2)
        cv2.putText(image, 'Face Found', (x, y+h+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    for (x, y, w, h) in eyes:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(image, 'Eyes Found', (x, y+h-50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)

    for (x, y, w, h) in palms:
        cv2.rectangle(image, (x, y), (x+w, y+h), (10, 255, 190), 2)
        cv2.putText(image, 'Palm Found', (x, y+h+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    for (x, y, w, h) in fists:
        cv2.rectangle(image, (x, y), (x+w, y+h), (10, 255, 0), 2)
        cv2.putText(image, 'Fist Found', (x, y+h+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
    return image

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow('Face', face(frame))
    if cv2.waitKey(1) == 32:
        break

cap.release()
cv2.destroyAllWindows()