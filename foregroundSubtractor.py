import cv2
import numpy as np

cap = cv2.VideoCapture(0)
_, frame = cap.read()

average = np.float32(frame)


while True:
    
    _, frame = cap.read()

    cv2.accumulateWeighted(frame, average, 0.05)

    background = cv2.convertScaleAbs(average)

    cv2.imshow('Background', background)
    cv2.imshow('Live', frame)

    if cv2.waitKey(1) == 32:
        break

cv2.destroyAllWindows()
