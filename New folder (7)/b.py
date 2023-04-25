from PIL.ImageGrab import grab
from time import time,sleep
from numba import jit
from mss import mss
a=time()
mss().shot(output='file.png')
input(time()-a)
d=[]
for i in range(100):
    a=time()
    grab()
    c=time()-a
    a=time()
    jit(target_backend='cuda')
    def b():
        grab()
    b()
    d.append(time()-a<c)
print(d.count(True))
for i in range(100):
    d=0
    for i in range(100):
        a=time()
        grab()
        d+=time()-a
    print(d/100)
input()
