# Python GUI Application

This project is a Python GUI application that allows users to manage financial data through various interfaces. Users can import CSV files, enter data manually, fix incomplete data, and view data in HTML format.

## Project Structure

```
python-gui-app
├── src
│   ├── main.py                  # Entry point of the application
│   ├── import_window.py         # GUI for importing CSV files
│   ├── manual_entry_window.py    # GUI for manual data entry
│   ├── fix_data_window.py       # GUI for fixing incomplete data
│   ├── view_html.py             # Functionality to view HTML data
│   └── utils
│       └── __init__.py          # Utility functions and classes
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/python-gui-app.git
   cd python-gui-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Features

- **Import CSV**: Select an account and import CSV files.
- **Manual Entry**: Enter financial data manually with various options.
- **Fix Data**: Edit and fix incomplete data entries.
- **View HTML**: Open an HTML file to view data tables and graphs.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.