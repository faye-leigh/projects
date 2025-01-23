from tkinter import *
from tkinter import filedialog, messagebox
from tkcalendar import DateEntry
from csv import reader, writer
import os

# Constants for file paths and CSV fields
FIELDS = ['Date', 'Description', 'Amount', 'Category']
CREDIT_CARDS = ["Apple", "Chase", "Citi", "Discover", "PayPal", "Synchrony", "Venmo"]
BANK_ACCOUNTS = ["Discover Checking", "Discover Savings", "Chase Checking"]
DATA_FILE_LOCATION = ".data/"

# Ensure the data directory exists
os.makedirs(DATA_FILE_LOCATION, exist_ok=True)

# Function to get the data file name based on the selected credit card
def get_data_file_name(credit_card):
    return os.path.join(DATA_FILE_LOCATION, f"{credit_card.lower().replace(' ', '_')}.csv")

# Function to import CSV file
def import_csv():
    # Open file dialog to select CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"),("CSV files", "*.CSV")])
    if file_path:
        with open(file_path, 'r') as import_file:
            csv_reader = reader(import_file)
            next(csv_reader)  # Skip the header line
            data = []
            for row in csv_reader:
                # Process the row based on the selected bank
                if bank_var.get() == "Bank A":
                    row.pop(0)
                    row.pop(3)
                    row.pop(3)
                elif bank_var.get() == "Bank B":
                    row.pop(1)
                    row.pop(2)
                data.append(row)
            # Append the processed data to the data file
            data_file_name = get_data_file_name(bank_var.get())
            file_exists = os.path.isfile(data_file_name)
            with open(data_file_name, 'a', newline='') as data_file:
                csv_writer = writer(data_file)
                if not file_exists:
                    csv_writer.writerow(FIELDS)  # Write header if file does not exist
                csv_writer.writerows(data)
            # Show success message
            messagebox.showinfo("Success", "CSV imported successfully")

# Function to manually enter data
def manual_entry():
    def save_manual_entry():
        date = entry_date.get()
        description = entry_description.get()
        amount = entry_amount.get()
        category = entry_category.get()
        bank = bank_var_manual.get()
        if date and description and amount and category and bank != "Select Bank":
            data_file_name = get_data_file_name(bank)
            file_exists = os.path.isfile(data_file_name)
            with open(data_file_name, 'a', newline='') as data_file:
                csv_writer = writer(data_file)
                if not file_exists:
                    csv_writer.writerow(FIELDS)  # Write header if file does not exist
                csv_writer.writerow([date, description, amount, category])
            # Show success message
            msg_label.config(text="Data saved successfully")
            # Clear the input fields except bank and date
            entry_description.delete(0, END)
            entry_amount.delete(0, END)
            entry_category.delete(0, END)
            # msg_label.config(text="")  # Clear any previous error message
        else:
            msg_label.config(text="All fields are required")

    manual_entry_window = Toplevel(root)
    manual_entry_window.title("Manual Data Entry")
    manual_entry_window.geometry("400x350")  # Set the window size

    Label(manual_entry_window, text="Date", anchor="w").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_date = DateEntry(manual_entry_window, date_pattern='yyyy-mm-dd')
    entry_date.grid(row=0, column=1, padx=10, pady=5)

    Label(manual_entry_window, text="Description", anchor="w").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_description = Entry(manual_entry_window)
    entry_description.grid(row=1, column=1, padx=10, pady=5)

    Label(manual_entry_window, text="Amount", anchor="w").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_amount = Entry(manual_entry_window)
    entry_amount.grid(row=2, column=1, padx=10, pady=5)

    Label(manual_entry_window, text="Category", anchor="w").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_category = Entry(manual_entry_window)
    entry_category.grid(row=3, column=1, padx=10, pady=5)

    Label(manual_entry_window, text="Bank", anchor="w").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    bank_var_manual = StringVar(manual_entry_window)
    bank_var_manual.set("Select Bank")  # Default value
    bank_menu_manual = OptionMenu(manual_entry_window, bank_var_manual, *CREDIT_CARDS)
    bank_menu_manual.grid(row=4, column=1, padx=10, pady=5)

    msg_label = Label(manual_entry_window, text="", fg="red")
    msg_label.grid(row=5, column=0, columnspan=2, pady=5)

    Button(manual_entry_window, text="Save", command=save_manual_entry).grid(row=6, column=0, padx=10, pady=10, sticky="ew")
    Button(manual_entry_window, text="Close", command=manual_entry_window.destroy).grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    manual_entry_window.grid_columnconfigure(0, weight=1)
    manual_entry_window.grid_columnconfigure(1, weight=1)

# Placeholder function to open HTML (to be implemented)
def open_html():
    pass

# Function to close the application
def close():
    root.destroy()

# GUI Setup
root = Tk()
root.title("Finance Manager")
root.geometry("600x400")  # Set the main window size

# Dropdown menu for selecting bank
bank_var = StringVar(root)
bank_var.set("Select Bank")  # Default value
bank_menu = OptionMenu(root, bank_var, *CREDIT_CARDS)
bank_menu.pack(padx=20, pady=10)

# Buttons for the GUI
btn_import = Button(root, text="Import CSV", command=import_csv)
btn_import.pack(padx=20, pady=10)

btn_manual_entry = Button(root, text="Manual Entry", command=manual_entry)
btn_manual_entry.pack(padx=20, pady=10)

btn_open_html = Button(root, text="Open HTML", command=open_html)
btn_open_html.pack(padx=20, pady=10)

btn_close = Button(root, text="Close", command=close)
btn_close.pack(padx=20, pady=10)

# Start the Tkinter event loop
root.mainloop()


