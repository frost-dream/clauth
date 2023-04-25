from time import time
from pyautogui import screenshot
b=0
for i in range(100):
    a=time()
    screenshot().save('file.bmp')
    b+=time()-a
print(b/100)
