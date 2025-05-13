"""
cli.py

Handles user interactions via the command line for Budget Tracker aka 'CashFlowr'
"""

from budget_manager import BudgetManager
from transaction import Transaction

def main_menu():
    print("\n******* Budget Tracker *******")
    print("1. Add a Transaction")
    print("2. View Current Balance")
    print("3. View Summary by Category")
    print("4. View All Transactions")
    print("5. Save and Exit")
    print("*****************************")

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Amount cannot be negative. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_type_input(prompt):
    while True:
        trans_type = input(prompt).strip().lower()
        if trans_type in ["income", "expense"]:
            return trans_type
        print("Invalid type. Please enter 'income' or 'expense'.")

def run_cli():
    manager = BudgetManager()

    # Ask user which file to load
    filename = input(" Enter filename to load (or press Enter for 'transactions.json'): ").strip()
    if not filename:
        filename = "transactions.json"

    manager.load_from_file(filename)
    print(f"\n Loaded: {filename}")

    while True:
        main_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            amount = get_float_input("Enter the amount: ")
            category = input("Enter the category (e.g., Food, Rent, Salary): ").strip()
            description = input("Enter a description: ").strip()
            trans_type = get_type_input("Enter the type ('income' or 'expense'): ")
            t = Transaction(amount, category, description, trans_type)
            manager.add_transaction(t)
            print(f"\n Transaction added successfully!")

        elif choice == "2":
            print(f"\n Current Balance: ${manager.get_balance():.2f}")

        elif choice == "3":
            print("\n Summary by Category:")
            summary = manager.summary_by_category()
            if not summary:
                print("No transactions to summarize.")
            else:
                for category, total in summary.items():
                    print(f"- {category}: ${total:.2f}")

        elif choice == "4":
            print("\n All Transactions:")
            if not manager.transactions:
                print("No transactions recorded yet.")
            else:
                for idx, t in enumerate(manager.transactions, 1):
                    print(f"{idx}. {t.trans_type.title()}: ${t.amount:.2f} | {t.category} | {t.description}")

        elif choice == "5":
            manager.save_to_file(filename)
            print(f"\n Saved to {filename}. Goodbye!")
            break

        else:
            print("Invalid option. Please select a number between 1 and 5.")

if __name__ == "__main__":
    run_cli()
