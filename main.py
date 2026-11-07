from tkinter import *
from datetime import date

root= Tk()
root.title("My First GUI")
root.geometry("400x300")
lbl = Label(text = "Hi There!", fg = "white", bg = "black", font = ("Arial Bold", 50), height = 1, width = 300)
name_lbl = Label(text = "Full Name", bg = "#3895D3")
name_entry = Entry()
def display():
    name = name_entry.get()
    global message
    message = "Welcome To Application /n and Today's Date Is:"
    greet = "hello " + name + "!"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box = Text(height = 3)
btn = Button(text = "Click Me!", command = display, bg = "#3895D3", fg = "white",height = 1)

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()
