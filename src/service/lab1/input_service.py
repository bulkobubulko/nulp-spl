"""This module contains functions for user input handling."""

VALID_OPERATORS = ['+', '-', '*', '/', '^', '√', '%']  
            
def check_operator(operator):
    """Check if operator is valid.
    
    Args:
        operator (str): Operator
    """
    if operator not in VALID_OPERATORS:
        print("Invalid operator. Please try again.")
        return False
    else:
        return True
    
def get_numeric_input(prompt):
    """Get numeric input from user.
    
    Args:
        prompt (str): Prompt to display to user.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.") 
            
def get_input():
    """Get input from user.

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
     
def get_decimal_places():
    """Get number of decimal places.
    
    Returns:
        decimal_places (int): Number of decimal places
        
    Raises:
        ValueError: If input is not a valid integer
    """    
    while True:
        try:
            decimal_places = int(input("Enter decimal places: "))
            if decimal_places >= 0:
                print(f"Decimal places set to {decimal_places}.")
                return decimal_places
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
def get_number_of_calc():
    """Get number of calculations.
    
    Returns:
        number_of_calculations (int): Number of calculations
        
    Raises:
        ValueError: If input is not a valid integer
    """    
    while True:
        try:
            number_of_calculations = int(input("Enter number of calculations to store: "))
            if number_of_calculations >= 0:
                print(f"Number of calculations set to {number_of_calculations}.")
                return number_of_calculations
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")