import pytest
from solution.ex2_fibonaccci_cal import fibonacci


@pytest.mark.parametrize("number, expected",
    [(10, 34),
    (50, 7778742049),
    (100,218922995834555169026),
    (200, 173402521172797813159685037284371942044301)]
)


def test_fibonacci(number, expected):
    assert fibonacci(number) == expected

def test_zero():
    with pytest.raises(ValueError):
        fibonacci(0)