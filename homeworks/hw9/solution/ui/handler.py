from solution.ui.account_requests import accounts_handler
from solution.ui.category_requests import categories_handler
from solution.ui.transactions_requests import transactions_handler
from solution.ui.transfer_requests import transfers_handler

TRANSACTION_END = 14
ACCOUNT_OPTIONS = range(1, 7)
CATEGORY_OPTIONS = range(7, 10)
TRANSACTION_OPTIONS = range(10, TRANSACTION_END)


def handle_action(user_option: int) -> None:
    if user_option in ACCOUNT_OPTIONS:
        accounts_handler(user_option)
    elif user_option in CATEGORY_OPTIONS:
        categories_handler(user_option)
    elif user_option in TRANSACTION_OPTIONS:
        transactions_handler(user_option)
    else:
        transfers_handler(user_option)
