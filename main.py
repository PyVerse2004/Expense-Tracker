from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses_list = []
        self.t_id = 1

    def add_expense(self, amount , category , description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now()
        
        track = {
            "id" : self.t_id , 
            "amount" : self.amount , 
            "category" : self.category , 
            "description" : self.description , 
            "date" : self.date
        }
        
        self.expenses_list.append(track)
        self.t_id +=1

    def delete_expense(self , item):
        self.expenses_list.pop(item-1)
        

    def total_expense(self):
        self.total = 0

        for track in self.expenses_list:
            self.total += track["amount"]

        return self.total









# acc = ExpenseTracker()
# acc1 = ExpenseTracker()

# acc.add_expense(250 , "food" , "lunch")
# acc.add_expense(120 , "taxi" , "Transport")

# print(acc.expenses_list)

# # acc.delete_expense(1)

# print(acc.expenses_list)

# print(acc.total_expense())