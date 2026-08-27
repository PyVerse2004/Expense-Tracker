import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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
    amount = amount_entry.get()
    category = category_entry.get()
    description  = description_entry.get()

    if not amount:
        messagebox.showerror("Error" , "Amount Is Required.")
        return
    
    if not category:
        messagebox.showerror("Error" , "Category Is Required.")
        return
    
    if not description:
        messagebox.showerror("Error" , "Description Is Required.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error" , "Amount Must Be A Number")
        return

    if amount <= 0:
            messagebox.showerror("Error" , "Amount Must Be greater Than Zero")
            return
    
    tracker.add_expense(amount , category , description)

    refresh_table()
    update_total(tracker.expenses_list)

    amount_entry.delete(0 , tk.END)
    category_entry.delete(0 , tk.END)
    description_entry.delete(0 , tk.END)

button = tk.Button(
    window,
    text="Add Expense",
    command=get_expense,
)

search_entry = tk.Entry(window)

def search_expenses():
    search_value = search_entry.get()

    if not search_value:
        messagebox.showwarning("Warning" , "Please Enter A Search Value")
        return
    
    search_method = search_type.get()

    if search_method == "Category" :
        results = tracker.search_by_category(search_value) 

    elif search_method == "Date" :
        results = tracker.search_by_date(search_value)

    elif search_method == "Min" :
        try:
            minimum = float(search_value)

        except ValueError:
            messagebox.showerror("Error" , "Min Amount Must Be A Number")
            return
        results = tracker.search_by_amount(float(minimum))

    else:
        return
    
    table.delete(*table.get_children())

    for track in results:
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
    update_total(results)

search_type = ttk.Combobox(
    window,
    values=["Category" , "Date" , "Min"],
    state="readonly"
)
search_type.set("Category")

search_button = tk.Button(
    window,
    text="Search",
    command=search_expenses
)

table = ttk.Treeview(window)

def clear_search():
    refresh_table()
    update_total(tracker.expenses_list)
    
    search_entry.delete(0 , tk.END)

clear_search_button = tk.Button(
    window,
    text="Clear Search",
    command=clear_search
)

search_type.grid(row=5 , column=3)
search_entry.grid(row=5 , column=0)
search_button.grid(row=5 , column=1)
clear_search_button.grid(row=5 , column=2)

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
    table.delete(*table.get_children())
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
    
total_label = tk.Label(
    window,
    text="Total Expense : "
)

def update_total(expenses):
    total = sum(track["amount"] for track in expenses)
    total_label.config(text=f"Total Expense : {total}")
    

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

table.grid(row=7 , column=0 , columnspan=2 )
total_label.grid(row=8 , column=0 , columnspan=2)

def delete_expense():
    selected = table.selection()

    if not selected:
        messagebox.showwarning("Warning" , "Please Select An Expnese To Delete")
        return

    answer = messagebox.askyesno("Confirm Delete" , "Are You Sure Want To Delete")
    if not answer:
        return
    
    item = table.item(selected[0])
    expense_id = item["values"][0]

    tracker.delete_expense(expense_id)

    refresh_table()
    update_total(tracker.expenses_list)


delete_button = tk.Button(
    window,
    text="Delete",
    command=delete_expense
)

delete_button.grid(row=7 , column=2 , columnspan=2)


refresh_table()
update_total(tracker.expenses_list)



window.mainloop()