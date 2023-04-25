from time import time
from win32gui import GetWindowDC,FindWindow
from win32ui import CreateDCFromHandle,CreateBitmap
from win32con import SRCCOPY
a=time()
b=CreateDCFromHandle(GetWindowDC(FindWindow(None, 'none')))
c=b.CreateCompatibleDC()
d=CreateBitmap()
d.CreateCompatibleBitmap(b, 1920, 1080)
c.SelectObject(d)
c.BitBlt((0,0),(1920,1080),b,(0,0),SRCCOPY)
d.SaveBitmapFile(c,'file.bmp')
print(time()-a)
