from tkinter import *
import os

root = Tk()
root.title("bonito")
root.iconbitmap("py.ico")
root.resizable(1,1)
root.geometry("600x300")
root.config(bg="green")

frame = Frame(root)
frame.pack()
frame.config(bg="blue")
frame.config(width=400, height=250)
frame.config(cursor="pirate")
#frame.config(relief="groove")
#frame.config(bd=35)
frame.config(relief="sunken")
frame.config(bd=35)

frame.pack(
    side=RIGHT,
    anchor=S,
)

frame.pack(
#    fill="y"
    fill="both"
)








root.mainloop() 