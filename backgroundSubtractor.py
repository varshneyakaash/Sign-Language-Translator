import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# back_fore = cv2.createBackgroundSubtractorMOG2()
back_fore = cv2.createBackgroundSubtractorKNN()

while True:
    
    _, frame = cap.read()

    mask = back_fore.apply(frame)

    cv2.imshow('BackFore', mask)

    if cv2.waitKey(1) == 32:
        break

cv2.destroyAllWindows()
