def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    
    return num1 - num2


def multiply(num1, num2):
    
    return num1 * num2


def divide(num1, num2):
    """Return the result of dividing num1 by num2. Returns None if num2 is 0."""
    if num2 == 0:
        print("You cannot divide by zero.")
        return None
    else:
        return num1 / num2
