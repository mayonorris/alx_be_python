# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """Performs basic arithmetic operations on two numbers.

    operation: 'add', 'subtract', 'multiply', or 'divide'
    On division by zero, returns a recognizable message instead of raising.
    """
    if operation == "add":
        return (num1 + num2)
    elif operation == "subtract":
        return (num1 - num2)
    elif operation == "multiply":
        return (num1 * num2)
    elif operation == "divide":
        if num2 == 0:
            return ("Error: Division by zero") 
        return (num1 / num2)
    else:
        return ("Error: Unsupported operation")
