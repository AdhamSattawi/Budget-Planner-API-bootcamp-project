import requests
from datetime import date
from enum import IntEnum


BASE_URL = "http://127.0.0.1:8000"


class Txn(IntEnum):
    INCOME = 10
    EXPENSE = 11
    VIEW = 12
    DELETE = 13


def transactions_handler(user_option: int) -> None:
    match user_option:
        case Txn.INCOME:
            add_income_transaction()
        case Txn.EXPENSE:
            add_expense_transaction()
        case Txn.VIEW:
            view_all_transactions()
        case Txn.DELETE:
            delete_transaction()


def view_all_transactions() -> None:
    print("===== All Transactions =====")
    try:
        response = requests.get(f"{BASE_URL}/transactions/")
    except Exception as error:
        print(f"[Error] something went wrong: {error}")
    response.raise_for_status()
    all_transactions = response.json()
    print("ID | Type | Amount | Description | Category ID | Acccount ID | Date")
    print("-" * 10)
    for tx_id, tx_data in all_transactions.items():
        print(
            f"[{tx_id}] {tx_data[0]} : ${tx_data[1]} | {tx_data[2]} | "
            f"Cat:{tx_data[3]} | Acc:{tx_data[4]} | {tx_data[5]}"
        )


def add_income_transaction() -> None:
    print("===== Add Income Transaction =====")
    amount = input("Enter amount: ")
    desc = input("Enter description: ")
    cat_id = input("Enter Category ID: ")
    acc_id = input("Enter Account ID: ")
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date_input:
        date_input = date.today().isoformat()
    data = {
        "type": "income",
        "amount": amount,
        "description": desc,
        "category_id": cat_id,
        "account_id": acc_id,
        "created_on": date_input,
    }
    try:
        response = requests.post(f"{BASE_URL}/transactions/", json=data)
    except Exception as error:
        print(f"[Error] something went wrong: {error}")
    response.raise_for_status()
    print("Income transaction added successfully!\n")


def add_expense_transaction() -> None:
    print("===== Add Expense Transaction =====")
    amount = input("Enter amount: ")
    desc = input("Enter description: ")
    cat_id = input("Enter Category ID: ")
    acc_id = input("Enter Account ID: ")
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date_input:
        date_input = date.today().isoformat()
    data = {
        "type": "expense",
        "amount": amount,
        "description": desc,
        "category_id": cat_id,
        "account_id": acc_id,
        "created_on": date_input,
    }
    try:
        response = requests.post(f"{BASE_URL}/transactions/", json=data)
    except Exception as error:
        print(f"[Error] something went wrong: {error}")
    response.raise_for_status()
    print("Expense transaction added successfully!\n")


def delete_transaction() -> None:
    print("===== Delete Transaction =====")
    view_all_transactions()
    print("=" * 10, end="\n")
    tx_id = int(input("Please enter Transaction ID to delete: "))
    try:
        response = requests.delete(f"{BASE_URL}/transactions/{tx_id}")
    except Exception as error:
        print(f"[Error] something went wrong: {error}")
    response.raise_for_status()
    print("Transaction deleted successfully!\n")
