"""Robust division utility for CLI usage.

This module exposes `safe_divide` which converts inputs, handles errors,
and returns a user-facing message string for main.py to print.
"""

def safe_divide(numerator, denominator):
    """Safely divide two values and return a user-facing message.

    Args:
        numerator: The numerator value as a string or number.
        denominator: The denominator value as a string or number.

    Returns:
        str: One of:
            - "The result of the division is <result>"
            - "Error: Cannot divide by zero."
            - "Error: Please enter numeric values only."
    """
    # Convert inputs to floats
    try:
        a = float(numerator)
        b = float(denominator)
    except ValueError:
        return ("Error: Please enter numeric values only.")

    # Perform division with zero handling
    try:
        result = a/b
    except ZeroDivisionError:
        return ("Error: Cannot divide by zero.")

    return (f"The result of the division is {result}")
