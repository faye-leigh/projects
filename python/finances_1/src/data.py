import os
import glob
from csv import *

def append_data(bank: str, account: str, date: str, description: str, amount: float, faye: int, oliver: int, monthly: int, annual: int, category: str) -> None:
    """
    Append the data to the CSV file.
    """
    file_path = 'bin/' + bank + '.csv'
    file_exists = os.path.isfile(file_path)

    with open(file_path, 'a') as file:
        if not file_exists:
            file.write('Account,Date,Description,Amount,Faye,Oliver,Monthly,Annual,Category\n')
        file.write(f'{account},{date},{description},{amount},{faye},{oliver},{monthly},{annual},{category}\n')

def fix_date(date: str) -> str:
    """
    Fix the date format from dd/mm/yyyy to yyyy-mm-dd.
    """
    if date[4] == '-':
        return date
    return date[-4:] + '-' + date[3:5] + '-' + date[:2]

def read_all_csv_files(folder_path: str) -> None:
    """
    Read all CSV files in the specified folder.
    """
    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
    for file_path in csv_files:
        with open(file_path, 'r') as file:
            print(f'Reading file: {file_path}')
            print(file.read())