from solution.ui.prints import welcome_message, menu, user_selection
from solution.ui.handler import handle_action


def budget_app_start() -> None:
    """This function runs the UI"""
    welcome_message()

    while True:
        menu()
        user_option = user_selection()
        if user_option == 0:
            print("Saving your data....Good Bye!")
            break
        try:
            handle_action(user_option)
        except Exception as error:
            print(f"[error] {error}")
            print("Please try again.")


if __name__ == "__main__":
    budget_app_start()
