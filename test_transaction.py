"""
test_transaction.py

Unit tests for the Transaction class.

"""

import unittest
from transaction import Transaction

class TestTransaction(unittest.TestCase):
    
    """ 
    These are unit tests for methods in the transaction class
    """
    
    def test_transaction_to_dict(self):
        """ 
        This tests that to_dict() correctly converts a transaction to dictionary
        """
        
        t = Transaction(100.0, "Food", "Lunch", "expense")
        expected = {
            "amount": 100.0,
            "category": "Food",
            "description": "Lunch",
            "type": "expense"
        }
        self.assertEqual(t.to_dict(), expected)

    def test_transaction_from_dict(self):
        
        """ 
        This tests from_dict() correctly creates a Transaction object from a dictionary
        """
        
        data = {
            "amount": 50.0,
            "category": "Salary",
            "description": "Monthly salary",
            "type": "income"
        }
        t = Transaction.from_dict(data)
        self.assertEqual(t.amount, 50.0)
        self.assertEqual(t.category, "Salary")
        self.assertEqual(t.description, "Monthly salary")
        self.assertEqual(t.trans_type, "income")

if __name__ == "__main__":
    unittest.main()
