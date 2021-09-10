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

import cv2 as cv
capture = cv.VideoCapture('Photos/dog.mp4')

def rescale(frame,scale=0.50):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()
    frame_resize = rescale(frame)
    cv.imshow('Video', frame_resize)
    if cv.waitKey(5) & 0xFF == ord('d'):
        break
capture.release()
capture.destroAllWindows