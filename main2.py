import tkinter as tk
from tkinter import ttk, messagebox
from tracker import ExpenseTracker


class ExpenseApp:

    def __init__(self, window):
        self.window = window
        self.tracker = ExpenseTracker()

        # Window
        self.window.title("Personal Expense Tracker")
        self.window.geometry("950x650")
        self.window.minsize(800, 550)

        # Style
        self.setup_style()

        # UI
        self.create_header()
        self.create_add_section()
        self.create_search_section()
        self.create_table()
        self.create_bottom_section()

        # Initial data
        self.refresh_table()
        self.update_total(self.tracker.expenses_list)

    # ==================================================
    # STYLE
    # ==================================================

    def setup_style(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Title.TLabel",
            font=("Arial", 22, "bold")
        )

        style.configure(
            "Section.TLabelframe.Label",
            font=("Arial", 11, "bold")
        )

        style.configure(
            "Treeview",
            rowheight=30,
            font=("Arial", 10)
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

        style.configure(
            "Action.TButton",
            font=("Arial", 10, "bold"),
            padding=6
        )

        style.configure(
            "Total.TLabel",
            font=("Arial", 13, "bold")
        )

    # ==================================================
    # HEADER
    # ==================================================

    def create_header(self):

        header_frame = ttk.Frame(
            self.window,
            padding=(20, 20, 20, 10)
        )

        header_frame.pack(fill="x")

        title = ttk.Label(
            header_frame,
            text="Personal Expense Tracker",
            style="Title.TLabel"
        )

        title.pack(anchor="w")

        subtitle = ttk.Label(
            header_frame,
            text="Manage your personal expenses"
        )

        subtitle.pack(
            anchor="w",
            pady=(5, 0)
        )

    # ==================================================
    # ADD EXPENSE SECTION
    # ==================================================

    def create_add_section(self):

        add_frame = ttk.LabelFrame(
            self.window,
            text="Add Expense",
            padding=15
        )

        add_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Amount
        ttk.Label(
            add_frame,
            text="Amount:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.amount_entry = ttk.Entry(
            add_frame,
            width=20
        )

        self.amount_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        # Category
        ttk.Label(
            add_frame,
            text="Category:"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        self.category_entry = ttk.Entry(
            add_frame,
            width=20
        )

        self.category_entry.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        # Description
        ttk.Label(
            add_frame,
            text="Description:"
        ).grid(
            row=0,
            column=4,
            padx=5,
            pady=5
        )

        self.description_entry = ttk.Entry(
            add_frame,
            width=25
        )

        self.description_entry.grid(
            row=0,
            column=5,
            padx=5,
            pady=5
        )

        # Add button
        self.add_button = ttk.Button(
            add_frame,
            text="Add Expense",
            style="Action.TButton",
            command=self.get_expense
        )

        self.add_button.grid(
            row=0,
            column=6,
            padx=10,
            pady=5
        )

    # ==================================================
    # SEARCH SECTION
    # ==================================================

    def create_search_section(self):

        search_frame = ttk.LabelFrame(
            self.window,
            text="Search Expenses",
            padding=15
        )

        search_frame.pack(
            fill="x",
            padx=20,
            pady=5
        )

        ttk.Label(
            search_frame,
            text="Search by:"
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        self.search_type = ttk.Combobox(
            search_frame,
            values=[
                "Category",
                "Date",
                "Min"
            ],
            state="readonly",
            width=15
        )

        self.search_type.set("Category")

        self.search_type.grid(
            row=0,
            column=1,
            padx=5
        )

        self.search_entry = ttk.Entry(
            search_frame,
            width=30
        )

        self.search_entry.grid(
            row=0,
            column=2,
            padx=5
        )

        self.search_button = ttk.Button(
            search_frame,
            text="Search",
            style="Action.TButton",
            command=self.search_expenses
        )

        self.search_button.grid(
            row=0,
            column=3,
            padx=5
        )

        self.clear_search_button = ttk.Button(
            search_frame,
            text="Clear Search",
            command=self.clear_search
        )

        self.clear_search_button.grid(
            row=0,
            column=4,
            padx=5
        )

    # ==================================================
    # TABLE
    # ==================================================

    def create_table(self):

        table_frame = ttk.Frame(
            self.window,
            padding=(20, 10, 20, 5)
        )

        table_frame.pack(
            fill="both",
            expand=True
        )

        columns = (
            "id",
            "date",
            "category",
            "description",
            "amount"
        )

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        # Headings

        self.table.heading(
            "id",
            text="ID"
        )

        self.table.heading(
            "date",
            text="Date"
        )

        self.table.heading(
            "category",
            text="Category"
        )

        self.table.heading(
            "description",
            text="Description"
        )

        self.table.heading(
            "amount",
            text="Amount"
        )

        # Column sizes

        self.table.column(
            "id",
            width=50,
            anchor="center"
        )

        self.table.column(
            "date",
            width=120,
            anchor="center"
        )

        self.table.column(
            "category",
            width=130,
            anchor="center"
        )

        self.table.column(
            "description",
            width=300,
            anchor="w"
        )

        self.table.column(
            "amount",
            width=100,
            anchor="center"
        )

        # Scrollbar

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.table.yview
        )

        self.table.configure(
            yscrollcommand=scrollbar.set
        )

        self.table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

    # ==================================================
    # BOTTOM SECTION
    # ==================================================

    def create_bottom_section(self):

        bottom_frame = ttk.Frame(
            self.window,
            padding=(20, 10, 20, 15)
        )

        bottom_frame.pack(
            fill="x"
        )

        self.total_label = ttk.Label(
            bottom_frame,
            text="Total Expense: $0",
            style="Total.TLabel"
        )

        self.total_label.pack(
            side="left"
        )

        self.delete_button = ttk.Button(
            bottom_frame,
            text="Delete Selected",
            command=self.delete_expense
        )

        self.delete_button.pack(
            side="right"
        )

    # ==================================================
    # ADD EXPENSE
    # ==================================================

    def get_expense(self):

        amount = self.amount_entry.get().strip()
        category = self.category_entry.get().strip()
        description = self.description_entry.get().strip()

        # Amount required
        if not amount:

            messagebox.showerror(
                "Error",
                "Amount Is Required."
            )

            self.amount_entry.focus()

            return

        # Category required
        if not category:

            messagebox.showerror(
                "Error",
                "Category Is Required."
            )

            self.category_entry.focus()

            return

        # Description required
        if not description:

            messagebox.showerror(
                "Error",
                "Description Is Required."
            )

            self.description_entry.focus()

            return

        # Convert amount
        try:

            amount = float(amount)

        except ValueError:

            messagebox.showerror(
                "Error",
                "Amount Must Be A Number."
            )

            self.amount_entry.focus()

            return

        # Amount must be positive
        if amount <= 0:

            messagebox.showerror(
                "Error",
                "Amount Must Be Greater Than Zero."
            )

            self.amount_entry.focus()

            return

        # Add expense
        self.tracker.add_expense(
            amount,
            category,
            description
        )

        # Update GUI
        self.refresh_table()
        self.update_total(
            self.tracker.expenses_list
        )

        # Clear entries
        self.amount_entry.delete(
            0,
            tk.END
        )

        self.category_entry.delete(
            0,
            tk.END
        )

        self.description_entry.delete(
            0,
            tk.END
        )

        self.amount_entry.focus()

    # ==================================================
    # SEARCH
    # ==================================================

    def search_expenses(self):

        search_value = self.search_entry.get().strip()

        if not search_value:

            messagebox.showwarning(
                "Warning",
                "Please Enter A Search Value."
            )

            self.search_entry.focus()

            return

        search_method = self.search_type.get()

        # Category
        if search_method == "Category":

            results = self.tracker.search_by_category(
                search_value
            )

        # Date
        elif search_method == "Date":

            results = self.tracker.search_by_date(
                search_value
            )

        # Minimum Amount
        elif search_method == "Min":

            try:

                minimum = float(search_value)

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Min Amount Must Be A Number."
                )

                self.search_entry.focus()

                return

            results = self.tracker.search_by_amount(
                minimum
            )

        else:
            return

        # Clear table
        self.table.delete(
            *self.table.get_children()
        )

        # Display results
        for track in results:

            self.table.insert(
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

        # Update total
        self.update_total(results)

        # No results
        if not results:

            messagebox.showinfo(
                "Search",
                "No Expense Found."
            )

    # ==================================================
    # CLEAR SEARCH
    # ==================================================

    def clear_search(self):

        self.search_entry.delete(
            0,
            tk.END
        )

        self.search_type.set(
            "Category"
        )

        self.refresh_table()

        self.update_total(
            self.tracker.expenses_list
        )

    # ==================================================
    # DELETE
    # ==================================================

    def delete_expense(self):

        selected = self.table.selection()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please Select An Expense To Delete."
            )

            return

        answer = messagebox.askyesno(
            "Confirm Delete",
            "Are You Sure You Want To Delete This Expense?"
        )

        if not answer:
            return

        item = self.table.item(
            selected[0]
        )

        expense_id = item["values"][0]

        self.tracker.delete_expense(
            expense_id
        )

        self.refresh_table()

        self.update_total(
            self.tracker.expenses_list
        )

    # ==================================================
    # REFRESH TABLE
    # ==================================================

    def refresh_table(self):

        self.table.delete(
            *self.table.get_children()
        )

        for track in self.tracker.expenses_list:

            self.table.insert(
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

    # ==================================================
    # UPDATE TOTAL
    # ==================================================

    def update_total(self, expenses):

        total = sum(
            track["amount"]
            for track in expenses
        )

        self.total_label.config(
            text=f"Total Expense: ${total:.2f}"
        )


# ======================================================
# START APPLICATION
# ======================================================

# if __name__ == "main":
window = tk.Tk()
app = ExpenseApp(window)
window.mainloop()