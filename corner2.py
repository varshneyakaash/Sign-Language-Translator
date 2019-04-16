import cv2
import numpy as np

chess = cv2.imread('./chess.png')
cv2.imshow('Cornres', chess)
gray = cv2.cvtColor(chess, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 55, 0.01, 15)
print(corners.size)
for corner in corners:
    x, y = corner[0]
    x, y = int(x), int(y)
    cv2.circle(chess, (x, y), 3, [0,0,255], 2)

cv2.imshow('Cornres', chess)
cv2.waitKey(0)
cv2.destroyAllWindows()
