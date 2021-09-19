import numpy as np
import cv2 as cv
import os
import pathlib as Path

haar_cascade = cv.CascadeClassifier(r'D:/computer-vision/haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy')

fac_recognizer = cv.face.LBPHFaceRecognizer_create()
fac_recognizer.read('face_trained.yml')

# p = (r'D:\computer-vision\Photos\Faces\val\mindy_kaling')
# p = (r'D:\computer-vision\Photos\Faces\val\elton_john')
# p = (r'D:\computer-vision\Photos\Faces\val\madonna')
p = (r'D:\computer-vision\Photos\Faces\val\ben_afflek')

for filepath in os.listdir(p):
    img = cv.imread(os.path.join(p, filepath))
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow('Person',gray)
    
    fac_recog = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)
    for (x,y,w,h) in fac_recog:
        face_roi = gray[y:y+h,x:x+w]
        labels, confidence = fac_recognizer.predict(face_roi)
        print(f'Labels = {people[labels]} with a confidence = {int(confidence)} %')
        cv.waitKey(3)



