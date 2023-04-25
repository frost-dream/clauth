from tkinter import Label,Tk
from PIL.ImageTk import PhotoImage
from PIL.Image import open as ope
a=Tk()
a.config(bg='green')
a.geometry('600x350+430+220')
a.title('video editor')
c=PhotoImage(ope('C:/Users/lenovo/Desktop/v.png'))
b=Label(a,image=c)
b.pack()
a.mainloop()