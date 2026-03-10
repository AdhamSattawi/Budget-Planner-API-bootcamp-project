from budget import Budget
from cli_prints import welcome_message, options
from handle_actions import handle_action
from user_input import user_selection


def budget_app_start() -> None:
    """This function runs the UI"""
    my_budget = Budget()
    print(welcome_message())
    while True:
        try:
            print(options())
            user_option = user_selection()
            if user_option == 9:
                print("Good Bye!")
                break
            handle_action(user_option, my_budget)
        except Exception as e:
            print(f"[error] {e}")
            print("Please try again.")
