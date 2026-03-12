import requests
from datetime import date


BASE_URL = "http://127.0.0.1:8000"

def transfers_handler(user_option):
    match user_option:
        case 14:
            view_all_transfers()
        case 15:
            add_transfer()
        case 16:
            delete_transfer()

def view_all_transfers() -> None:
    print("===== All Transfers =====")
    try:
        response = requests.get(f"{BASE_URL}/transfers/")
        response.raise_for_status()
        all_transfers = response.json()
        print("ID | Sender Account | Receiver Account | Amount | Description | Date")
        print("-" * 65)
        for transfer_id, data in all_transfers.items():
            sender, receiver, amount, desc, created_on = data
            print(f"[{transfer_id}] Acc {sender} -> Acc {receiver} : ${amount} | {desc} | {created_on}")
    except Exception as e:
        print(f"[Error] something went wrong: {e}")

def add_transfer() -> None:
    print("===== Add New Transfer =====")
    try:
        sender_id = input("Enter Sender Account ID: ")
        receiver_id = input("Enter Receiver Account ID: ")
        amount = input("Enter transfer amount: ")
        description = input("Enter description: ")
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
        if not date_input:
            date_input = date.today().isoformat()
        data = {
            "sender_id": sender_id,
            "receiver_id": receiver_id,
            "amount": amount,
            "description": description,
            "created_on": date_input
        }
        response = requests.post(f"{BASE_URL}/transfers/", json=data)
        response.raise_for_status()
        print("Transfer added successfully!\n")
    except Exception as e:
        print(f"[Error] something went wrong: {e}")

def delete_transfer() -> None:
    print("===== Delete Transfer =====")
    view_all_transfers() 
    print("=" * 10, end="\n")
    try:
        transfer_id = int(input("Please enter Transfer ID to delete: "))
        response = requests.delete(f"{BASE_URL}/transfers/{transfer_id}")
        response.raise_for_status()
        print("Transfer deleted successfully!\n")
    except Exception as e:
        print(f"[Error] something went wrong: {e}")