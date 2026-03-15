from ex2_control_flow_types.student_grade_classifier import classify_grade
import pytest


def test_grade_A():
    result = classify_grade(95)
    assert result == 'A'

def test_grade_F():
    result = classify_grade(0)
    assert result == 'F'

def test_grade_error():
    with pytest.raises(ValueError):
        classify_grade(110)