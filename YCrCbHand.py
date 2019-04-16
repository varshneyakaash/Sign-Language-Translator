import cv2
import numpy as np

import util.gui.YCrCbExtrator as extractor

extractor.create('YCrCb')
cap = cv2.VideoCapture(0)

while True:

	_, frame = cap.read()
	ycrcb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)

	low, high = extractor.extract('YCrCb')
	low = np.array(list(low))
	high = np.array(list(high))

	mask = cv2.inRange(ycrcb_img, low, high)
	res = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow("YCrCb", res)
	if cv2.waitKey(1) == 32:
		break

cap.release()
cv2.destroyAllWindows()
