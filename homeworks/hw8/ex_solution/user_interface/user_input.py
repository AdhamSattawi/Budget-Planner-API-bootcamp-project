from validations.validations import valid_option, valid_adding, valid_id


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
    item_id = input("Please enter the ID: ").strip()
    if valid_id(item_id):
        return (item_id)
    raise ValueError("Wrong input")
