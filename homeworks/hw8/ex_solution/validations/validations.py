def valid_option(option: str) -> bool:
    if not option.isdigit():
        raise ValueError("Wrong option number.")
    if not (1 <= int(option) <= 9):
        raise ValueError("Wrong option number.")
    return True


def valid_adding(amount: str, desc: str) -> bool:
    try:
        float(amount)
    except ValueError:
        raise ValueError("Amount must be a number.")
    if float(amount) < 0:
        raise ValueError("Amount must be greater than zero.")
    if desc == "":
        raise ValueError("Enter a description")
    return True


def valid_id(item_id: str) -> bool:
    if not item_id.isdigit():
        raise ValueError("ID must be a number")
    if int(item_id) < 0:
        raise ValueError("ID must be greater than zero.")
    return True


def valid_description(desc: str) -> bool:
    if desc == "":
        raise ValueError("Enter a description")
    return True
