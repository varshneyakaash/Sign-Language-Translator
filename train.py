import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

def start():
    photos = [f for f in listdir('./shiv/') if isfile(join('./shiv/', f))]

    Training = []
    Labels = []

    for i, file in enumerate(photos):
        path = './shiv/' + photos[i]
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        Training.append(np.asarray(img, 'uint8'))
        Labels.append(i)

    Labels = np.asarray(Labels, 'int32')

    model = cv2.face.LBPHFaceRecognizer_create()

    model.train(np.asarray(Training), np.asarray(Labels))
    print('Sucessfuly trained')

    return model

def face_lock(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face = cv2.CascadeClassifier('../XML/haarcascade_frontalface_default.xml')
    faces = face.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return image, []

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (127, 0, 255), 2)
        crop = image[y:y+h, x:x+w]
        crop = cv2.resize(crop, (200, 200))
    return image, crop

model = start()
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    
    image, face = face_lock(frame)

    try:        
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = model.predict(face)

        if result[1] < 500:
            c = int(100 - result[1]/3)
            cv2.putText(image, '{}% confident'.format(c), (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        if c > 80:
            cv2.putText(image, 'Unlocked', (0, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(image, 'Locked', (0, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Croppper', image)

    except:
        cv2.imshow('Croppper', image)
        

    if cv2.waitKey(1) == 32:
        break


cap.release()
cv2.destroyAllWindows()   
