from solution.ui.account_requests import accounts_handler
from solution.ui.category_requests import categories_handler
from solution.ui.transactions_requests import transactions_handler
from solution.ui.transfer_requests import transfers_handler


def handle_action(user_option: int):
    if 1 <= user_option <= 6 :
        accounts_handler(user_option)
    elif 7 <= user_option <= 9:
        categories_handler(user_option)
    elif 10 <= user_option <= 13:
        transactions_handler(user_option)
    else:
        transfers_handler(user_option)