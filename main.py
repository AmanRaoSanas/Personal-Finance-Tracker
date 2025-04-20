from models.transaction import Transaction
from utils.helpers import add_transaction as addT
from utils.helpers import save_transaction as saveT
from utils.helpers import load_transaction as loadT
from utils.helpers import view_transaction as viewT
from models.finance_manager import FinanceManager

def main():
    print(f"{'Welcome':-^60}")
    finc_obj = FinanceManager()
    finc_obj.load_transaction()

    # CLI menu
    while True:
        option = int(input("Enter the number of  your choice: \n1) Add Transaction \n2) View Transactions \n3) Save data \n4) Exit \n\nYour choice: "))
        if option == 1:
            finc_obj.add_transaction()
        elif option == 2:
            finc_obj.view_transaction()
        elif option == 3:
            finc_obj.save_transaction()
        elif option == 4:
            print("Thanks")
            break
        else:
            print("Please enter a number from 1, 2, 3 and 4")

if __name__ == "__main__":
    main()





    # obj = Transaction(500, "food", '17/04/2025', "at cafe")
    # print(obj)

    # a = addT()
    # print(a)
    #
    # saveT(a)
    # print(loadT())
