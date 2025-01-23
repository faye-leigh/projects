# Libraries
from csv import *
from tkcalendar import DateEntry
from tkinter import *
from tkinter import ttk, filedialog
from os import *
# Config file
from config import *
# Custom classes
from data import *
from import_csv import *

CSV_DIR = 'bin/data'

def create_csv(file_path: str):
    """
    Creates a new CSV file with the specified file path.

    Args:
        file_path (str): The path to the CSV file to create.
    """
    # Ensure the CSV_DIR directory exists
    makedirs(CSV_DIR, exist_ok=True)

    # Create and write to the CSV file
    with open(file_path, mode='w', newline='') as new_csv:
        csv_writer = writer(new_csv)
        csv_writer.writerow(FIELDS)

def append_data(account: str, data: list):
    """
    Appends data to the specified account's CSV file. Creates the file if it does not exist.

    Args:
        account (str): The account name used to construct the CSV file name.
        data (list): The data to append to the CSV file.
    """
    # Construct the full path to the CSV file
    file_path = path.join(path.dirname(__file__), CSV_DIR, account + '.csv')
    
    # Write to CSV file, create if necessary
    file_exists = path.isfile(file_path)
    if not file_exists:
        create_csv(file_path)
    with open(file_path, mode='a', newline='') as csv:
        csv_writer = writer(csv)
        csv_writer.writerow(data)

def __get_csv_files():
    """"""
    csv_files = list()
    for file_name in listdir(path.join(path.dirname(__file__), CSV_DIR)):
        if file_name.endswith('.csv'):
            csv_files.append(file_name)
            print(file_name)

    return csv_files

def __fix_data(parent: Tk):
    with parent:
        print()

# Example usage
# get_csv_files()

