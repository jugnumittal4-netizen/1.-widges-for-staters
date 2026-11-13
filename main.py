from tkinter import *
root  = Tk()
root.title("My First GUI")
root.geometry("400x300")
root.mainloop()



lbl = Label(pady = 30,text = "Welcome to my site", fg = "white", bg = "black", font = ("Arial Bold", 50), height = 1, width = 300)
def display():
    
   
    text_box.insert(END, "Welcome to my site")
    text_box.insert(END, "This is a simple GUI application built using Tkinter.")
text_box = Text(height = 3)
Btn = Button(text = "Click Me!", command = display, bg = "#3895D3", fg = "white",height = 1)
lbl.pack()
text_box.pack()
Btn.pack()
root.mainloop()

