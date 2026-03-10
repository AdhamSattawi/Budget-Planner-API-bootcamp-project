from user_interface.cli_prints import welcome_message, options
from handler.handle_actions_api import handle_action
from user_interface.user_input import user_selection


def budget_app_start() -> None:
    """This function runs the UI"""
    print(welcome_message())
    while True:
        try:
            print(options())
            user_option = user_selection()
            if user_option == 9:
                print("Good Bye!")
                break
            handle_action(user_option)
        except Exception as e:
            print(f"[error] {e}")
            print("Please try again.")
