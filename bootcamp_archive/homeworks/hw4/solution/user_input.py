from validations import valid_option, valid_adding, valid_id, valid_description


def user_selection() -> int:
    option = input("Choose an option: ").strip()
    if valid_option(option):
        return int(option)
    else:
        raise ValueError("Wrong option number.")

def income_input() -> tuple:
    amount = input("Please enter income amount: ").strip()
    desc = input("Please enter income description: ").strip()
    if valid_adding(amount, desc):
        return (float(amount), desc)
    else:
        raise ValueError("Wrong input.")


def expense_input() -> tuple:
    amount = input("Please enter expense amount: ").strip()
    desc = input("Please enter expense description: ").strip()
    if valid_adding(amount, desc):
        return (float(amount), desc)
    else:
        raise ValueError("Wrong input.")


def remove_input() -> tuple:
    remove_type = input(
        "Enter 1 to remove by item ID, or 2 to remove by description: "
    ).strip()
    if remove_type == "1":
        item_id = input("Please enter the ID: ").strip()
        if valid_id(item_id):
            return (remove_type, item_id)
    elif remove_type == "2":
        item_description = input("Please enter the description: ").strip()
        item_description = item_description
        if valid_description(item_description):
            return (remove_type, item_description)
    raise ValueError("Wrong input")
