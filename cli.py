"""
cli.py
Handles user interactions via the command line.
"""

from budget_manager import BudgetManager
from transaction import Transaction

def main_menu():
    """
    Display the main CLI menu options.
    """
    ## this shows the main options for user interaction with the budget system
    print("\nBudget Tracker")
    print("1. Add Transaction")
    print("2. View Balance")
    print("3. View Summary by Category")
    print("4. Save and Exit")

def run_cli():
    """
    Run the command-line interface loop for the Budget Tracker app.
    """
    ## this creates an instance of BudgetManager and loads previous data
    manager = BudgetManager()
    manager.load_from_file("transactions.json")

    ## this keeps the menu running until the user chooses to exit
    while True:
        main_menu()
        choice = input("Select an option: ")

        ## this adds a new income or expense transaction
        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")
            trans_type = input("Type (income/expense): ").lower()
            t = Transaction(amount, category, description, trans_type)
            manager.add_transaction(t)

        ## this prints the current balance
        elif choice == "2":
            print("Current Balance: $", manager.get_balance())

        ## this shows a summary of totals grouped by category
        elif choice == "3":
            summary = manager.summary_by_category()
            for category, total in summary.items():
                print(f"{category}: ${total}")

        ## this saves the data and exits the program
        elif choice == "4":
            manager.save_to_file("transactions.json")
            print("Saved. Exiting.")
            break

        ## this warns the user of invalid inputs
        else:
            print("Invalid option. Try again.")

## this runs the app only if the script is executed directly
if __name__ == "__main__":
    run_cli()
