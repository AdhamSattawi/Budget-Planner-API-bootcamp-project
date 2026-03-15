from ex5_classes.vector_class import Vector2D


def test_operator_overloading():
    v1 = Vector2D(3.0, 4.0)
    v2 = Vector2D(1.0, 2.0)
    assert v1.__str__() == "Vector2D(3.0, 4.0)"
    
    assert v1 +v2 == Vector2D(4.0, 6.0)

def test_eq():
    v1 = Vector2D(3.0, 4.0)
    v2 = Vector2D(1.0, 2.0)
    assert v1.__eq__(v2) == False

def test_zero_negative():
    v_zero = Vector2D(0, 0)
    v_one = Vector2D(3, 4)
    assert abs(v_zero) == 0.0
    result = v_one + v_zero
    assert result == v_one
    assert v_one.dot(v_zero) == 0.0
