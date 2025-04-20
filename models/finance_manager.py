from json import JSONDecodeError
from models.transaction import Transaction
import os, json
from datetime import datetime

class FinanceManager:

# Class constructor
    def __init__(self):
        self.transaction_list = []

# method to add new transaction with user input
    def add_transaction(self):
    # data input validation open
        while True:
            try:
                amt = float(input("enter a amount "))
                float(amt)
                break
            except ValueError:
                print("Enter a valid ammount")

        cat = input("enter a category ")
        while True:
            try:
                date = input("enter date ").strip()
                datetime.strptime(date, "%d/%m/%Y")
                break
            except:
                print("invalid date please enter date in dd/mm/yyyy")
        note = input("note ")
    # data input validation close
        obj = Transaction(amt, cat, date, note)
        self.transaction_list.append(obj.__dict__)
        # return obj

# Method to view all the entries
    def view_transaction(self):
        # Printing transaction data
        if self.transaction_list != []:
            print(f"{'Amount':^10} | {'Category':^10} | {'Date':^15} | {'Tag':^10}")
            print('-' * 50)
            for i in self.transaction_list:
                print(f"  {i["amount"]:<8} | {i["category"]:<10} | {i["date"]:^15} | {i["note"]:<10}")
        else:
            print(f"{"No entries":-^50}")

# Method to save transaction to json
    def save_transaction(self, file="data/transaction.json"):
        data = []
        data.extend(self.transaction_list)

        with open(file, "w") as f:
            json.dump(data, f, indent=4)

# Method to load transaction
    def load_transaction(self,file="data/transaction.json"):
        data = []

        if os.path.exists(file):
            with open(file, "r") as f:
                try:
                    data = json.load(f)
                except JSONDecodeError:
                    data = []
        self.transaction_list.extend(data)
        # return json.dumps(data, indent=5)








    # def view_transaction(self,file="data/transaction.json"):
    #     data = []
    #
    #     if os.path.exists(file):
    #         with open(file, "r") as f:
    #             try:
    #                 data = json.load(f)
    #             except JSONDecodeError:
    #                 data = []
    #     if data != []:
    #         print(f"{'Amount':^10} | {'Category':^10} | {'Date':^15} | {'Tag':^10}")
    #         print('-' * 50)
    #         print(f"{"There is no data":-^30}")
    #         for i in data:
    #             print(f"  {i["amount"]:<8} | {i["category"]:<10} | {i["date"]:^15} | {i["note"]:<10}")
    #     else:
    #         pass
