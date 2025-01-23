from tkinter import Tk, Label, Button, StringVar, OptionMenu, filedialog, Toplevel, Frame
from config import ACCOUNTS

class ImportWindow:
    def __init__(self, master):
        self.master = master
        master.title('Import CSV')

        self.account_var = StringVar(master)
        self.account_var.set('Select Account')  # default value

        # Flatten the ACCOUNTS dictionary for the OptionMenu
        account_options = [f'{bank} -> {account}' for bank, accounts in ACCOUNTS.items() for account in accounts]
        self.account_menu = OptionMenu(master, self.account_var, *account_options)
        self.account_menu.config(width=20)
        self.account_menu.pack(padx=20, pady=(20, 0))

        self.file_button = Button(master, text='Select CSV File', command=self.select_file, width=20)
        self.file_button.pack()

        self.file_path_label = Label(master, text='', padx=20)
        self.file_path_label.pack()

        # Frame to contain the Back and Submit buttons
        self.button_frame = Frame(master)
        self.button_frame.pack(pady=(20, 0))

        self.back_button = Button(self.button_frame, text='Back', command=self.back, width=10)
        self.back_button.pack(side='left', padx=(0, 10))

        self.submit_button = Button(self.button_frame, text='Submit', command=self.submit, width=10)
        self.submit_button.pack(side='left')

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv'), ('CSV files', '*.CSV'), ('All files', '*.*')], parent=self.master)
        if file_path:
            self.file_path_label.config(text=f'Selected file: {file_path}')

    def back(self):
        print('Going back to the main window')  # Placeholder for navigation logic
        self.master.destroy()

    def submit(self):
        print(f'Submitting data for account: {self.account_var.get()}')  # Placeholder for submission logic
