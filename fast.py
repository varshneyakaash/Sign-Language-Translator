import cv2
import numpy as np

image = cv2.imread('./sift.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fast = cv2.FastFeatureDetector_create()
fast.setThreshold(8000)

keypoints = fast.detect(gray, None)

print('No. of keypoints {}'.format(len(keypoints)))

cv2.drawKeypoints(image, keypoints, image, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('FAST', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

