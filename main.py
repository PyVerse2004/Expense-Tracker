from datetime import datetime

class ExpenseTracker:
    def __init__(self , amount , category , description):
        self.t_id = 1
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now()
        self.expenses_list = []

    def add_expense(self):
        track = {
            "id" : self.t_id , 
            "amount" : self.amount , 
            "category" : self.category , 
            "description" : self.description , 
            "date" : self.date
        }
        self.t_id +=1
        self.expenses_list.append(track)

    def delete_expense(self , item):
        self.expenses_list.pop(item-1)
        



















acc = ExpenseTracker(255 , "food" , "description")

acc.add_expense()


acc1 = ExpenseTracker(2 , "foodsdaad" , "dn")
acc.add_expense()
print(acc.expenses_list)
acc.delete_expense(2)
print(acc.expenses_list)
