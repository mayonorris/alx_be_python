"""
Temperature Conversion Tool
This module provides functions to convert temperatures between Celsius and Fahrenheit.
Learning Objectives:
- Implement temperature conversion functions
- Handle user input and validation
"""
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if __name__ == "__main__":
    raw_temp = input("Enter the temperature to convert: ").strip()
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    # numeric validation with required error message
    try:
        temp = float(raw_temp)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    # Convert based on unit
    match unit:
        case "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")
        case "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        case _:
            print("Invalid scale. Please use 'C' for Celsius or 'F' for Fahrenheit.")