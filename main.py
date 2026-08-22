from datetime import datetime

class ExpenseTracker:
    def __init__(self , amount , category , description):
        self.t_id = 1
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now()


