import json
from datetime import date

class ExpenseTracker:
    def __init__(self , filename="Expenses.json"):
        self.filename = filename
        self.expenses_list = []
        self.t_id = 1
        
    def save_file(self):
        with open(self.filename , "w") as file :
            json.dump(self.expenses_list , file , indent=4)

    def add_expense(self, amount , category , description):
        track = {
            "id" : self.t_id , 
            "amount" : amount , 
            "category" : category , 
            "description" : description , 
            "date" : date.today().isoformat()
        }
        
        self.expenses_list.append(track)
        self.save_file()
        self.t_id +=1
        
    def delete_expense(self , item):
        for track in self.expenses_list:
            if track["id"] == item :
                self.expenses_list.remove(track)
                self.save_file()  

    def total_expense(self):
        self.total = 0

        for track in self.expenses_list:
            self.total += track["amount"]

        return self.total

    def show_expense(self):
        for track in self.expenses_list:
            print(f"[{track["id"]}] - Amount: {track["amount"]}$ For {track["description"]} --> {track["category"]}") 

    def search_by_category(self , category):
        for track in self.expenses_list :
            if track["category"] == category:
                print(track)
    






acc = ExpenseTracker()
acc1 = ExpenseTracker()

acc.add_expense(250 , "Food" , "Lunch")
acc.add_expense(120 , "Transport" , "Taxi")
acc.add_expense(120 , "Transport" , "Snapp")


print(acc.expenses_list)

# acc.delete_expense(2)

print(acc.expenses_list)

print(acc.total_expense())

acc.show_expense()

acc.search_by_category("Transport")