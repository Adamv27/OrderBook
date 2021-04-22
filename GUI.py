from AddEntry import AddEntry
from tkinter import *
import tkinter.font as font


class Gui:
    def __init__(self, root):
        self.root = root
        self.width = 400
        self.height = 400
        self.root.geometry(f'{self.width}x{self.height}')
        self.font = font.Font(size=10)

        self.name_entry = AddEntry(self.root, 'Name', 1, 1)
        self.name_entry.entry.grid(padx=(5, 5))
        self.number_entry = AddEntry(self.root, 'Number', 1, 2)
        self.time_entry = AddEntry(self.root, 'Time', 1, 3)

        self.order_entry = AddEntry(self.root, 'Order', 2, 1)
        self.order_entry.entry.grid(columnspan=2, ipadx=50, ipady=15, pady=5)

        self.add_order_button = Button(self.root, text='Add Order', bg='#3C4042', fg='white')
        self.add_order_button.grid(row=2, column=3, ipadx=15, ipady=10)

        self.root.configure(bg='#121212')

        self.search_order_button = Button(self.root, text='Search', bg='#3C4042', fg='white')
        self.search_order_button.grid(row=3, column=2, pady=20, ipady=10, ipadx=40)

    def get_order(self):
        full_order = [self.name_entry.entry.get(), self.number_entry.entry.get(), self.time_entry.entry.get(), self.order_entry.entry.get()]
        return full_order

    def reset_entries(self):
        self.name_entry.entry.delete(0, 'end')
        self.name_entry.entry.insert(0, 'Name')

        self.number_entry.entry.delete(0, 'end')
        self.number_entry.entry.insert(0, 'Number')

        self.time_entry.entry.delete(0, 'end')
        self.time_entry.entry.insert(0, 'Time')

        self.order_entry.entry.delete(0, 'end')
        self.order_entry.entry.insert(0, 'Order')
    
