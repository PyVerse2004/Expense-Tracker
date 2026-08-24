import tkinter as tk
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
        
    except:
        print("Invalid Format")

button = tk.Button(
    window,
    text="Add Expense",
    command=get_expense
    
)

label.grid(row=0 , column=1)

amount_label.grid(row=1 , column=0)
amount_entry.grid(row=1 , column=1)


category_label.grid(row=2 , column=0)
category_entry.grid(row=2 , column=1)

description_label.grid(row=3 , column=0)
description_entry.grid(row=3 , column=1)

button.grid(row=4 , column=1)

window.mainloop()