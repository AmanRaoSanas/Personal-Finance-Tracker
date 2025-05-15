import unittest
from models.transaction import Transaction
from models.finance_manager import FinanceManager
import os

class Test_Transaction(unittest.TestCase):
    def test_transaction_check(self):

        tx_obj = Transaction(500,"Food","12/04/2025","Lunch")
        self.assertEqual(tx_obj.amount, 500)
        self.assertEqual(tx_obj.category, "Food")
        self.assertEqual(tx_obj.date, "12/04/2025")
        self.assertEqual(tx_obj.note, "Lunch")

class Test_Finance(unittest.TestCase):

    def test_save_transaction(self):
        tx_obj = Transaction(500, "Food", "12/04/2025", "Lunch")
        fm_obj1 = FinanceManager()

        fm_obj1.add_transaction(tx_obj)
        fm_obj1.save_transaction("data/test_transaction.json")

        fm_obj2  = FinanceManager()
        fm_obj2.load_transaction("data/test_transaction.json")

        self.assertEqual(len(fm_obj2.transaction_list),1)
        self.assertEqual(fm_obj2.transaction_list[0]['amount'], 500)
        self.assertEqual(fm_obj2.transaction_list[0]['date'], "12/04/2025")
        os.remove("data/test_transaction.json")


