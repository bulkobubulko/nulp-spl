VALID_OPERATORS = ['+', '-', '*', '/', '^', '√', '%']

# Input functions

def get_input():
    """
    Get input from user

    Returns:
        first_number (float): First number
        second_number (float): Second number
        operator (str): Operator
    """
    while True:
        operator = input("Enter an operator (+, -, *, /, ^, √, %): ")
        if check_operator(operator):
            break
    # Special case for square root and power operators
    if operator == '^':
        first_number = get_numeric_input("Enter number: ")
        second_number = get_numeric_input("Enter power: ")
    elif operator == '√':
        first_number = get_numeric_input("Enter number: ")
        second_number = None
    # For all other operators
    else:
        first_number = get_numeric_input("Enter first number: ")
        second_number = get_numeric_input("Enter second number: ")
    return first_number, second_number, operator

def check_operator(operator):
    """
    Check if operator is valid.
    
    Args:
        operator (str): Operator
    """
    if operator not in VALID_OPERATORS:
        print("Invalid operator. Please try again.")
        return False
    else:
        return True
    
def get_numeric_input(prompt):
    """
    Get numeric input from user.
    
    Args:
        prompt (str): Prompt to display to user.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")   