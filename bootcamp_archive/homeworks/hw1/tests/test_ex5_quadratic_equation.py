from solution.ex5_quadratic_equation import quadratic

def test_quadratic_equation():
    assert quadratic(1, -3, 2) == "x1 = 1.00, x2 = 2.00"

def test_zero():
    assert quadratic(1, 0, 0) == "x1 = 0.00, x2 = 0.00"

def test_negative():
    assert quadratic(-3, -5, -7) == "x1 =-0.83+1.28j, x2 =-0.83-1.28j"