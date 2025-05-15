import argparse
from models.transaction import Transaction
from models.finance_manager import FinanceManager
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description="Personal Finance Tracker")

    subparser = parser.add_subparsers(dest="command")

    add_txn = subparser.add_parser('add', help="Add a new transaction")
    view_txn = subparser.add_parser('view', help="View all transactions")
    filt = subparser.add_parser('filter', help="filter all transactions")

    # add transaction arguments
    add_txn.add_argument('--amount', type=float, required=True)
    add_txn.add_argument('--category', type=str, required=True)
    add_txn.add_argument('--date', type=str, required=True)
    add_txn.add_argument('--note', type=str, default="")

    # filtering arguments
    filt.add_argument("--category", type=str)
    filt.add_argument("--start_date", type=str)
    filt.add_argument("--end_date", type=str)


    args = parser.parse_args()


    if args.command == "filter":
        fm =FinanceManager()
        if args.category:
            data = [dt for dt in fm.transaction_list if args.category.lower() == dt['category'].lower()]
            print(f"{'Amount':^10} | {'Category':^10} | {'Date':^15} | {'Tag':^10}")
            print('-' * 50)
            for i in data:
                print(f"  {i["amount"]:<8} | {i["category"]:<10} | {i["date"]:^15} | {i["note"]:<10}")


        if args.start_date and args.end_date:
            print("both")
            from_date = datetime.strptime(args.start_date, "%d/%m/%Y")
            end_date = datetime.strptime(args.end_date, "%d/%m/%Y")
            data = [dt for dt in fm.transaction_list if from_date <= datetime.strptime(dt['date'], "%d/%m/%Y") <= end_date]
            print(f"{'Amount':^10} | {'Category':^10} | {'Date':^15} | {'Tag':^10}")
            print('-' * 50)
            for i in data:
                print(f"  {i["amount"]:<8} | {i["category"]:<10} | {i["date"]:^15} | {i["note"]:<10}")

        elif args.start_date:
            from_date = datetime.strptime(args.start_date, "%d/%m/%Y")
            data = [dt for dt in fm.transaction_list if datetime.strptime(dt['date'], "%d/%m/%Y") >= from_date]
            print(f"{'Amount':^10} | {'Category':^10} | {'Date':^15} | {'Tag':^10}")
            print('-' * 50)
            for i in data:
                print(f"  {i["amount"]:<8} | {i["category"]:<10} | {i["date"]:^15} | {i["note"]:<10}")

        elif args.end_date:
            end_date = datetime.strptime(args.end_date, "%d/%m/%Y")
            data = [dt for dt in fm.transaction_list if datetime.strptime(dt['date'], "%d/%m/%Y") <= end_date]
            print(f"{'Amount':^10} | {'Category':^10} | {'Date':^15} | {'Tag':^10}")
            print('-' * 50)
            for i in data:
                print(f"  {i["amount"]:<8} | {i["category"]:<10} | {i["date"]:^15} | {i["note"]:<10}")


    if args.command == "add":
        txn = Transaction(
            args.amount,
            args.category,
            args.date,
            args.note
        )

        fm = FinanceManager()

        fm.load_transaction()
        fm.add_transaction(txn)
        fm.save_transaction()


    if args.command == "view":
        fm = FinanceManager()
        # fm.load_transaction()
        fm.view_transaction()

if __name__ == "__main__":
    main()



