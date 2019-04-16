import cv2
import numpy as np

chess = cv2.imread('./chess.png')
cv2.imshow('Cornres', chess)

gray = cv2.cvtColor(chess, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

# corner harris require float32 data. so we need to convert it

harris_corner = cv2.cornerHarris(gray, 3, 3, 0.05)
# img - Input image, it should be grayscale and float32 type.
# blockSize - It is the size of neighbourhood considered for corner detection
# ksize - Aperture parameter of Sobel derivative used.
# k - Harris detector free parameter in the equation.

kernel = np.ones((7, 7), np.uint8)
harris_corner = cv2.dilate(harris_corner, kernel, iterations=2)

chess[harris_corner > 0.03*harris_corner.max()] = [0, 0, 255]

cv2.imshow('Corners', chess)
cv2.waitKey(0)
cv2.destroyAllWindows()
