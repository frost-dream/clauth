import cv2
from numpy import array
from PIL.ImageGrab import grab
from tkinter import Tk
from time import time
a=Tk()
a=cv2.VideoWriter("output.avi",cv2.VideoWriter_fourcc(*"XVID"),22,(a.winfo_screenwidth(),a.winfo_screenheight()))
b=time()
while time()-b<2:
    a.write(cv2.cvtColor(array(grab()),cv2.COLOR_BGR2RGB))
a.release()
