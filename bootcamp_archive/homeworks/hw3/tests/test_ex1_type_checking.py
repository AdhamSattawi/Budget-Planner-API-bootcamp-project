from solution.ex1_type_checking_dec import type_check
import pytest


@type_check
def format_data(name: str, age: int, data: dict, other_info = None) -> str:
    other_info_str = ', Other Info : ' + str(other_info) if other_info else ''
    return f"Name: {name}, Age: {age}, Data: {data['key']}{other_info_str}"

def test_type_check():
    result = format_data("Alice", 30, {"key": "value"}, 1234)
    expected = "Name: Alice, Age: 30, Data: value, Other Info : 1234"
    assert result == expected

def test_value_error():
    with pytest.raises(TypeError):
        format_data("Alice", "thirty", {"key": "value"})