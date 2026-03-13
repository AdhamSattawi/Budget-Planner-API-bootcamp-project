import requests

BASE_URL = "http://127.0.0.1:8000"


def accounts_handler(user_option: int) -> None:
    match user_option:
        case 1:
            view_all_accounts()
        case 2:
            view_single_balance()
        case 3:
            add_account()
        case 4:
            edit_account_name()
        case 5:
            delete_account()
        case 6:
            view_net_worth()


def view_all_accounts() -> None:
    print("===== All Accounts =====")
    try:
        response = requests.get(f"{BASE_URL}/accounts/")
    except Exception as error:
        print(f"[Error] something went wrong: {error}")
    response.raise_for_status()
    all_accounts = response.json()
    print("Account ID _ Account Name : Current Balance $\n")
    for acc_key, balance in all_accounts.items():
        print(f"{acc_key} : ${balance}")


def view_single_balance() -> None:
    print("===== Account =====")
    view_all_accounts()
    print("=" * 10, end="\n")
    acc_id = int(input("Please enter account id from the list above: "))
    try:
        response = requests.get(f"{BASE_URL}/accounts/{acc_id}")
    except Exception as error:
        print(f"[Error] something went wrong: {error}")
    response.raise_for_status()
    account = response.json()
    print(f"Account Balance: ${account["account_balance"]}")


def add_account() -> None:
    print("===== Add New Account =====")
    name = input("Enter new account name: ")
    balance = input("Enter opening balance: ")
    new_account = {"name": name, "opening_balance": balance}
    try:
        response = requests.post(f"{BASE_URL}/accounts/", json=new_account)
    except Exception as error:
        print(f"[Error] something went wrong: {error}")
    response.raise_for_status()
    print("Account added successfully!")


def edit_account_name() -> None:
    print("===== Edit Account Name =====")
    view_all_accounts()
    print("=" * 10, end="\n")
    acc_id = int(input("Please enter account id from the list above: "))
    new_name = input("Enter the new account name: ")
    new_acc = {"new_name": new_name}
    try:
        response = requests.put(f"{BASE_URL}/accounts/{acc_id}", json=new_acc)
    except Exception as error:
        print(f"[Error] something went wrong: {error}")
    response.raise_for_status()
    print("Account name updated successfully!")


def delete_account() -> None:
    print("===== Delete Account =====")
    view_all_accounts()
    print("=" * 10, end="\n")
    acc_id = int(input("Please enter account id to delete: "))
    try:
        response = requests.delete(f"{BASE_URL}/accounts/{acc_id}")
    except Exception as error:
        print(f"[Error] something went wrong: {error}")
    response.raise_for_status()
    print("Account deleted successfully!")


def view_net_worth() -> None:
    print("===== Net Worth =====")
    try:
        response = requests.get(f"{BASE_URL}/accounts/net_worth")
    except Exception as error:
        print(f"[Error] something went wrong: {error}")
    response.raise_for_status()
    data = response.json()
    print(f"Total Net Worth: ${data['net_worth']}")
