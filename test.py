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

# import cv2 as cv
# import numpy as np
#
# blank = np.zeros((400, 500, 3), dtype='uint8')
#
# blank[:] = 0, 0, 0  # B,G,R  format in Python
# # #use Color Picker from Google to generate HEX code for RGB
#
# # this generates a green box in the blue image
# # creates a similar looking Mercedes Symbol
# cv.circle(blank, radius=30, center=(250, 200), thickness=2, color=(0, 250, 0))
# cv.line(blank, (250, 200), (250, 172), thickness=2, color=(0, 0, 250))  # upper
# cv.line(blank, (250, 200), (272, 218), thickness=2, color=(0, 0, 250))  # right
# cv.line(blank, (250, 200), (228, 218), thickness=2, color=(0, 0, 250))  # left
#
#
# cv.imshow('Benz', blank)
#
# cv.waitKey(0)

# import cv2 as cv
# import numpy as np

# # converting an image to grayscale

# img = cv.imread(r'D:/computer-vision/Photos/python.jpg')
# # cv.imshow('Img', img)
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)
# cv.waitKey(0)

# import cv2 as cv
# import numpy as np
# # Blur
# img = cv.imread(r'D:/computer-vision/Photos/python.jpg')
# #Gaussian Blurring Technique
# blur = cv.GaussianBlur(img,(41,41),cv.BORDER_DEFAULT) # to increase the blurriness, we need to increase the kernel size
# cv.imshow('Blur',blur)
# cv.imshow('Normal',img)
# cv.waitKey(0)

# #Edge cascasde
# import cv2 as cv
# import numpy as np
# img = cv.imread(r'D:/computer-vision/Photos/village.jpg')
# img2 = cv.imread(r'D:/computer-vision/Photos/village2.jpg')

# width,height = 600,500
# imgnew = cv.resize(img,(width,height))
# imgnew2 = cv.resize(img2,(width,height))

# cany = cv.Canny(imgnew,250,250)
# cany2 = cv.Canny(imgnew2,300,300)

# Hori = np.concatenate((cany,cany2),axis=1)
# cv.imshow('Horizontal Concatenation',Hori)
# cv.waitKey(0)

# import cv2 as cv
# import numpy as np
# img = cv.imread(r'D:/computer-vision/Photos/village.jpg')
# img2 = cv.imread(r'D:/computer-vision/Photos/village2.jpg')

# width,height = 600,500
# imgnew = cv.resize(img,(width,height))

# cany = cv.Canny(imgnew,250,250)

# cv.waitKey(0)

# import cv2 as cv
# capture = cv.VideoCapture(0)
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
#     if cv.waitKey(5) & 0xFF == ord('d'):  #d is the kill swich here
#         break
# capture.release()
# capture.destroAllWindows

# # Edge cascading on a blurred image
# import cv2 as cv
# import numpy as np
# img = cv.imread(r'D:/computer-vision/Photos/boston.jpg')

# width,height = 600,500
# imgnew = cv.resize(img,(width,height))
# blur = cv.GaussianBlur(imgnew,(7,7),cv.BORDER_DEFAULT)
# cany = cv.Canny(blur,100,100)
# cv.imshow('Boston',cany)
# cv.waitKey(0)

#Dialate a image
# import cv2 as cv
# import numpy as np
# img = cv.imread(r'D:/computer-vision/Photos/boston.jpg')
# width,height = 600,500
# img = cv.resize(img,(width,height))
# cany = cv.Canny(img,100,100)
# dilated = cv.dilate(cany,(50,50),iterations=1)
# cv.imshow('Boston',dilated)
# cv.waitKey(0)

#Taking a video as canny, dilated and blurred
import cv2 as cv
import numpy as np
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    blur = cv.GaussianBlur(frame,(7,7),cv.BORDER_DEFAULT)
    cany = cv.Canny(blur,100,100)
    cv.imshow('Video', cany)
    if cv.waitKey(5) & 0xFF == ord('d'):  #d is the kill swich here
        break
capture.release()
capture.destroAllWindows