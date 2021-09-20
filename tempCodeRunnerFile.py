import cv2 as cv
import numpy as np

img = cv.imread(r'D:\computer-vision\Photos\street.jpg')
width,height = 700,500
new = cv.resize(img,(width,height))
hsv = cv.cvtColor(new,cv.COLOR_BGR2HSV)
cv.imshow('People',hsv)
cv.waitKey(0)