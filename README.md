## Computer-Vision
Computer vision is an interdisciplinary scientific field that deals with how computers can gain high-level understanding from digital images or videos.
From the perspective of engineering, it seeks to understand and automate tasks that the human visual system can do

The [`basics.py`](https://github.com/souvik0306/computer-vision/blob/master/basics.py) file contains a few rudimentary OpenCV functions to play around with like - 
- Rescaling and Resizing Images & Videos
- BGR Image to Grayscale Conversion
- Simple Shape Creation
- Edge Cascading
- Canny Image Creation
- Bluring Images & Videos

Coming to the second part of this repository, I have made a Face Detection module using the [`haar-casacdes`](https://github.com/opencv/opencv/tree/master/data/haarcascades) function. It is an Object Detection Algorithm used to identify faces in an image or a real time video. In the code I have included this feature for both [Videos](https://github.com/souvik0306/computer-vision/blob/master/Face%20Detection%20over%20Video.py) and [Images](https://github.com/souvik0306/computer-vision/blob/master/Face%20Detection%20over%20Image.py). 

As per the <a href = #Videos> tutorial</a>, the Image Code was only capable of detecting faces over a *single image* at a time, so after a bit of tweaking and scrabling through StackOverflow I devised a method to iteratre over all the images in a given folder using the [`os`](https://docs.python.org/3/library/os.html) library. 

Now the code is capable to iterating over all the images in a directory, saving a lot of time, and prints a subsequent match-percentage as well.

## For this following repository I have made use of some amazing resources - <section id="Videos">
1. OpenCV Course by freeCodeCamp.org - [YouTube](https://www.youtube.com/watch?v=oXlwWbU8l2o&ab_channel=freeCodeCamp.org)
2. OpenCV Official Documentation - [Doc](https://docs.opencv.org/4.5.3/)
3. Jason D'Souza's OpenCV Repository - [GitHub](https://github.com/jasmcaus/opencv-course)
