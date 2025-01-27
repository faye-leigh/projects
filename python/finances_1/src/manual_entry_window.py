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

        self.date_label = Label(master, text='Date:')
        self.date_label.grid(row=1, column=1, sticky='w')
        self.date_entry = Entry(master)
        self.date_entry.grid(row=1, column=2)

        self.description_label = Label(master, text='Description:')
        self.description_label.grid(row=2, column=1, sticky='w')
        self.description_entry = Entry(master)
        self.description_entry.grid(row=2, column=2)

        self.amount_label = Label(master, text='Amount:')
        self.amount_label.grid(row=3, column=1, sticky='w')
        self.amount_entry = Entry(master)
        self.amount_entry.grid(row=3, column=2)

        self.account_label = Label(master, text='Account:')
        self.account_label.grid(row=4, column=1, sticky='w')
        self.account_entry = Entry(master)
        self.account_entry.grid(row=4, column=2)

        self.faye_var = IntVar()
        self.oliver_var = IntVar()
        self.monthly_var = IntVar()
        self.annual_var = IntVar()

        self.faye_checkbox = Checkbutton(master, text='Faye', variable=self.faye_var)
        self.faye_checkbox.grid(row=2, column=3, sticky='w')

        self.oliver_checkbox = Checkbutton(master, text='Oliver', variable=self.oliver_var)
        self.oliver_checkbox.grid(row=2, column=4, sticky='w')

        self.monthly_checkbox = Checkbutton(master, text='Monthly', variable=self.monthly_var)
        self.monthly_checkbox.grid(row=3, column=3, sticky='w')

        self.annual_checkbox = Checkbutton(master, text='Annual', variable=self.annual_var)
        self.annual_checkbox.grid(row=3, column=4, sticky='w')

        self.msg_label = Label(master, text='', foreground='red')
        self.msg_label.grid(row=5, column=1, columnspan=4)

        self.back_button = Button(master, text='Back', command=self.back, width=10)
        self.back_button.grid(row=6, column=1)

        self.submit_button = Button(master, text='Submit', command=self.submit, width=10)
        self.submit_button.grid(row=6, column=4)

    def getEntries(self):
        return {
            'date': self.date_entry.get(),
            'description': self.description_entry.get(),
            'amount': self.amount_entry.get(),
            'account': self.account_entry.get(),
            'faye': self.faye_var.get(),
            'oliver': self.oliver_var.get(),
            'monthly': self.monthly_var.get(),
            'annual': self.annual_var.get()
        }
    
    def back(self):
        self.master.destroy()  # Close the current window

    def submit(self):
        print(getEntries(self))  # Placeholder for submission logic
    

if __name__ == '__main__':
    root = Tk()
    manual_entry_window = ManualEntryWindow(root)
    root.mainloop()