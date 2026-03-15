people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30},
    {"name": "Diana", "age": 16},
    {"name": "Alex", "age": 14}
]

def filter_adults(people: list[dict]) -> list[dict]:
    old_people = list(filter(lambda someone: someone["age"] >= 18, people))
    return old_people

def get_names(people: list[dict]) -> list[dict]:
    names = list(map(lambda person: person["name"], people))
    return names

def sort_by_age(people: list[dict]) -> list[dict]:
    people.sort(reverse = True, key = lambda person: person["age"])
    return people

if __name__ == "__main__":
    print(filter_adults(people))
    print(get_names(people))
    print(sort_by_age(people))