from ex2_control_flow_types.number_pattern_generator import generate_pyramid
import pytest

def test_max_floors():
    result = generate_pyramid(3)
    assert result == '  1\n 121\n12321\n'

def test_low_height_invalid():
    with pytest.raises(ValueError):
        generate_pyramid(0)

def test_high_height_invalid():
    with pytest.raises(ValueError):
        generate_pyramid(10)