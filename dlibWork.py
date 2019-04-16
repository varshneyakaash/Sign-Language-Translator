import cv2
import dlib
import numpy as np

predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
detector = dlib.get_frontal_face_detector()

class TooManyFaces:
    pass

class NoFaces:
    pass

def get_landmarks(image):
    rects = detector(image, 1)

    if len(rects) > 1:
        raise TooManyFaces
    if len(rects) == 0:
        raise NoFaces

    return np.matrix([[p.x, p.y] for p in predictor(image, rects[0]).parts()])

def annotate_landmarks(image, landmarks):
    image = image.copy()

    for i, point in enumerate(landmarks):
        # cv2.putText(image, '{}'.format(i), (point[0, 0], point[0, 1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
        cv2.circle(image, (point[0, 0], point[0, 1]), 1, [0,0,255], 2)

    return image


image = cv2.imread('shiv.jpg')
landmarks = get_landmarks(image)
new_image = annotate_landmarks(image, landmarks)

cv2.imshow('Dlib Work', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


