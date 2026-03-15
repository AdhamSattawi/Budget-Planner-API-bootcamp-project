from solution.ex2_simple_calculator import parsing_input, add, subtract, multiply, divide
import pytest


@pytest.mark.parametrize("user_input, expected",
    [("add 2 to 5", "The answer is 7"),
    ("subtract 2 from 5", "The answer is 3"),
    ("multiply 2 by 5","The answer is 10"),
    ("divide 10 by 5", "The answer is 2.0")]
)


def test_parsing_input(user_input, expected):
    assert parsing_input(user_input) == expected

def test_subtract():
    assert subtract("10", "50") == "The answer is 40"

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Can't divide by 0."):
        divide("10", "0")

def test_invalid_number_input():
    with pytest.raises(ValueError, match="please enter valid numbers."):
        add("apple", "5")
