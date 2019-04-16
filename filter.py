import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#skin color
lower_skin = np.array([0, 48, 80], dtype = "uint8")
upper_skin = np.array([20, 255, 255], dtype = "uint8")

while True:

    _, image = cap.read()

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_image, lower_skin, upper_skin)

    res = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow('Original', image)
    cv2.imshow('HSV', hsv_image)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', res)

    if cv2.waitKey(1) == 32:
        break

cv2.destroyAllWindows()

