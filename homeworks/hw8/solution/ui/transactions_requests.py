import requests
from datetime import date

BASE_URL = "http://127.0.0.1:8000"

def transactions_handler(user_option: int) -> None:
    match user_option:
        case 10:
            add_income_transaction()
        case 11:
            add_expense_transaction()
        case 12:
            view_all_transactions()  
        case 13:
            delete_transaction()  
 
def view_all_transactions() -> None:
    print("===== All Transactions =====")
    try: 
        response = requests.get(f"{BASE_URL}/transactions/")
        response.raise_for_status()
        all_transactions = response.json() 
        print("ID | Type | Amount | Description | Category ID | Acccount ID | Date")
        print("-" * 80)  
        for tx_id, tx_data in all_transactions.items():
            tx_type, amount, desc, cat_id, acc_id, created_on = tx_data    
            print(f"[{tx_id}] {tx_type} : ${amount} | {desc} | Cat:{cat_id} | Acc:{acc_id} | {created_on}") 
    except Exception as e:
        print(f"[Error] something went wrong: {e}")

def add_income_transaction() -> None:
    print("===== Add Income Transaction =====")
    try:
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
            "created_on": date_input
        }
        response = requests.post(f"{BASE_URL}/transactions/", json=data)
        response.raise_for_status()
        print("Income transaction added successfully!\n")
    except Exception as e:
        print(f"[Error] something went wrong: {e}")

def add_expense_transaction() -> None:
    print("===== Add Expense Transaction =====")
    try:
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
            "created_on": date_input
        }
        response = requests.post(f"{BASE_URL}/transactions/", json=data)
        response.raise_for_status()
        print("Expense transaction added successfully!\n")
    except Exception as e:
        print(f"[Error] something went wrong: {e}")

def delete_transaction() -> None:
    print("===== Delete Transaction =====")
    view_all_transactions() 
    print("=" * 10, end="\n")
    try:
        tx_id = int(input("Please enter Transaction ID to delete: "))
        response = requests.delete(f"{BASE_URL}/transactions/{tx_id}")
        response.raise_for_status()
        print("Transaction deleted successfully!\n")
    except Exception as e:
        print(f"[Error] something went wrong: {e}")