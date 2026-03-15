from ex4_linters.example import calculate_test_statistics


def test_regular():
    scores = [85, 92, 78, 45, 88, 67, 95, 54, 73, 81]
    result = calculate_test_statistics(scores)
    assert result["average"] == 75.8

def test_empty():
    scores = []
    result = calculate_test_statistics(scores)
    assert result["average"] == 0

def test_failed():
    scores = [1, 18, 28, 50]
    result = calculate_test_statistics(scores)
    assert result["failed"] == 4

def test_passed():
    scores = [70, 88, 98, 100]
    result = calculate_test_statistics(scores)
    assert result["passed"] == 4
