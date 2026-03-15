# This is a simple command-line calculator that performs basic arithmetic operations: addition, subtraction, multiplication, and division.


def parsing_input(user_input: str) -> str | int | float:
    input_parts = user_input.lower().strip().split()
    match input_parts[0]:  # operation
        case "add":
            return add(input_parts[1], input_parts[3])  # number 1 and number 2
        case "subtract":
            return subtract(input_parts[1], input_parts[3])
        case "multiply":
            return multiply(input_parts[1], input_parts[3])
        case "divide":
            return divide(input_parts[1], input_parts[3])
        case "help":
            return help()
        case _:
            return "Wrong input, Please see 'help'"


def decimal_validation(num1: str, num2: str) -> None:
    try:
        float(num1)
        float(num2)
    except ValueError:
        raise ValueError("please enter valid numbers.")


def add(num1: str, num2: str) -> str:
    decimal_validation(num1, num2)
    result = int(num1) + int(num2)
    return f"The answer is {result}"


def subtract(num1: str, num2: str) -> str:
    decimal_validation(num1, num2)
    result = int(num2) - int(num1)  # subtract num1 from num2
    return f"The answer is {result}"


def multiply(num1: str, num2: str) -> str:
    decimal_validation(num1, num2)
    result = int(num1) * int(num2)
    return f"The answer is {result}"


def divide(num1: str, num2: str) -> str:
    decimal_validation(num1, num2)
    if int(num2) == 0:
        raise ZeroDivisionError("Can't divide by 0.")
    result = float(num1) / float(num2)
    return f"The answer is {result}"


def help() -> str:
    help_text = """
    -------------------------------------------------------
    COMMAND LINE CALCULATOR INSTRUCTIONS:
    Format: [operation] [number] [connector] [number]
    Examples:
    - add 10 to 5          (Result: 15)
    - subtract 5 from 10   (Result: 5)
    - multiply 3 by 4      (Result: 12)
    - divide 20 by 5       (Result: 4.0)
    Type 'exit' to quit.
    -------------------------------------------------------
    """
    return help_text


def simple_calculator() -> None:
    print("--- Welcome to MY SIMPLE CALCULATOR---")
    while True:
        print("Please provide the prompt. Type 'help' for syntax or 'exit' to quit.")
        user_input = input()
        if user_input == "exit":
            print("Goodbye!")
            break
        result = parsing_input(user_input)
        print(result)
        print("=====" * 10)


if __name__ == "__main__":
    simple_calculator()
