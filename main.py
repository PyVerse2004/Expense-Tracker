import json
from datetime import date

class ExpenseTracker:
    def __init__(self , filename="Expenses.json"):
        self.filename = filename
        self.load_file()
        self.expenses_list = []
        self.t_id = 1

    def load_file(self):   
        with open(self.filename , "r") as file :
            json.load(file)

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
    
    def search_by_date(self , date):
        for track in self.expenses_list:
            if track["date"] == date:
                print(track)
    
    def search_by_amount(self , minimum):
        for track in self.expenses_list:
            if track["amount"] >= minimum:
                print(track)

    def category_summary(self):
        summary = {}
        for track in self.expenses_list:
            if not track["category"] in summary:
                summary[track["category"]] = track["amount"]
            else:
                for i in summary:
                    if track["category"] == i :
                        summary[i] += track["amount"]
        print("=" * 17)
        print("CATEGORY SUMMARY")
        print("=" * 17)
        for i in summary:
            print(f"{i} : ${summary[i]}")
        print("")
        print(f"Total : {sum(summary.values())}")
            
    def monthly_summary(self , date):
        summary = {}
        for track in self.expenses_list:
            if track["date"][:7] == date:
                if not track["category"] in summary:
                    summary[track["category"]] = track["amount"]
                else:
                    for i in summary:
                        if track["category"] == i :
                            summary[i] += track["amount"]
        print("=" * 17)
        print(f"{date} SUMMARY")
        print("=" * 17)
        for i in summary:
            print(f"{i} : ${summary[i]}")
        print("")
        print(f"Total : {sum(summary.values())}")



acc = ExpenseTracker()
acc1 = ExpenseTracker()

acc.add_expense(250 , "Food" , "Lunch")
acc.add_expense(120 , "Transport" , "Taxi")
acc.add_expense(200 , "Transport" , "Snapp")
acc.add_expense(70 , "Shopping" , "Shoes")
acc.add_expense(95 , "Shopping" , "Shoes")
acc.add_expense(35 , "Taxes" , "Internet")


print(acc.expenses_list)

# acc.delete_expense(2)

print(acc.expenses_list)

print(acc.total_expense())

acc.show_expense()

acc.search_by_category("Transport")
print("-"*30)
acc.search_by_date("2026-08-24")
print("-"*30)
acc.search_by_amount(200)
print("-"*30)
print("-"*30)
acc.category_summary()
print("-"*30)
acc.monthly_summary("2026-08")
