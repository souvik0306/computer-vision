import numpy as np
import cv2 as cv
import os
from pathlib import Path

# A loop to Open all the images in a folder 
p = Path(r'D:\computer-vision\Photos\Faces\val\ben_afflek')
for filepath in p.glob('*.jpg'):
    img = cv.imread(os.path.join(p, filepath))
    cv.imshow('Photos', img)
    cv.waitKey(0)