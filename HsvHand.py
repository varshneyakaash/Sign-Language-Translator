import cv2
import numpy as np

import util.gui.HsvExtractor as extractor

extractor.create('HSV')
cap = cv2.VideoCapture(0)

while True:

	_, frame = cap.read()
	hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	low, high = extractor.extract('HSV')
	low = np.array(list(low))
	high = np.array(list(high))

	mask = cv2.inRange(hsv_img, low, high)
	res = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow("HSV", res)
	if cv2.waitKey(1) == 32:
		break

cap.release()
cv2.destroyAllWindows()
