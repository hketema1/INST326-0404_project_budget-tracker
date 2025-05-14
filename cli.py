"""
cli.py

Command-line interface for the Budget Tracker app aka 'CashFlowr💸'

This allows users to add and manage financial transactions, view summaries, 
and visualize spending via charts using matplotlib.

"""

from budget_manager import BudgetManager
from transaction import Transaction
import matplotlib.pyplot as plt

def main_menu():
    """
    Displays the main menu of options for the user.
    """
    print("\n******* Welcome to CashFlowr💸 *******")
    print("1. Add a Transaction")
    print("2. View Current Balance")
    print("3. View Summary by Category")
    print("4. View All Transactions")
    print("5. Save and Exit")
    print("6. Visualize Summary Chart")
    print("*****************************")

def get_float_input(prompt):
    """
    Prompts the user for a float input and validates it.

    Args:
        prompt (str): The input prompt to display.

    Returns:
        float: The validated float input from the user.
    """
    while True:
        try:
            value = float(prompt_user(prompt))
            if value < 0:
                print("Amount cannot be negative. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_type_input(prompt):
    """
    Prompts the user to enter a valid transaction type.

    Args:
        prompt (str): The input prompt to display.

    Returns:
        str: 'income' or 'expense'
    """
    while True:
        trans_type = prompt_user(prompt).strip().lower()
        if trans_type in ["income", "expense"]:
            return trans_type
        print("Invalid type. Please enter 'income' or 'expense'.")

def prompt_user(message):
    """
    Handles user input for consistency.

    Args:
        message (str): The prompt to display to the user.

    Returns:
        str: User's input string.
    """
    return input(message)

def plot_summary(summary):
    """
    Displays a chart (bar or pie) of the summary totals by category.

    Args:
        summary (dict): A dictionary containing category totals.
    """
    ### This checks if there is data to visualize
    if not summary:
        print("No data to display. Add some transactions first.")
        return

    print("\n📈 Choose a chart type:")
    print("1. Bar chart")
    print("2. Pie chart")
    chart_choice = input("Enter 1 or 2: ").strip()

    categories = list(summary.keys())
    amounts = list(summary.values())

    if chart_choice == "1":
        ### This creates a bar chart of category totals
        plt.figure(figsize=(8, 5))
        plt.bar(categories, amounts, color="skyblue")
        plt.title("Summary by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Amount")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    elif chart_choice == "2":
        ### This creates a pie chart of category proportions
        plt.figure(figsize=(6, 6))
        plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
        plt.title("Spending Breakdown by Category")
        plt.axis("equal")
        plt.tight_layout()
        plt.show()
    else:
        print("❗ Invalid input. Returning to main menu.")

def run_cli():
    """
    This runs the main loop of the command-line interface.
    """
    ### This initializes the budget manager
    manager = BudgetManager()

    ### This prompts the user to load or create a JSON file
    filename = input("📁 Enter filename to load (or press Enter for 'transactions.json'): ").strip()
    if not filename:
        filename = "transactions.json"

    manager.load_from_file(filename)
    print(f"\n✅ Loaded: {filename}")

    while True:
        main_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            ### This handles creating and storing a new transaction
            amount = get_float_input("Enter the amount: ")
            category = input("Enter the category (e.g., Food, Rent, Salary): ").strip()
            description = input("Enter a description: ").strip()
            trans_type = get_type_input("Enter the type ('income' or 'expense'): ")
            t = Transaction(amount, category, description, trans_type)
            manager.add_transaction(t)
            print(f"\n✅ Transaction added successfully!")

        elif choice == "2":
            ### This displays the current balance
            print(f"\n💵 Current Balance: ${manager.get_balance():.2f}")

        elif choice == "3":
            ### This displays a summary by category
            print("\n📊 Summary by Category:")
            summary = manager.summary_by_category()
            if not summary:
                print("No transactions to summarize.")
            else:
                for category, total in summary.items():
                    print(f"- {category}: ${total:.2f}")

        elif choice == "4":
            ### This lists all transactions with details
            print("\n🧾 All Transactions:")
            if not manager.transactions:
                print("No transactions recorded yet.")
            else:
                for idx, t in enumerate(manager.transactions, 1):
                    print(f"{idx}. {t.trans_type.title()}: ${t.amount:.2f} | {t.category} | {t.description}")

        elif choice == "5":
            ### This saves the data and exits the program
            manager.save_to_file(filename)
            print(f"\n💾 Saved to {filename}. Goodbye!")
            break

        elif choice == "6":
            ### This generates a bar or pie chart of category totals
            summary = manager.summary_by_category()
            plot_summary(summary)

        else:
            print("❗ Invalid option. Please select a number between 1 and 6.")

if __name__ == "__main__":
    run_cli()
