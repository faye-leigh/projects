from tkinter import Tk, Label, Entry, Button, Checkbutton, IntVar, StringVar

class FixDataWindow:
    def __init__(self, master, incomplete_data):
        self.master = master
        self.master.title("Fix Data")

        self.date_var = StringVar(value=incomplete_data.get('date', ''))
        self.description_var = StringVar(value=incomplete_data.get('description', ''))
        self.amount_var = StringVar(value=incomplete_data.get('amount', ''))
        self.account_var = StringVar(value=incomplete_data.get('account', ''))

        self.faye_var = IntVar(value=1 if incomplete_data.get('faye', False) else 0)
        self.ollie_var = IntVar(value=1 if incomplete_data.get('ollie', False) else 0)
        self.monthly_var = IntVar(value=1 if incomplete_data.get('monthly', False) else 0)
        self.annual_var = IntVar(value=1 if incomplete_data.get('annual', False) else 0)

        Label(master, text="Date").grid(row=0)
        Entry(master, textvariable=self.date_var).grid(row=0, column=1)

        Label(master, text="Description").grid(row=1)
        Entry(master, textvariable=self.description_var).grid(row=1, column=1)

        Label(master, text="Amount").grid(row=2)
        Entry(master, textvariable=self.amount_var).grid(row=2, column=1)

        Label(master, text="Account").grid(row=3)
        Entry(master, textvariable=self.account_var).grid(row=3, column=1)

        Checkbutton(master, text="Faye", variable=self.faye_var).grid(row=4, column=0)
        Checkbutton(master, text="Ollie", variable=self.ollie_var).grid(row=4, column=1)
        Checkbutton(master, text="Monthly", variable=self.monthly_var).grid(row=5, column=0)
        Checkbutton(master, text="Annual", variable=self.annual_var).grid(row=5, column=1)

        Button(master, text="Back", command=self.master.destroy).grid(row=6, column=0)
        Button(master, text="Submit", command=self.submit_data).grid(row=6, column=1)

    def submit_data(self):
        # Logic to handle the submission of fixed data
        fixed_data = {
            'date': self.date_var.get(),
            'description': self.description_var.get(),
            'amount': self.amount_var.get(),
            'account': self.account_var.get(),
            'faye': bool(self.faye_var.get()),
            'ollie': bool(self.ollie_var.get()),
            'monthly': bool(self.monthly_var.get()),
            'annual': bool(self.annual_var.get()),
        }
        print(fixed_data)  # Replace with actual submission logic
        self.master.destroy()