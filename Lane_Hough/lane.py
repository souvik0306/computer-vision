import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r'D:\computer-vision\Photos\road4.jpg')
width,height = 700,600
image = cv.resize(img,(width,height))

blur = cv.GaussianBlur(image,(3,3),0)
gray = cv.cvtColor(blur,cv.COLOR_BGR2GRAY)

low = 50
high = 100
edges = cv.Canny(gray,low,high,3)
# cv.imshow("Edges",edges)

rho = 1
theta = np.pi/180
threshold = 80
min_line_length = 5
max_line_gap = 70

lines = cv.HoughLinesP(edges,1,np.pi/180,50,5,50)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(image, (x1, y1), (x2, y2), (0,255, 0), 3)

cv.imshow("Image",image)

cv.waitKey(0)