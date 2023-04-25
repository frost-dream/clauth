from turtle import *
from random import randint,choice
from threading import Timer
from time import time
speed(0)
colormode(255)
setup(width=1.0,height=1.0)
getcanvas().winfo_toplevel().overrideredirect(1)
hideturtle()
bgcolor('black')
b=time()
while True:
    if time()-b>10:
        clear()
        b=time()
    pensize(randint(0,30))
    color(randint(0,255),randint(0,255),randint(0,255))
    begin_fill()
    a=choice(['s','t','c'])
    if a=='c':
        circle(randint(0,30))
    elif a=='t':
        fd(30)
        right(120)
        fd(30)
        right(120)
        fd(30)
    else:
        fd(40)
        right(90)
        fd(40)
        right(90)
        fd(40)
        right(90)
        fd(40)
    if randint(0,1):
        end_fill()
    penup()
    goto(randint(-960,960),randint(-540,540))
    pendown()
