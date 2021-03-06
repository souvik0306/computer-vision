import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier(r'D:\computer-vision\Face Detection\haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy')

fac_recognizer = cv.face.LBPHFaceRecognizer_create()
fac_recognizer.read(r'D:\computer-vision\Face Detection\face_trained.yml')

img = cv.imread(r'D:\computer-vision\Photos\Faces\val\madonna\mad.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

fac_recog = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)
for (x,y,w,h) in fac_recog:
    face_roi = gray[y:y+h,x:x+w]
    labels, confidence = fac_recognizer.predict(face_roi)
    print(f'Labels = {people[labels]} with confidence = {confidence}')

cv.waitKey(0)