from PIL import ImageGrab
from threading import Thread as c
from pyautogui import screenshot
from time import time
def b():
    screenshot()
a=time()
c(target=b).start()
input(time()-a)
