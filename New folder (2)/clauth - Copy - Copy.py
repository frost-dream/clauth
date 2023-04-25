import win32gui
import win32ui
import win32con
from time import time
e=[]
f=time()
for i in range(35):
    a=time()
    b=win32ui.CreateDCFromHandle(win32gui.GetWindowDC(win32gui.FindWindow(None, 'example')))
    c=b.CreateCompatibleDC()
    d = win32ui.CreateBitmap()
    d.CreateCompatibleBitmap(b, 1920, 1080)
    c.SelectObject(d)
    c.BitBlt((0,0),(1920, 1080) , b, (0,0), win32con.SRCCOPY)
    d.SaveBitmapFile(c, 'file.bmp')
    e.append(time()-a)
print(time()-f)
e.sort()
input(e)
