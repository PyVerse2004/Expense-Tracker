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
        for track in self.expenses_list:
            if track["id"] == item:
                self.expenses_list.remove(track)
            return

    def total_expense(self):
        self.total = 0

        for track in self.expenses_list:
            self.total += track["amount"]

        return self.total

    def show_expense(self):
        for track in self.expenses_list:
            print(f"[{track["id"]}] - Amount: {track["amount"]}$ For {track["description"]} --> {track["category"]}") 









acc = ExpenseTracker()
acc1 = ExpenseTracker()

acc.add_expense(250 , "Food" , "Lunch")
acc.add_expense(120 , "Transport" , "Taxi")

print(acc.expenses_list)

acc.delete_expense(1)

print(acc.expenses_list)

print(acc.total_expense())

acc.show_expense()