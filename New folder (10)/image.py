from PIL import Image
from PIL.ImageGrab import grab
a=grab()
b=a.load()
for i in range(a.size[0]):
    for j in range(a.size[1]):
        if b[i,j][0]>100:
            b[i,j]=(0,0,0)
a.save('file.png')
