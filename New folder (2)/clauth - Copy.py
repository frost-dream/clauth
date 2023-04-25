import cv2
from numpy import array
from PIL import ImageGrab
from time import time
a=cv2.VideoWriter("output.avi",cv2.VideoWriter_fourcc(*"XVID"),30,(1920,1080))
b=time()
while time()-b<3:
    a.write(cv2.cvtColor(array(ImageGrab.grab()), cv2.COLOR_BGR2RGB))
a.release()
