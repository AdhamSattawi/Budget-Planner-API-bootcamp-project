# This function prints the variable types and their sizes for all primitive types in Python.

# int-float
# bool, None
# list-tuple
# str


def print_int():
    x1 = 999999999
    print(f"Type:{type(x1)}, Value:{x1}, Size:{x1.__sizeof__()}")
    x2 = 9999999999999999999999999999999
    print(f"Type:{type(x2)}, Value:{x2}, Size:{x2.__sizeof__()}")
    x3 = 99999999999999999999999999999999999999999999999999999999
    print(f"Type:{type(x3)}, Value:{x3}, Size:{x3.__sizeof__()}")
    x4 = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    print(f"Type:{type(x4)}, Value:{x4}, Size:{x4.__sizeof__()}")
    x5 = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    print(f"Type:{type(x5)}, Value:{x5}, Size:{x5.__sizeof__()}")


def print_float():
    x1 = 999999999.0
    print(f"Type:{type(x1)}, Value:{x1}, Size:{x1.__sizeof__()}")
    x2 = 9999999999999999999999999999999.0
    print(f"Type:{type(x2)}, Value:{x2}, Size:{x2.__sizeof__()}")
    x3 = 99999999999999999999999999999999999999999999999999999999.0
    print(f"Type:{type(x3)}, Value:{x3}, Size:{x3.__sizeof__()}")
    x4 = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.0
    print(f"Type:{type(x4)}, Value:{x4}, Size:{x4.__sizeof__()}")
    x5 = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.0
    print(f"Type:{type(x5)}, Value:{x5}, Size:{x5.__sizeof__()}")


def print_bool_none():
    x1 = True
    print(f"Type:{type(x1)}, Value:{x1}, Size:{x1.__sizeof__()}")
    x2 = False
    print(f"Type:{type(x2)}, Value:{x2}, Size:{x2.__sizeof__()}")
    x3 = None
    print(f"Type:{type(x2)}, Value:{x2}, Size:{x2.__sizeof__()}")


def print_list():
    x1 = []
    print(f"Type:{type(x1)}, Value:{x1}, Size:{x1.__sizeof__()}")
    x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Type:{type(x2)}, Value:{x2}, Size:{x2.__sizeof__()}")
    x3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    print(f"Type:{type(x3)}, Value:{x3}, Size:{x3.__sizeof__()}")
    x4 = [False, True, None]
    print(f"Type:{type(x4)}, Value:{x4}, Size:{x4.__sizeof__()}")
    x5 = [
        1,
        2,
        3,
        "B",
        "C",
        "D",
        False,
        True,
        (1, 2, 3),
        [
            [],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
            [False, True, None],
        ],
    ]
    print(f"Type:{type(x5)}, Value:{x5}, Size:{x5.__sizeof__()}")


def print_tuple():
    x1 = ()
    print(f"Type:{type(x1)}, Value:{x1}, Size:{x1.__sizeof__()}")
    x2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(f"Type:{type(x2)}, Value:{x2}, Size:{x2.__sizeof__()}")
    x3 = ("A", "B", "C", "D", "E", "F", "G", "H", "I")
    print(f"Type:{type(x3)}, Value:{x3}, Size:{x3.__sizeof__()}")
    x4 = (False, True, None)
    print(f"Type:{type(x4)}, Value:{x4}, Size:{x4.__sizeof__()}")
    x5 = (
        1,
        2,
        3,
        "B",
        "C",
        "D",
        False,
        True,
        (1, 2, 3),
        [
            [],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
            [False, True, None],
        ],
    )
    print(f"Type:{type(x5)}, Value:{x5}, Size:{x5.__sizeof__()}")


def print_str():
    x1 = ""
    print(f"Type:{type(x1)}, Value:{x1}, Size:{x1.__sizeof__()}")
    x2 = "[1,2,3,4,5,6,7,8,9]"
    print(f"Type:{type(x2)}, Value:{x2}, Size:{x2.__sizeof__()}")
    x3 = "[A,B,C,D,E,F,G,H,I]"
    print(f"Type:{type(x3)}, Value:{x3}, Size:{x3.__sizeof__()}")
    x4 = "[False,True,None]"
    print(f"Type:{type(x4)}, Value:{x4}, Size:{x4.__sizeof__()}")
    x5 = "[1,2,3,B,C,D,False,True,(1,2,3),[[],[1,2,3,4,5,6,7,8,9],[A,B,C,D,E,F,G,H,I],[False,True,None]]]"
    print(f"Type:{type(x5)}, Value:{x5}, Size:{x5.__sizeof__()}")


def print_types():
    print_int()
    print("===" * 30)
    print_float()
    print("===" * 30)
    print_bool_none()
    print("===" * 30)
    print_list()
    print("===" * 30)
    print_tuple()
    print("===" * 30)
    print_str()


print_types()
