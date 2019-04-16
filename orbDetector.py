import cv2
import numpy as np

def ORB_detector(image, template):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create(1000, 1.2)

    keypoints1, descriptor1 = orb.detectAndCompute(gray, None)
    keypoints2, descriptor2 = orb.detectAndCompute(template, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(descriptor1, descriptor2)

    matches = sorted(matches, key=lambda val: val.distance)

    return len(matches)

cap = cv2.VideoCapture(0)
template = cv2.imread('./template.jpg')

while True:

    _, frame = cap.read()

    # create region for capturing
    h, w = frame.shape[:2]

    top_x, top_y, bottom_x, bottom_y = int(w*0.34), int(h*0.25), int(w*0.67), int(h*0.75)

    image = frame[top_y:bottom_y, top_x:bottom_x]
    #flipping the image
    frame = cv2.flip(frame, 1)

    matches = ORB_detector(image, template)
    cv2.putText(frame, 'Matches {}'.format(matches), (50, 450), cv2.FONT_HERSHEY_COMPLEX, 2, (250, 0, 0), 2)

    if matches > 320:
        cv2.rectangle(frame, (top_x, top_y), (bottom_x, bottom_y), (0, 255, 0), 3)
        cv2.putText(frame, 'Watch found', (75, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
    else:
        cv2.rectangle(frame, (top_x, top_y), (bottom_x, bottom_y), (0, 0, 255), 3)
        cv2.putText(frame, 'Not found', (75, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)

    cv2.imshow('Ghadi Detector', frame)

    if cv2.waitKey(1) == 32:
        break

cv2.destroyAllWindows()
