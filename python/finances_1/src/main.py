from tkinter import Tk, Button, Frame, Toplevel
from import_window import ImportWindow
from manual_entry_window import ManualEntryWindow
from fix_data_window import FixDataWindow
from view_html import ViewHTML

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title('Main Window')

        self.frame = Frame(master, padx=20, pady=20)
        self.frame.pack()

        self.import_button = Button(self.frame, text='Import CSV', command=self.open_import_window, width=15)
        self.import_button.pack()

        self.manual_entry_button = Button(self.frame, text='Manual Entry', command=self.open_manual_entry_window, width=15)
        self.manual_entry_button.pack()

        self.fix_data_button = Button(self.frame, text='Fix Data', command=self.open_fix_data_window, width=15)
        self.fix_data_button.pack()

        self.view_html_button = Button(self.frame, text='View HTML', command=self.open_view_html, width=15)
        self.view_html_button.pack()

        self.close_button = Button(self.frame, text='Close', command=master.quit, width=10)
        self.close_button.pack(pady=(20, 0))

    def open_import_window(self):
        new_window = Toplevel(self.master)
        import_window = ImportWindow(new_window)

    def open_manual_entry_window(self):
        new_window = Toplevel(self.master)
        manual_entry_window = ManualEntryWindow(new_window)

    def open_fix_data_window(self):
        new_window = Toplevel(self.master)
        fix_data_window = FixDataWindow(new_window, {})

    def open_view_html(self):
        new_window = Toplevel(self.master)
        view_html = ViewHTML(new_window)

if __name__ == '__main__':
    root = Tk()
    main_window = MainWindow(root)
    root.mainloop()