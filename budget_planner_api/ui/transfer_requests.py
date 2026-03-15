import requests
from datetime import date
from enum import IntEnum

BASE_URL = "http://127.0.0.1:8000"


class Trf(IntEnum):
    VIEW = 14
    ADD = 15
    DELETE = 16


def transfers_handler(user_option: int) -> None:
    match user_option:
        case Trf.VIEW:
            view_all_transfers()
        case Trf.ADD:
            add_transfer()
        case Trf.DELETE:
            delete_transfer()


def view_all_transfers() -> None:
    print("===== All Transfers =====")
    try:
        response = requests.get(f"{BASE_URL}/transfers/")
    except Exception as error:
        print(f"[Error] something went wrong: {error}")
    response.raise_for_status()
    all_transfers = response.json()
    print("ID | Sender Account | Receiver Account | Amount | Description | Date")
    print("-" * 10)
    for transfer_id, data in all_transfers.items():
        print(
            f"[{transfer_id}] Acc {data[0]} -> Acc {data[1]} :"
            f"${data[2]} | {data[3]} | {data[4]}"
        )


def add_transfer() -> None:
    print("===== Add New Transfer =====")
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
        "created_on": date_input,
    }
    try:
        response = requests.post(f"{BASE_URL}/transfers/", json=data)
    except Exception as error:
        print(f"[Error] something went wrong: {error}")
    response.raise_for_status()
    print("Transfer added successfully!\n")


def delete_transfer() -> None:
    print("===== Delete Transfer =====")
    view_all_transfers()
    print("=" * 10, end="\n")
    transfer_id = int(input("Please enter Transfer ID to delete: "))
    try:
        response = requests.delete(f"{BASE_URL}/transfers/{transfer_id}")
    except Exception as error:
        print(f"[Error] something went wrong: {error}")
    response.raise_for_status()
    print("Transfer deleted successfully!\n")
