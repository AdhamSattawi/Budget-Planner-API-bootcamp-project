from budget import Budget
from user_input import income_input, expense_input, remove_input


def add_income(my_budget: Budget) -> None:
    income_amount, income_description = income_input()
    my_budget.add_income(income_amount, income_description)
    print("Income successfully added!")


def add_expense(my_budget: Budget) -> None:
    expense_amount, expense_description = expense_input()
    my_budget.add_expense(expense_amount, expense_description)
    print("expense successfully added!")


def view_income(my_budget: Budget) -> None:
    incomes = my_budget.view_incomes()
    print("----------INCOMES---------")
    if not incomes:
        print("No incomes yet!")
    print(incomes)


def view_expense(my_budget: Budget) -> None:
    expenses = my_budget.view_expenses()
    print("----------EXPENSES---------")
    if not expenses:
        print("No expenses yet!")
    print(expenses)


def view_summary(my_budget: Budget) -> None:
    incomes = my_budget.view_incomes()
    expenses = my_budget.view_expenses()
    print("----------SUMMARY---------")
    total_income, total_expense, remaning_budget = (
        my_budget.view_summary()
    )
    print(f"""
    All Recorded Incomes: {incomes}
    All Recorded Expenses: {expenses}
    Total Incomes: {total_income}
    Total Expenses: {total_expense}
    Remaning Budget: {remaning_budget}
    +++++++++++++++++++++++++++++++++++++++
    """)


def remove(activity_type: str, my_budget: Budget) -> None:
    match activity_type:
        case "income":
            remove_type, content = remove_input()
            if remove_type == "1":
                my_budget.remove_by_id("income", int(content))
            else:
                my_budget.remove_by_description("income", content)
        case "expense":
            remove_type, content = remove_input()
            if remove_type == "1":
                my_budget.remove_by_id("expense", int(content))
            else:
                my_budget.remove_by_description("expense", content)
    print("Successfully Removed!")


def clear_all(my_budget: Budget) -> None:
    my_budget.clear_all()
    print("All Data Has Been Removed!")
