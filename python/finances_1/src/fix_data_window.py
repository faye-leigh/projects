from tkinter import Tk, Label, Entry, Button, Checkbutton, IntVar, StringVar, Frame
from tkinter import ttk
import yaml
from tkcalendar import DateEntry
# Custom classes
from data import *
from gui import *

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)
    ACCOUNTS = config['accounts']
    CATEGORIES = config['categories']

class FixDataWindow:
    def __init__(self, main):
        self.main = main
        main.title('Manual Entry')

        main = grid_configure(main, 7, 4)

        self.date_label = Label(main, text='Date')
        self.date_label.grid(row=1, column=1, sticky='w')
        self.date_entry = DateEntry(main, width=23, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=1, column=2, sticky='e')

        self.description_label = Label(main, text='Description')
        self.description_label.grid(row=2, column=1, sticky='w')
        self.description_entry = Entry(main, width=24)
        self.description_entry.grid(row=2, column=2, sticky='e')

        self.amount_label = Label(main, text='Amount')
        self.amount_label.grid(row=3, column=1, sticky='w')
        self.amount_entry = Entry(main, width=24)
        self.amount_entry.grid(row=3, column=2, sticky='e')

        self.category_label = Label(main, text='Category')
        self.category_label.grid(row=4, column=1, sticky='w')

        # Create a combo dropdown box for categories
        self.category_var = StringVar()
        self.category_combobox = ttk.Combobox(main, textvariable=self.category_var, width=23)
        self.category_combobox['values'] = CATEGORIES
        self.category_combobox.grid(row=4, column=2, sticky='e')

        self.account_label = Label(main, text='Account')
        self.account_label.grid(row=5, column=1, sticky='w')
        
        # Create a combo dropdown box for accounts
        self.account_var = StringVar()
        self.account_combobox = ttk.Combobox(main, textvariable=self.account_var, width=23)
        self.account_combobox['values'] = [f'{bank} {account}' for bank, accounts in ACCOUNTS.items() for account in accounts]
        self.account_combobox.grid(row=5, column=2, sticky='e')

        self.faye_var = IntVar()
        self.oliver_var = IntVar()
        self.monthly_var = IntVar()
        self.annual_var = IntVar()

        self.faye_checkbox = Checkbutton(main, text='Faye', variable=self.faye_var)
        self.faye_checkbox.grid(row=2, column=3, sticky='w')

        self.oliver_checkbox = Checkbutton(main, text='Oliver', variable=self.oliver_var)
        self.oliver_checkbox.grid(row=2, column=4, sticky='w')

        self.monthly_checkbox = Checkbutton(main, text='Monthly', variable=self.monthly_var)
        self.monthly_checkbox.grid(row=3, column=3, sticky='w')

        self.annual_checkbox = Checkbutton(main, text='Annual', variable=self.annual_var)
        self.annual_checkbox.grid(row=3, column=4, sticky='w')

        self.msg_label = Label(main, text='', foreground='red')
        self.msg_label.grid(row=6, column=1, columnspan=4)

        self.back_button = Button(main, text='Back', command=self.back, width=10)
        self.back_button.grid(row=7, column=1)

        self.submit_button = Button(main, text='Submit', command=self.submit, width=10)
        self.submit_button.grid(row=7, column=4)
    
    def back(self):
        self.main.destroy()  # Close the current window

    def submit(self):
        append_data(
            self.account_var.get().split(' ')[0],
            self.account_var.get().split(' ')[1],
            self.date_entry.get(),
            self.description_entry.get(),
            self.amount_entry.get(),
            self.faye_var.get(),
            self.oliver_var.get(),
            self.monthly_var.get(),
            self.annual_var.get(),
            self.category_var.get()
        )

if __name__ == '__main__':
    root = Tk()
    manual_entry_window = FixDataWindow(root)
    root.mainloop()