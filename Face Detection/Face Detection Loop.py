import numpy as np
import cv2
import os
import pathlib as Path

haar_cascade = cv2.CascadeClassifier(r'D:\computer-vision\Face Detection\haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy')

fac_recognizer = cv2.face_LBPHFaceRecognizer.create()
fac_recognizer.read(r'D:\computer-vision\Face Detection\face_trained.yml')

# p = (r'D:\computer-vision\Photos\Faces\val\mindy_kaling')
# p = (r'D:\computer-vision\Photos\Faces\val\elton_john')
p = (r'D:\computer-vision\Photos\Faces\val\madonna')
# p = (r'D:\computer-vision\Photos\Faces\val\ben_afflek')

for filepath in os.listdir(p):
    img = cv2.imread(os.path.join(p, filepath))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Person',gray)
    
    fac_recog = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)
    for (x,y,w,h) in fac_recog:
        face_roi = gray[y:y+h,x:x+w]
        labels, confidence = fac_recognizer.predict(face_roi)
        print(f'Labels = {people[labels]} with a confidence = {int(confidence)} %')
        cv2.waitKey(3)



