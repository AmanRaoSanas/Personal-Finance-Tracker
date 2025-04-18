from models.transaction import Transaction
from utils.helpers import add_transaction as addT
from utils.helpers import save_transaction as saveT
from utils.helpers import load_transaction as loadT

def main():
    print("-------------------Welcome----------------")

    # obj = Transaction(500, "food", '17/04/2025', "at cafe")
    # print(obj)

    # a = addT()
    # print(a)
    #
    # saveT(a)
    # print(loadT())

    while True:
        option = int(input("Enter the number of  your choice: \n1) Add Transaction \n2) View Transactions \n3) Exit \n\nYour choice: "))
        if option == 1:
            a = addT()
            saveT(a)
        elif option == 2:
            print(loadT())
        elif option == 3:
            print("Thanks")
            break
        else:
            print("Please enter a number from 1,2 and 3")

if __name__ == "__main__":
    main()
