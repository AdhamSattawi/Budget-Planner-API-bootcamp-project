from ex2_control_flow_types.temperature_converter_with_validation import convert_temperature
import pytest

def test_converting_C_to_K():
    result = convert_temperature(100,'C','K')
    assert result == 373.15

def test_converting_K_to_C():
    result = convert_temperature(100,'K','C')
    assert result == pytest.approx(-173.15)

def test_converting_C_to_F():
    result = convert_temperature(0,'C','F')
    assert result == 32.0

def test_converting_F_to_C():
    result = convert_temperature(32,'F','C')
    assert result == 0

def test_converting_C_to_C():
    result = convert_temperature(0,'C','C')
    assert result == 0

def test_invalid_type():
    with pytest.raises(ValueError):
        convert_temperature(32,'A','B')