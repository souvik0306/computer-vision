import cv2 as cv
import numpy as np
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    faces = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5)
    # cv.imshow('Video', gray)
    if cv.waitKey(5) & 0xFF == ord('d'):  # d is the kill swich here
        break
    else:
        for (x,y,w,h) in faces:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
            cv.imshow('Final',frame)
capture.release()
capture.destroAllWindows
