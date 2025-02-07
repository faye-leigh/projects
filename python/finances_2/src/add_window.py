import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import yaml

from gui import *
from data import submit_transaction

def open_add_window():
    add_window = tk.Toplevel()
    add_window.title('Add Transaction')

    add_window = grid_config(add_window, 10, 3)

    # Load configuration
    with open('src/config.yml', 'r') as file:
        config = yaml.safe_load(file)
        accounts = config['accounts']
        categories = config['categories']

    # Date picker
    tk.Label(add_window, text='Date', width=12, anchor='w').grid(row=1, column=1, sticky='w')
    date_entry = DateEntry(add_window, width=12, date_pattern='yyyy-mm-dd')
    date_entry.grid(row=1, column=2, sticky='w', columnspan=2)

    # Description
    tk.Label(add_window, text='Description').grid(row=2, column=1, sticky='w')
    description_entry = tk.Entry(add_window, width=24)
    description_entry.grid(row=2, column=2, sticky='w', columnspan=2)

    # Amount
    tk.Label(add_window, text='Amount').grid(row=3, column=1, sticky='w')
    amount_entry = tk.Entry(add_window, width=12)
    amount_entry.grid(row=3, column=2, sticky='w', columnspan=2)

    # Category combobox
    tk.Label(add_window, text='Category').grid(row=4, column=1, sticky='w')
    category_var = tk.StringVar()
    category_combobox = ttk.Combobox(add_window, textvariable=category_var, values=categories, width=12)
    category_combobox.grid(row=4, column=2, sticky='w', columnspan=2)

    # Bank combobox
    tk.Label(add_window, text='Bank').grid(row=5, column=1, sticky='w')
    bank_var = tk.StringVar()
    bank_combobox = ttk.Combobox(add_window, textvariable=bank_var, values=list(accounts.keys()), width=12)
    bank_combobox.grid(row=5, column=2, sticky='w', columnspan=2)

    # Account combobox
    tk.Label(add_window, text='Account').grid(row=6, column=1, sticky='w')
    account_var = tk.StringVar()
    account_combobox = ttk.Combobox(add_window, textvariable=account_var, values=[], width=12)
    account_combobox.grid(row=6, column=2, sticky='w', columnspan=2)

    # Update account options based on selected bank
    def update_account_options(*args):
        selected_bank = bank_var.get()
        if selected_bank in accounts:
            account_combobox['values'] = accounts[selected_bank]
        else:
            account_combobox['values'] = []

    bank_var.trace_add('write', update_account_options)

    # Checkboxes
    faye_var = tk.IntVar()
    oliver_var = tk.IntVar()
    monthly_var = tk.IntVar()
    annual_var = tk.IntVar()

    tk.Checkbutton(add_window, text='Faye', variable=faye_var).grid(row=7, column=2, sticky='w')
    tk.Checkbutton(add_window, text='Oliver', variable=oliver_var).grid(row=7, column=3, sticky='w')
    tk.Checkbutton(add_window, text='Monthly', variable=monthly_var).grid(row=8, column=2, sticky='w')
    tk.Checkbutton(add_window, text='Annual', variable=annual_var).grid(row=8, column=3, sticky='w')

    # Message line
    msg_line = tk.Label(add_window, text='', fg='red')
    msg_line.grid(row=9, column=1, columnspan=3)

    # Validation function
    def validate_and_submit():
        if not date_entry.get_date() or not description_entry.get() or not amount_entry.get() or not category_var.get() or not bank_var.get() or not account_var.get() or not (faye_var.get() or oliver_var.get()):
            msg_line.config(text='All fields except Monthly and Annual are required.')
        else:
            submit_transaction(
                bank_var.get(),
                account_var.get(),
                [
                    date_entry.get_date(),
                    description_entry.get(),
                    amount_entry.get(),
                    category_var.get(),
                    faye_var.get(),
                    oliver_var.get(),
                    monthly_var.get(),
                    annual_var.get()
                ]
            )
            msg_line.config(text='Transaction submitted successfully.', fg='green')
            date_entry.delete(0, 'end')
            description_entry.delete(0, 'end')
            amount_entry.delete(0, 'end')
            category_combobox.set('')
            faye_var.set(0)
            oliver_var.set(0)
            monthly_var.set(0)
            annual_var.set(0)

    # Submit button
    submit_button = tk.Button(add_window, text='Submit', command=validate_and_submit, width=8)
    submit_button.grid(row=10, column=3, sticky='e')

    # Back button
    back_button = tk.Button(add_window, text='Back', command=add_window.destroy, width=8)
    back_button.grid(row=10, column=1, sticky='w')

# Example usage
if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    open_add_window()
    root.mainloop()