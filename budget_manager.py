"""
budget_manager.py

Handles storing, retrieving, and summarizing transactions.
"""

import json
from transaction import Transaction

class BudgetManager:
    """
    A class used to manage financial transactions including adding,
    summarizing, saving, and loading transaction data.
    """
    
    def __init__(self):
        ## This initializes the transaction list to store all transaction objects
        """Initializes the BudgetManager with an empty list of transactions."""
        self.transactions = []

    def add_transaction(self, transaction):
        ## This adds a new transaction to the transaction list
        """
        Adds a transaction to the internal list.

        Args:
            transaction (Transaction): The transaction to be added.
        """
        self.transactions.append(transaction)

    def get_balance(self):
        ## This calculates the current balance by subtracting total expenses from total income
        """
        Calculates the net balance based on income and expenses.

        Returns:
            float: The net balance (income - expenses).
        """
        income = sum(t.amount for t in self.transactions if t.trans_type == "income")
        expense = sum(t.amount for t in self.transactions if t.trans_type == "expense")
        return income - expense

    def save_to_file(self, filename):
        ## This saves all transactions to a JSON file for persistence
        """
        Saves all transactions to a JSON file.

        Args:
            filename (str): The name of the file to save transactions to.
        """
        with open(filename, "w") as f:
            json.dump([t.to_dict() for t in self.transactions], f)

    def load_from_file(self, filename):
        ## This loads transactions from a JSON file into the transaction list
        """
        Loads transactions from a JSON file. If file does not exist, initializes with an empty list.

        Args:
            filename (str): The name of the file to load transactions from.
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.transactions = [Transaction.from_dict(item) for item in data]
        except FileNotFoundError:
            ## If the file doesn't exist, it initializes with an empty list
            self.transactions = []

    def summary_by_category(self):
        ## This returns a dictionary summarizing total amounts spent or earned per category
        """
        Returns the total amount of transactions per category.

        Returns:
            dict: A dictionary with categories as keys and summed amounts as values.
        """
        summary = {}
        for t in self.transactions:
            summary[t.category] = summary.get(t.category, 0) + t.amount
        return summary
