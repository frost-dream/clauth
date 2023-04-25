from time import time
from os import chdir
from pyautogui import screenshot
from PIL import ImageGrab
from threading import Thread
chdir('c:/users/lenovo/desktop')
def b():
    screenshot().save("hoy3.jpg")
c=0
a=time()
while time()-a<1:
    s=Thread(target=b)
    s.start()
    c+=1
input((time()-a,c))

def b():
    ImageGrab.grab().save("hoy3.jpg")
c=0
a=time()
while time()-a<1:
    s=Thread(target=b)
    s.start()
    c+=1
input((time()-a,c))
