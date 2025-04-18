from json import JSONDecodeError
from models.transaction import Transaction
import data
import os, json

def add_transaction():
    amt = int(input("enter a amount "))
    cat = input("enter a category ")
    date = input("enter date ")
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
