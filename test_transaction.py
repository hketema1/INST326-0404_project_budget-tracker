
"""
test_transaction.py

Unit tests for the Transaction class.
"""

import unittest
from transaction import Transaction

class TestTransaction(unittest.TestCase):
    def test_to_dict(self):
        t = Transaction(20.0, "Food", "Lunch", "expense")
        expected = {
            "amount": 20.0,
            "category": "Food",
            "description": "Lunch",
            "type": "expense"
        }
        self.assertEqual(t.to_dict(), expected)

    def test_from_dict(self):
        data = {
            "amount": 150.0,
            "category": "Salary",
            "description": "Paycheck",
            "type": "income"
        }
        t = Transaction.from_dict(data)
        self.assertEqual(t.amount, 150.0)
        self.assertEqual(t.category, "Salary")
        self.assertEqual(t.description, "Paycheck")
        self.assertEqual(t.trans_type, "income")

if __name__ == "__main__":
    unittest.main()
