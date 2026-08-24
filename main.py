import tkinter as tk
from tkinter import ttk
from tracker import ExpenseTracker

window = tk.Tk()
window.geometry("800x600")

tracker = ExpenseTracker()

label = tk.Label(
    window,
    text= "Personal Expense Tracker"
)

amount_label = tk.Label(
    window,
    text="1- Amount :"
)

amount_entry = tk.Entry(window)

category_label = tk.Label(
    window,
    text="2- Category :"
)

category_entry = tk.Entry(window)


description_label = tk.Label(
    window,
    text="3- Description :"
)

description_entry = tk.Entry(window)

def get_expense():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        description  = description_entry.get()

        tracker.add_expense(amount , category , description)

        amount_entry.delete(0 , tk.END)
        category_entry.delete(0 , tk.END)
        description_entry.delete(0 , tk.END)

    except ValueError:
        print("Invalid Format")

button = tk.Button(
    window,
    text="Add Expense",
    command=get_expense,
)

table = ttk.Treeview(window)
columns = ("id" , "date" , "category" , "description" , "amount")

label.grid(row=0 , column=1)

amount_label.grid(row=1 , column=0)
amount_entry.grid(row=1 , column=1)


category_label.grid(row=2 , column=0)
category_entry.grid(row=2 , column=1)

description_label.grid(row=3 , column=0)
description_entry.grid(row=3 , column=1)

button.grid(row=4 , column=1)

table = ttk.Treeview(
    window,
    columns=columns,
    show="headings"
)

def refresh_table():
    for track in tracker.expenses_list:
        table.insert(
            "",
            tk.END,
            values=(
                track["id"],
                track["date"],
                track["category"],
                track["description"],
                track["amount"]
            )
        )

table.heading("id" , text="ID")
table.heading("date" , text="Date")
table.heading("category" , text="Category")
table.heading("description" , text="Description")
table.heading("amount" , text="Amount")

table.column("id" , width=50)
table.column("date" , width=100)
table.column("category" , width=100)
table.column("description" , width=200)
table.column("amount" , width=100)

table.grid(row=6 , column=1 , columnspan=2 )

refresh_table()


window.mainloop()