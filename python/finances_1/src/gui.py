from tkinter import *

def grid_configure(widget: Tk, rows: int, cols: int) -> Tk:
    pad = 20
    widget.grid_rowconfigure(0, minsize=pad)
    widget.grid_rowconfigure(rows + 1, minsize=pad)
    widget.grid_columnconfigure(0, minsize=pad)
    widget.grid_columnconfigure(cols + 1, minsize=pad)

    return widget
