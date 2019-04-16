import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)


while True:

    _, frame = cap.read()
<<<<<<< HEAD

    cv2.rectangle(frame, (400,400), (100,100), (0,255,0), 0)
    crop_img = frame[100:400, 100:400]
=======
>>>>>>> 1fa14e879967175419e45181d01dd2e3a81486dc

    cv2.rectangle(frame, (400,400), (100,100), (0,255,0), 0)
    crop_img = frame[100:400, 100:400]

<<<<<<< HEAD
=======
    
>>>>>>> 1fa14e879967175419e45181d01dd2e3a81486dc
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (35, 35), 0)

    #OTSU binarisation Nice :-(
    _, thresh1 = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
<<<<<<< HEAD

    cv2.imshow('Thresholded', thresh1)
    _, contours, _ = cv2.findContours(thresh1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # find max coutour 
    cnt = max(contours, key=lambda x: cv2.contourArea(x))

=======

    cv2.imshow('Thresholded', thresh1)
    _, contours, _ = cv2.findContours(thresh1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # find max coutour 
    cnt = max(contours, key=lambda x: cv2.contourArea(x))
   
>>>>>>> 1fa14e879967175419e45181d01dd2e3a81486dc
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(crop_img, (x, y), (x+w, y+h), (0, 0, 255), 0)

    # finding convex hull
    hull = cv2.convexHull(cnt)

    # drawing contours on Black sheet
    drawing = np.zeros(crop_img.shape, np.uint8)
    cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 0)
    cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 0)

    # finding convex hull
    # Remember we have to pass returnPoints = False while finding convex hull, in order to find convexity defects.
    hull = cv2.convexHull(cnt, returnPoints=False)

    # finding convexity defects 
    defects = cv2.convexityDefects(cnt, hull)
    count_defects = 0
    cv2.drawContours(thresh1, contours, -1, (0, 255, 0), 3)
<<<<<<< HEAD

=======
    
>>>>>>> 1fa14e879967175419e45181d01dd2e3a81486dc
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i,0]

        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])

        # find length of all sides of triangle
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

        # apply cosine rule here
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57

        # ignore angles > 90 and highlight rest with red dots
        if angle <= 90:
            count_defects += 1
            cv2.circle(crop_img, far, 1, (0,0,255), -1)
<<<<<<< HEAD

=======
        
>>>>>>> 1fa14e879967175419e45181d01dd2e3a81486dc
        cv2.line(crop_img,start, end, [0,255,0], 2)

    if count_defects == 1:
        cv2.putText(frame,'1', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 2:
        cv2.putText(frame, '2', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 3:
        cv2.putText(frame, '3', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 4:
        cv2.putText(frame,'4', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    else:
        cv2.putText(frame,'0', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

    cv2.imshow('Gesture', frame)
    #add two image in horizotal position
    all_img = np.hstack((drawing, crop_img))
    cv2.imshow('Contours', all_img)

    if cv2.waitKey(1) == 32:
        break

cv2.destroyAllWindows()