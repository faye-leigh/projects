import tkinter as tk
from tkinter import messagebox

from gui import *
from add_window import *

def open_view_window():
    messagebox.showinfo("View", "Open View Window")

def open_summary_window():
    messagebox.showinfo("Summary", "Open Summary Window")

def open_update_window():
    messagebox.showinfo("Update", "Open Update Window")

def open_delete_window():
    messagebox.showinfo("Delete", "Open Delete Window")

def quit_program():
    root.quit()

root = tk.Tk()
root.title("Finance Manager")

# Create buttons
btn_add = tk.Button(root, text="Add", command=open_add_window, width=12)
btn_view = tk.Button(root, text="View", command=open_view_window, width=12)
btn_summary = tk.Button(root, text="Summary", command=open_summary_window, width=12)
btn_update = tk.Button(root, text="Update", command=open_update_window, width=12)
btn_delete = tk.Button(root, text="Delete", command=open_delete_window, width=12)
btn_quit = tk.Button(root, text="Quit", command=quit_program, width=12)

# Place buttons on the window
root = grid_config(root, 5, 2)

btn_add.grid(row=1, column=1)
btn_update.grid(row=1, column=2)
btn_view.grid(row=2, column=1)
btn_delete.grid(row=2, column=2)
btn_summary.grid(row=3, column=1, columnspan=2)
btn_quit.grid(row=5, column=1, columnspan=2)

root.mainloop()
