import string
from tkinter import mainloop
from tinkter import *
from tinkter.ttk import *


from time import strftime


root = Tk()

root.title("Matheros Clock")


def  time():
    string = strftime('%H:%M %p')

    label.config(text = string)


label.after(1000, time)


label = Label(root, font("Azonix", 80), background = "light blue", foreground = "red" )


label.pack(anchor = 'center')
time()

mainloop()
