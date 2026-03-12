import requests

BASE_URL = "http://127.0.0.1:8000"

def categories_handler(user_option: int) -> None:
    match user_option:
        case 7:
            view_all_categories()
        case 8:
            add_category()
        case 9:
            delete_category()

def view_all_categories() -> None:
    print("===== All Categories =====")
    try:
        response = requests.get(f"{BASE_URL}/categories/")
        response.raise_for_status()
        all_categories = response.json()
        print("Category ID _ Category Name : Type\n")
        for cat_key, cat_type in all_categories.items():
            print(f"{cat_key} : {cat_type}")
    except Exception as e:
        print(f"[Error] something went wrong: {e}")

def add_category() -> None:
    print("===== Add New Category =====")
    name = input("Enter new category name: ")
    cat_type = input("Enter category type (income / expense): ") 
    new_category = {"name": name, "type": cat_type}
    try:
        response = requests.post(f"{BASE_URL}/categories/", json=new_category)
        response.raise_for_status()
        print("Category added successfully!")
    except Exception as e:
        print(f"[Error] something went wrong: {e}")

def delete_category() -> None:
    print("===== Delete Category =====")
    view_all_categories()
    print("=" * 10, end="\n")
    try:
        cat_id = int(input("Please enter category ID to delete: "))
        response = requests.delete(f"{BASE_URL}/categories/{cat_id}")
        response.raise_for_status()
        print("Category deleted successfully!")
    except Exception as e:
        print(f"[Error] something went wrong: {e}")