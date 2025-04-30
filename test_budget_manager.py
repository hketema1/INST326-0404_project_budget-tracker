"""
test_budget_manager.py

This is for the unit tests for the BudgetManager class.

"""

import unittest
from transaction import Transaction
from budget_manager import BudgetManager

class TestBudgetManager(unittest.TestCase):
    def setUp(self):
        ## This sets up a fresh BudgetManager before each test
        self.manager = BudgetManager()
        self.income = Transaction(1000, "Salary", "Monthly salary", "income")
        self.expense = Transaction(200, "Food", "Groceries", "expense")
        self.manager.add_transaction(self.income)
        self.manager.add_transaction(self.expense)

    def test_add_transaction(self):
        ## This checks if a transaction is added correctly
        self.assertEqual(len(self.manager.transactions), 2)

    def test_get_balance(self):
        ## This checks if balance calculation is correct
        balance = self.manager.get_balance()
        expected_balance = 800  # 1000 - 200
        self.assertEqual(balance, expected_balance)

    def test_summary_by_category(self):
        ## This checks if summary by category groups amounts properly
        summary = self.manager.summary_by_category()
        self.assertEqual(summary["Salary"], 1000)
        self.assertEqual(summary["Food"], 200)

if __name__ == "__main__":
    unittest.main()
