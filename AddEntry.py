from tkinter import *


class AddEntry:
    def __init__(self, root, text, row, column):
        self.color = '#3C4042'
        self.row = row
        self.column = column
        self.first_click = True

        self.entry = Entry(root, justify='center', bg=self.color)
        self.entry.insert(0, text)
        self.entry.config(fg='white')
        self.entry.bind('<FocusIn>', self.on_click)
        self.place()

    def place(self):
        self.entry.grid(row=self.row, column=self.column, ipady=5, pady=(100, 0), padx=(0, 5))

    def on_click(self, event):
        if self.first_click:
            self.first_click = False
            self.entry.delete(0, 'end')
