from tkinter import *
import webbrowser

class ViewHTML:
    def __init__(self, master):
        self.master = master
        self.window = Toplevel(master)
        self.window.title("View HTML")
        self.create_widgets()

    def create_widgets(self):
        # Create a button to open the HTML file
        self.open_button = Button(self.window, text="Open HTML", command=self.open_html)
        self.open_button.pack(pady=20)

        # Create a button to close the window
        self.close_button = Button(self.window, text="Close", command=self.window.destroy)
        self.close_button.pack(pady=20)

    def open_html(self):
        # Specify the path to the HTML file
        html_file_path = "path/to/your/html_file.html"
        webbrowser.open(html_file_path)