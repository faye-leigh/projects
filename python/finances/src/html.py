import webbrowser
import os

def open_html(html_file_name):
    """
    Opens the specified HTML file in the default web browser.

    Args:
        html_file_name (str): The name of the HTML file.
    """
    # Construct the path to the HTML file relative to the current file
    file_path = os.path.join(os.path.dirname(__file__), 'bin/', html_file_name)

    # Open the HTML file in the default web browser
    webbrowser.open('file://' + file_path)

def create_html(csv_file_path):
    pass

open_html('test.html')
