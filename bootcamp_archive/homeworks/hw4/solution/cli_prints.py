def welcome_message() -> str:
    welcome_message = """
        +++++++++++++++++++++++++++++++++++++++++
        Welocme to Adham's Budget Planner App $$$
        +++++++++++++++++++++++++++++++++++++++++
        Track your income, manage expenses,
        and keep your finances in balance.
        """
    return welcome_message


def options() -> str:
    options_message = """
        =========================================
        =============Budget Planner v1===========

        Please select option number:
        1. Add Income
        2. Add Expense
        3. View Incomes
        4. View Expenses
        5. View Summary
        6. Remove Income
        7. Remove Expense
        8. Clear All Data
        9. Exit

        """
    return options_message
