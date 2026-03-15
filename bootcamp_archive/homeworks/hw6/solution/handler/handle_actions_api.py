from core_functions.actions_api import (
    add_expense,
    add_income,
    view_expense,
    view_income,
    view_summary,
    remove,
    clear_all,
)


def handle_action(user_option: int) -> None:
    if user_option in range(1, 3):
        handle_adding(user_option)
    elif user_option in range(3, 6):
        handle_view(user_option)
    elif user_option in range(6, 9):
        handle_removing(user_option)
    else:
        raise ValueError("Wrong Option, please select the proper number from the list.")


def handle_adding(user_option: int) -> None:
    match user_option:
        case 1:
            add_income()
        case 2:
            add_expense()


def handle_view(user_option: int) -> None:
    match user_option:
        case 3:
            view_income()
        case 4:
            view_expense()
        case 5:
            view_summary()


def handle_removing(user_option: int) -> None:
    match user_option:
        case 6:
            remove("income")
        case 7:
            remove("expense")
        case 8:
            clear_all()
