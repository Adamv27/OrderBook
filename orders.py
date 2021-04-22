import GUI
import sqlite3
import SearchGUI
from tkinter import *
import DisplayWindowGUI


def add_order():
    conn = sqlite3.connect('crosbys.db')
    c = conn.cursor()

    # If default words are found then the order is missing information
    default_words_list = ['Name', 'Number', 'Time', 'Order']
    order = [word for word in gui.get_order() if word not in default_words_list]

    if len(order) == 4:
        c.execute('INSERT INTO orders VALUES(?,?,?,?)', (order[0], order[1], order[2], order[3],))
        gui.reset_entries()
    else:
        print('Missing Values')
    conn.commit()
    conn.close()


def sql():
    conn = sqlite3.connect('crosbys.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS orders(
                 name text,
                 number text,
                 time text,
                 customerOrder text
                 )''')
    conn.commit()
    conn.close()


def open_search_window():
    search_window = SearchGUI.SearchGUI(root)
    # Take the text from the entry and use it to search through the database to find possible orders
    search_window.search_button.configure(command=lambda: search_order(search_window.search_entry.get()))


def search_order(search_query):
    conn = sqlite3.connect('crosbys.db')
    c = conn.cursor()
    c.execute("SELECT * FROM orders")
    all_orders = [" ".join(word) for word in c.fetchall()]

    possible_orders = []
    for order in all_orders:
        if search_query in order:
            possible_orders.append(order)

    open_display_window(possible_orders)

    conn.commit()
    conn.close()


def open_display_window(orders):
    display_window = DisplayWindowGUI.GUI(root)
    display_window.display_orders(orders)




sql()
root = Tk()
gui = GUI.Gui(root)
gui.add_order_button.configure(command=add_order)
gui.search_order_button.configure(command=open_search_window)
root.mainloop()
