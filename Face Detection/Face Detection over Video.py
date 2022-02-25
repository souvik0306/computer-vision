import cv2 as cv
import numpy as np
capture = cv.VideoCapture(r'D:\computer-vision\WhatsApp Video 2021-12-07 at 15.27.55.mp4')

while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier(r'D:\computer-vision\Face Detection\upper_body.xml')
    faces = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=1)
    # cv.imshow('Video', gray)
    if cv.waitKey(5) & 0xFF == ord('d'):  # d is the kill switch here
        break
    else:
        for (x,y,w,h) in faces:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
            cv.imshow('Final',frame)
capture.release()
capture.destroyAllWindows()
