from tkinter import *


class SearchGUI:
    def __init__(self, root):
        self.color = '#121212'
        self.window = Toplevel(root)
        self.width = 400
        self.height = 400
        self.window.configure(bg=self.color)
        self.window.geometry(f'{self.width}x{self.height}')

        self.instruction_label_string = 'Search for an oder by entering the name, time, phone number, or order'
        self.instruction_label = Label(self.window, text=self.instruction_label_string, fg='white', bg=self.color)
        self.instruction_label.grid(row=1)

        self.search_entry = Entry(self.window, justify='center', bg=self.color, fg='white')
        self.search_entry.insert(0, 'Search...')
        self.search_entry_first_click = True
        self.search_entry.bind('<FocusIn>', self.on_click)
        self.search_entry.grid(row=2, pady=20, ipady=10, ipadx=30)

        self.search_button = Button(self.window, text='Search', bg='#3C4042', fg='white')
        self.search_button.grid(row=3, ipady=10, ipadx=30, pady=10)

    def on_click(self, event):
        if self.search_entry_first_click:
            self.search_entry_first_click = False
            self.search_entry.delete(0, 'end')

