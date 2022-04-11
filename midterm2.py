from tkinter import *
from tkinter import ttk
win = Tk()
win.geometry("500x300+10+20")
win.title("Midterm in OOP")

# Button widgets
btn = Button(win,text = "Click to display your name", fg = "Red", bg = "White")
btn.place(x=5, y =70)

# label widget
lbl = Label(win,text = "Enter your fullname", fg = "red")
lbl.place(x=5, y = 40)

# text field
txt = Entry(win,font= ("Red", 12), bd = 5)
txt.place(x=170, y = 40)

# text field
txt = Entry(win,font= ("Red", 12), bd = 5)
txt.place(x=170, y = 70)


win.mainloop()