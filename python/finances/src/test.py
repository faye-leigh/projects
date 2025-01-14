from tkinter import *

root = Tk()
root.grid_columnconfigure(0, minsize=48)
root.grid_rowconfigure(0, minsize=48)
frame = Frame(root,width=32, height=32, background='green')
frame.grid(row=0, column=0)
root.mainloop()
