import cv2
import dlib
import numpy as np

predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
detector = dlib.get_frontal_face_detector()


def get_landmarks(image):
    rects = detector(image, 1)

    if len(rects) > 1 or len(rects) < 1:
        return []

    return np.matrix([[p.x, p.y] for p in predictor(image, rects[0]).parts()])

def annotate_landmarks(image, landmarks):
    image = image.copy()

    for i, point in enumerate(landmarks):
        #cv2.putText(image, '{}'.format(i), (point[0, 0]-5, point[0, 1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
        cv2.circle(image, (point[0, 0], point[0, 1]), 1, [0,0,255], 1)

    return image

def top_lip(landmarks):
    top_lip_pts = []
    for i in range(50, 53):
        top_lip_pts.append(landmarks[i])
    for i in range(61, 64):
        top_lip_pts.append(landmarks[i])
    top_lip_mean = np.mean(top_lip_pts, axis=0)

    return int(top_lip_mean[:, 1])

def bottom_lip(landmarks):
    bottom_lip_pts = []
    for i in range(65, 68):
        bottom_lip_pts.append(landmarks[i])
    for i in range(56, 59):
        bottom_lip_pts.append(landmarks[i])
    bottom_lip_mean = np.mean(bottom_lip_pts, axis=0)

    return int(bottom_lip_mean[:, 1])

def mouth_open(image):
    landmarks = get_landmarks(image)

    if landmarks == []:
        return image, 0

    new_image = annotate_landmarks(image, landmarks)
    top_lip_center = top_lip(landmarks)
    bottom_lip_center = bottom_lip(landmarks)
    diff = abs(bottom_lip_center - top_lip_center)

    return new_image, diff

cap = cv2.VideoCapture(0)
yawn = 0

while True:
    _, frame = cap.read()

    image, diff = mouth_open(frame)

    if diff > 20:
        yawn += 1

    cv2.putText(frame, 'No. of yawn {}'.format(yawn), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 1)

    cv2.imshow('Landmarks', image)
    cv2.imshow('Yamn detector', frame)

    if cv2.waitKey(1) == 32:
        break

cv2.destroyAllWindows()