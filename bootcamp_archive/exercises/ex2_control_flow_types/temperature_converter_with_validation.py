
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    valid_unit = ['C','F','K']
    if from_unit not in valid_unit or to_unit not in valid_unit:
        raise ValueError( "Invalid unit. Use 'C', 'F', or 'K'.")
    elif from_unit == 'K' and value < 0:
        raise ValueError ("Kelvin cannot be negative.")
    elif from_unit == 'C' and value < -273.15:
        raise ValueError("Temperature below absolute zero.")
    elif from_unit == to_unit:
        return value
    else:
        return temp_converter(value, from_unit, to_unit)

def temp_converter(value: float, from_unit: str, to_unit: str) -> float:
    fahrenheit_to_celsius = (value - 32) * (5 / 9)
    celsius_to_fahrenheit = (value * (9 / 5)) + 32
    celsius_to_kelvin = value + 273.15
    kelvin_to_celsius = value - 273.15

    match (from_unit, to_unit):
        case ('K','C'):
            return kelvin_to_celsius
        case ('C','K'):
            return celsius_to_kelvin
        case ('F','C'):
            return fahrenheit_to_celsius
        case ('C','F'):
            return celsius_to_fahrenheit
        