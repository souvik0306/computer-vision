import cv2 as cv
import numpy as np
import os

people = []
for i in os.listdir(r'D:/computer-vision/Photos/Faces/train'):
    people.append(i)
print(people)
DIR = (r'D:/computer-vision/Photos/Faces/train')

haar_cascade = cv.CascadeClassifier(r'D:/computer-vision/haar_face.xml')

features = []
labels = []
def createTrain():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_arr = cv.imread(img_path)
            gray = cv.cvtColor(img_arr,cv.COLOR_BGR2GRAY)

            faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            for (x,y,w,h) in faces:
                face_roi = gray[y:y+h,x:x+w]
                features.append(face_roi)
                labels.append(label)

createTrain()
print("Done")
features = np.array(features,dtype='object')
labels = np.array(labels)
fac_recog = cv.face.LBPHFaceRecognizer_create()

#Train 

fac_recog.train(features,labels)

fac_recog.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)