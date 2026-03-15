#This code converts temperature from celsius to fahrenheit or kelvin
celsius = float(input("please enter a temperature in Celsius: "))
fahrenheit: float = (celsius * (9/5)) + 32
kelvin: float = celsius + 273.15

print(f'''
    Temperature in Celsius: {celsius}
    Temperature in Fahrenheit: {fahrenheit}
    Temperature in Kelvin: {kelvin}
      ''')