# import cv2 as cv
# img = cv.imread('Photos/cat.jfif')
# cv.imshow('Cat',img)
# cv.waitKey(0)


# import cv2 as cv
# capture = cv.VideoCapture('Photos/dog.mp4')
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
# capture.release()
# capture.destroAllWindows

# Rescale Videos -

# import cv2 as cv
# capture = cv.VideoCapture('Photos/dog.mp4')
#
# def rescale(frame,scale=0.50):
#     width = int(frame.shape[1]*scale)
#     height = int(frame.shape[0]*scale)
#     dimension = (width,height)
#     return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
#
# while True:
#     isTrue, frame = capture.read()
#     frame_resize = rescale(frame)
#     cv.imshow('New Video', frame_resize)
#     if cv.waitKey(5) & 0xFF == ord('d'):
#         break
# capture.release()
# capture.destroAllWindows

# Resize Images -
# import cv2 as cv
# img = cv.imread('Photos/python.jpg')
#
# width,height = 700,500
# imgnew = cv.resize(img,(width,height))
#
# cv.imshow('New',imgnew)
# print(img.shape)
# print(imgnew.shape)
#
# cv.waitKey(0)

import cv2 as cv
import numpy as np

blank = np.zeros((400, 500, 3), dtype='uint8')

blank[:] = 0, 0, 0  # B,G,R  format in Python
# #use Color Picker from Google to generate HEX code for RGB

# this generates a green box in the blue image
cv.circle(blank, radius=30, center=(250, 200), thickness=2, color=(0, 250, 0))
cv.line(blank, (250, 200), (250, 172), thickness=2, color=(0, 0, 250))  # upper
cv.line(blank, (250, 200), (272, 218), thickness=2, color=(0, 0, 250))  # right
cv.line(blank, (250, 200), (228, 218), thickness=2, color=(0, 0, 250))  # left

cv.imshow('Shapes', blank)

cv.waitKey(0)
