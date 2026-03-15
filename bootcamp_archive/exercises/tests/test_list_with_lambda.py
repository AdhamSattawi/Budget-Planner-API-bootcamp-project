from ex3_functions.list_operations_with_lambda import get_names, filter_adults, sort_by_age

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30},
    {"name": "Diana", "age": 18}
]

def test_filter_adults():
    result = filter_adults(people)
    assert result[2]["age"] == 18

def test_get_names():
    result = get_names(people)
    assert result[0] == "Alice"

def test_sort_by_age():
    result = sort_by_age(people)
    assert result[0]["name"] == "Charlie"