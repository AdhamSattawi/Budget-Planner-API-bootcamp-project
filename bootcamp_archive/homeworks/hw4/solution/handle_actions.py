from budget import Budget
from actions import (
    add_expense,
    add_income,
    view_expense,
    view_income,
    view_summary,
    remove,
    clear_all,
)


def handle_action(user_option: int, my_budget: Budget) -> None:
    if user_option in range(1, 3):
        handle_adding(user_option, my_budget)
    elif user_option in range(3, 6):
        handle_view(user_option, my_budget)
    elif user_option in range(6, 9):
        handle_removing(user_option, my_budget)
    else:
        raise ValueError("Wrong Option, please select the proper number from the list.")


def handle_adding(user_option: int, my_budget: Budget) -> None:
    match user_option:
        case 1:
            add_income(my_budget)
        case 2:
            add_expense(my_budget)


def handle_view(user_option: int, my_budget: Budget) -> None:
    match user_option:
        case 3:
            view_income(my_budget)
        case 4:
            view_expense(my_budget)
        case 5:
            view_summary(my_budget)


def handle_removing(user_option: int, my_budget: Budget) -> None:
    match user_option:
        case 6:
            remove("income", my_budget)
        case 7:
            remove("expense", my_budget)
        case 8:
            clear_all(my_budget)
