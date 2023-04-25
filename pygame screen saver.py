from pygame import draw,init,display,FULLSCREEN
from random import randint 
init()
a=display.set_mode((1920,1080),FULLSCREEN)
while True:
    sleep(.001)
    a.fill((0,0,0))
    draw.rect(a,(255,0,0),(randint(0,1920),randint(0,1080),randint(0,30),randint(0,30)))
    draw.rect(a,(0,0,255),(randint(0,1920),randint(0,1080),randint(0,30),randint(0,30)))
    draw.rect(a,(0,255,0),(randint(0,1920),randint(0,1080),randint(0,30),randint(0,30)))
    display.update()
