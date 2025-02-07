import os
import yaml
from csv import *

from gui import *

# Load configuration
with open('src/config.yml', 'r') as config_file:
    CONFIG = yaml.safe_load(config_file)
    ACCOUNTS = CONFIG['accounts']
    CATEGORIES = CONFIG['categories']
    FORMAT = CONFIG['format']

def summary():
    """Return a summary of all transactions."""
    pass

def submit_transaction(bank: str, account: str, data: list):
    if not exists(bank, account):
        file = open_file(bank, account)
        write_header(file)
    file = append_file(bank, account)
    write_row(file, data)

def exists(bank: str, account: str) -> bool:
    """Check if a CSV file exists."""
    filepath = f'data/{bank} {account}.csv'
    return os.path.exists(filepath)

def open_file(bank: str, account: str) -> object:
    """Open a CSV file for writing."""
    filepath = f'data/{bank} {account}.csv'
    file = open(filepath, 'w') 
    return file

def append_file(bank: str, account: str) -> object:
    """Open a CSV file for writing."""
    filepath = f'data/{bank} {account}.csv'
    file = open(filepath, 'a') 
    return file

def write_header(file: object):
    """Write the header to the CSV file."""
    with file:
        writer = DictWriter(file, fieldnames=FORMAT['header'])
        writer.writeheader()

def write_row(file: object, data: list):
    """Write a row to the CSV file."""
    with file:
        writer = DictWriter(file, fieldnames=FORMAT['header'])
        row_dict = {FORMAT['header'][i]: data[i] for i in range(len(data))}
        writer.writerow(row_dict)

def list_csv_files(folder: str) -> list:
    """List all CSV files in the given folder."""
    return [f for f in os.listdir(folder) if f.endswith('.csv')]

def oliver_tab() -> float:
    """Return the total amount of money Oliver owes."""
    tab: float = 0.0
    csv_files = list_csv_files('data')
    for csv_file in csv_files:
        filepath = os.path.join('data', csv_file)
        with open(filepath, 'r') as file:
            reader = DictReader(file)
            for row in reader:
                if row['Faye'] == '1' and row['Oliver'] == '1':
                    tab += float(row['Amount']) / 2
                elif row['Oliver'] == '1':
                    tab += float(row['Amount'])
                    
    return tab

# Example usage
if __name__ == '__main__':
    print(oliver_tab())