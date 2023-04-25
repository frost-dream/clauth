from tkinter import Tk,VERTICAL,Label,ttk
a=Tk()
mutationslider=ttk.Scale(a, from_=0, to=1000, orient=VERTICAL,length=200, value=100, style="custom.Horizontal.TScale")
mutationslider.grid(row=1, column=1)
mutationlabel=Label(a, font=("Helvetica", 11, "bold"), bg='#0000b3', fg="white")
mutationlabel.grid(row=2, column=1)
