import sys
import unittest
from unicodedata import category

from models.transaction import Transaction
from models.finance_manager import FinanceManager
from unittest.mock import patch
import cli

class TestCli(unittest.TestCase):

    @patch('builtins.print')
    @patch('models.finance_manager.FinanceManager.view_transaction')
    def test_view_command(self, mock_view_transaction, mock_print):
        test_args = ['cli.py', 'view']
        with patch.object(sys, 'argv', test_args):
            cli.main()
            mock_view_transaction.assert_called_once()

    @patch('builtins.print')
    @patch('models.finance_manager.FinanceManager.add_transaction')
    def test_add_command(self, mock_add_transaction,mock_print):
        test_args = [
            "cli.py", "add",
            "--amount", "400",
            "--category", "clothes",
            "--date", "13/05/2025",
            "--note", "dress"]

        with patch.object(sys, 'argv', test_args):
            cli.main()

        mock_add_transaction.assert_called_once()




if __name__ == '__main__':
    unittest.main()