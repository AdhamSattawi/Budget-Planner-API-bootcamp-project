from user_interface.user_input import income_input, expense_input, remove_input
import requests

BASE_URL = "http://127.0.0.1:8000"

def add_income() -> None:
    try:
        income_amount, income_description = income_input()
        data = {"amount" : income_amount, "description" : income_description}
        requests.post(f"{BASE_URL}/income",json = data)
        print("Income successfully added!")
    except Exception as e:
        print(f"Something went wrong! {e}")


def add_expense() -> None:
    try:
        expense_amount, expense_description = expense_input()
        data = {"amount" : expense_amount, "description" : expense_description}
        requests.post(f"{BASE_URL}/expense",json = data)
        print("expense successfully added!")
    except Exception as e:
        print(f"Something went wrong! {e}")


def remove(activity_type: str) -> None:
    try:
        id = remove_input()
        requests.delete(f"{BASE_URL}/{activity_type}/{id}")
        print("Successfully Removed!")
    except Exception as e:
        print(f"Something went wrong! {e}")


def clear_all() -> None:
    try:
        requests.delete(f"{BASE_URL}/clear")
        print("All Data Has Been Removed!")
    except Exception as e:
        print(f"Something went wrong! {e}")


def view_income() -> None:
    try:
        response = requests.get(f"{BASE_URL}/income")
        incomes = response.json()
        print("----------INCOMES---------")
        if not incomes:
            print("No incomes yet!")
        else:
            for id, data in incomes.items():
                print(f"[{id}] [${data["amount"]}] {data["description"]}")
    except Exception as e:
        print(f"Something went wrong! {e}")


def view_expense() -> None:
    try:
        response = requests.get(f"{BASE_URL}/expense")
        expenses = response.json()
        print("----------EXPENSES---------")
        if not expenses:
            print("No expenses yet!")
        else:
            for id, data in expenses.items():
                print(f"[{id}] [-${data["amount"]}] {data["description"]}")
    except Exception as e:
        print(f"Something went wrong! {e}")



def view_summary() -> None:
    try:
        print("----------SUMMARY---------")
        response = requests.get(f"{BASE_URL}/summary")
        summary_data = response.json()
        print(f"""
        Total Incomes: {summary_data["Total Incomes"]}
        Total Expenses: {summary_data["Total Expenses"]}
        Remaning Budget: {summary_data["Remaning Budget"]}
        +++++++++++++++++++++++++++++++++++++++
        """)
    except Exception as e:
        print(f"Something went wrong! {e}")