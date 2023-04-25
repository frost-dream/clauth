"{60254CA5-953B-11CF-8C96-00AA00B8708C}"
from sys import argv
from time import sleep
from tkinter import Tk,Button
a=Tk()
def c():
    print(argv)
b=Button(a,text='lessgo',command=c)
b.pack()
a.mainloop()
