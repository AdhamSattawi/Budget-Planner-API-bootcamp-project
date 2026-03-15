from ex3_functions.calculate_statistics import calculate_statistics

def test_empty():
    result = calculate_statistics(math=[])
    assert result['math']['sum'] == None
    assert result['math']['average'] == None
    assert result['math']['min'] == None
    assert result['math']['max'] == None

def test_standard():
    result = calculate_statistics(math=[10,20,30])
    assert result['math']['sum'] == 60
    assert result['math']['average'] == 20
    assert result['math']['min'] == 10
    assert result['math']['max'] == 30

def test_multi():
    result = calculate_statistics(math=[10,20,30], science=[42,35,65,32], sport=[100,4020,5390,333333])
    assert result['math']['sum'] == 60
    assert result['science']['sum'] == 174
    assert result['sport']['max'] == 333333

def test_single():
    result = calculate_statistics(math=[8])
    assert result['math']['sum'] == 8
    assert result['math']['average'] == 8
    assert result['math']['min'] == 8
    assert result['math']['max'] == 8

