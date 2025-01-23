from tkinter import Tk, Label, Entry, Button, Checkbutton, IntVar, StringVar, Frame
# Config
from config import *
# Custom py files
from gui import *

class ManualEntryWindow:
    def __init__(self, master):
        self.master = master
        master.title('Manual Entry')

        master = grid_configure(master, 6, 4)

        self.date_label = Label(master, text='Date:', anchor='w')
        self.date_label.grid(row=1, column=1)
        self.date_entry = Entry(master)
        self.date_entry.grid(row=1, column=2)

        self.description_label = Label(master, text='Description:', anchor='w')
        self.description_label.grid(row=2, column=1)
        self.description_entry = Entry(master)
        self.description_entry.grid(row=2, column=2)

        self.amount_label = Label(master, text='Amount:', anchor='w')
        self.amount_label.grid(row=3, column=1)
        self.amount_entry = Entry(master)
        self.amount_entry.grid(row=3, column=2)

        self.account_label = Label(master, text='Account:', anchor='w')
        self.account_label.grid(row=4, column=1)
        self.account_entry = Entry(master)
        self.account_entry.grid(row=4, column=2)

        self.faye_var = IntVar()
        self.ollie_var = IntVar()
        self.monthly_var = IntVar()
        self.annual_var = IntVar()

        self.faye_checkbox = Checkbutton(master, text='Faye', variable=self.faye_var, anchor='w')
        self.faye_checkbox.grid(row=2, column=3)

        self.oliver_checkbox = Checkbutton(master, text='Oliver', variable=self.ollie_var, anchor='w')
        self.oliver_checkbox.grid(row=2, column=4)

        self.monthly_checkbox = Checkbutton(master, text='Monthly', variable=self.monthly_var, anchor='w')
        self.monthly_checkbox.grid(row=3, column=3)

        self.annual_checkbox = Checkbutton(master, text='Annual', variable=self.annual_var, anchor='w')
        self.annual_checkbox.grid(row=3, column=4)

        self.msg_label = Label(master, text='Message', foreground='red', anchor='w')
        self.msg_label.grid(row=5, column=1, columnspan=4)

        self.back_button = Button(master, text='Back', command=self.back, width=10)
        self.back_button.grid(row=6, column=1)

        self.submit_button = Button(master, text='Submit', command=self.submit, width=10)
        self.submit_button.grid(row=6, column=4)

    def back(self):
        self.master.destroy()  # Close the current window

    def submit(self):
        print('Submitting data')  # Placeholder for submission logic

if __name__ == '__main__':
    root = Tk()
    manual_entry_window = ManualEntryWindow(root)
    root.mainloop()