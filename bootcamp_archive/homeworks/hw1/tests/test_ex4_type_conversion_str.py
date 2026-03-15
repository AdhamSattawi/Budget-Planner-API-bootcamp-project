from solution.ex4_type_conversion_str import binary_to_dec

def test_bin_to_dec():
    binary = "1101"
    expected = 13
    assert binary_to_dec(binary) == expected

def test_one_int():
    binary = "1"
    expected = 1
    assert binary_to_dec(binary) == expected

def test_zero():
    binary = "0"
    expected = 0
    assert binary_to_dec(binary) == expected