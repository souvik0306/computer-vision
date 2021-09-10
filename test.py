# import cv2 as cv
# img = cv.imread('Photos/cat.jfif')
# cv.imshow('Cat',img)
# cv.waitKey(0)


import cv2 as cv
capture = cv.VideoCapture('Photos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
capture.destroAllWindows

