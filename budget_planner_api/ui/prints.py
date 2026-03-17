def welcome_message() -> None:
    print("========================================")
    print("      💰 BUDGET PLANNER API 💰       ")
    print("========================================")
    print("Welcome! Connecting to your database...")
    print("========================================\n")


def menu() -> None:
    """Display the main menu options."""
    menu_text = """
--- 🏦 ACCOUNTS & WEALTH ---
 1. View all accounts & balances
 2. View a single account's balance
 3. Add a new account
 4. Edit an account's name
 5. Delete an account
 6. View your Net Worth

--- 📂 CATEGORIES ---
 7. View all categories
 8. Add a new category
 9. Delete a category

--- 💸 TRANSACTIONS & TRANSFERS ---
10. Add an Income transaction
11. Add an Expense transaction
12. View all transactions
13. Delete a transaction
14. View all transfers
15. Add a new transfer
16. Delete a transfer

----------------------------------------
 0. Exit Application
----------------------------------------
"""
    print(menu_text)


def user_selection() -> int:
    while True:
        try:
            choice = int(input("Select an option (0-16): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        max_option_munber = 16
        if 0 <= choice <= max_option_munber:
            return choice
        print("Invalid choice. Please select a number between 0 and 15.")
