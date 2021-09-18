import cv2 as cv
import numpy as np

img = cv.imread(r'D:/computer-vision/Photos/people2.jpg')

width, height = 700, 500
new = cv.resize(img, (width, height))

gray = cv.cvtColor(new, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier(r'D:/computer-vision/haar_face.xml')
faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
# min is the min number of rectangles the code must identify to declare it as a face
# on setting the scale close to 1.1 and 3 or 4 we are accurately able to get all 18 faces correctly
# on increasing the min> 3, we are encountering errors of +1 or -1
for (x,y,w,h) in faces:
    cv.rectangle(new,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('Final',new)
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
