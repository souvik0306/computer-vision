import cv2 as cv
import numpy as np

img = cv.imread(r'D:/computer-vision/Photos/people.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
haar_cascade = cv.CascadeClassifier(r'D:/computer-vision/haar_face.xml')
faces = haar_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=10)
cv.imshow('Image',gray)
print(f'Number of faces: {len(faces)}')
cv.waitKey(0)












# capture = cv.VideoCapture(0)

# while True:
#     isTrue, frame = capture.read()
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     haar_cascade = cv.CascadeClassifier('haar_face.xml')
#     faces = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, miniNeighbors=3)
#     cv.imshow('Video', gray)
#     if cv.waitKey(5) & 0xFF == ord('d'):  # d is the kill swich here
#         break

# capture.release()
# capture.destroAllWindows