from tkinter import *

def grid_config(root: Tk, rows: int, columns: int) -> Tk:
    for i in range(rows+2):
        root.grid_rowconfigure(i, minsize=24)
    for i in range(columns+2):
        root.grid_columnconfigure(i, minsize=24)
    return root