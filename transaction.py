"""
transaction.py

Defines the Transaction class for managing individual income and expense entries.
"""

class Transaction:
    def __init__(self, amount, category, description, trans_type):
        ###This initializes the transaction with all necessary details
 
        """
        Initializes a new transaction.

        Args:
            amount (float): The amount of the transaction.
            category (str): The category of the transaction.
            description (str): A brief description of the transaction.
            trans_type (str): 'income' or 'expense'
        """
        self.amount = amount
        self.category = category
        self.description = description
        self.trans_type = trans_type

    def to_dict(self):
     ###This converts the transaction object to a dictionary format for saving

        """Returns the transaction data as a dictionary."""
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "type": self.trans_type
        }

    @staticmethod
    ###This creates a transaction object from a saved dictionary

    def from_dict(data):
        """Creates a Transaction object from a dictionary."""
        return Transaction(data["amount"], data["category"], data["description"], data["type"])
