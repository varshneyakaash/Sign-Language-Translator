import cv2
import numpy as np

cap = cv2.VideoCapture(0)
_, frame = cap.read()

x, y, w, h = 400, 240, 100, 160

tracker = (x, y, w, h)

roi = frame[y:y+h, x:x+h]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

low_calc = np.array([104, 67, 43])
high_calc = np.array([130, 188, 169])
mask = cv2.inRange(hsv_roi, low_calc, high_calc)

roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])

cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

term_cric = (cv2.TERM_CRITERIA_EPS | cv2.TermCriteria_COUNT, 10, 1)
    
while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    _, tracker = cv2.meanShift(dst, tracker, term_cric)

    (x, y, w, h) = tracker
    cv2.rectangle(frame, (x, y), (x+w, y+h), 255, 2)
    cv2.imshow('MeanShift Tracker', frame)

    if cv2.waitKey(1) == 32:
        break

cv2.destroyAllWindows() 
