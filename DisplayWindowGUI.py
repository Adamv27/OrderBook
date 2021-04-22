import sqlite3
from tkinter import *


class GUI:
    def __init__(self, root):
        self.window = Toplevel(root)
        self.width = 400
        self.height = 400
        self.color = '#121212'
        self.window.configure(bg=self.color)
        self.window.geometry(f'{self.width}x{self.height}')

    def display_orders(self, orders):
        for index, order in enumerate(orders):
            label = Label(self.window, text=order, fg='white', bg=self.color)
            label.grid(row=index + 1, column=1, pady=5)

            button = Button(self.window, text='DELETE', bg=self.color, fg='white')
            button.grid(row=index+1, column=2)
            button.configure(command=lambda index=index: delete_order(index, orders))


def delete_order(order, orders):
    conn = sqlite3.connect('crosbys.db')
    c = conn.cursor()
    order = orders[order].split()

    sql = '''DELETE FROM orders 
                  WHERE name=? AND number=? AND time=? and customerOrder=?'''

    c.execute(sql, (order[0], order[1], order[2], order[3],))

    print('Deleted order')

    conn.commit()
    conn.close()



