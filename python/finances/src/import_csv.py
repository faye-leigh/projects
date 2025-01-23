# Libraries
from csv import *
from tkcalendar import DateEntry
from tkinter import *
from tkinter import ttk, filedialog
import os
from datetime import datetime
# Config file
from config import *
# Custom classes
from data import *
from import_csv import *

def import_csv(parent: Tk, file_path: str):
    __import_paypal(file_path)

def __import_paypal(file_path: str):
    with open(file_path, flags=0, mode='r') as csv_file:
        csv_reader = DictReader(csv_file)
        for row in csv_reader:
            date = datetime.strptime(row['"Date"']).strftime('%Y-%m-%d')
            description = row['"Name"']
            amount = row['"Gross"']
            print(date, description, amount)
            # append_data(CARDS[6], [date, description, amount, '', 0, 0, 0, 0])
