from json import JSONDecodeError
from models.transaction import Transaction
import os, json
from datetime import datetime

def add_transaction():
    try:
        amt = float(input("enter a amount "))
    except ValueError:
        print("Enter a valid ammount")

    cat = input("enter a category ")
    date = input("enter date ")
    try:
        datetime.strptime(date,"%d/%m/%y")
    except:
        print("invalid date please enter date in dd/mm/yyyy")
    note = input("note ")
    obj = Transaction(amt,cat,date,note)
    return obj

def save_transaction(transaction_obj, file="data/transaction.json"):
    data = []

    if os.path.exists(file):
        with open(file, "r") as f:
            try:
                data = json.load(f)
            except JSONDecodeError:
                data =[]

    data.append(transaction_obj.to_dict())

    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def load_transaction(file="data/transaction.json"):
    data = []

    if os.path.exists(file):
        with open(file, "r") as f:
            try:
                data = json.load(f)
            except JSONDecodeError:
                data =[]
    return json.dumps(data, indent= 5)

def view_transaction(file="data/transaction.json"):
    data = []

    if os.path.exists(file):
        with open(file, "r") as f:
            try:
                data = json.load(f)
            except JSONDecodeError:
                data =[]
    if data != []:
        print(f"{'Amount':^10} | {'Category':^10} | {'Date':^15} | {'Tag':^10}")
        print('-'*50)
        for i in data:
            print(f"  {i["amount"]:<8} | {i["category"]:<10} | {i["date"]:^15} | {i["note"]:<10}")
    else:
        print("There is no data ")
