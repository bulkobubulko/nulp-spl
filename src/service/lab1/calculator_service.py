from service.lab1.calc_ops import *
from service.lab1.input_service import get_input
from service.lab1.history_service import save_result

def calculate_result(first_number, second_number, operator):
    if operator == '+':
        return addition(first_number, second_number)
    elif operator == '-':
        return subtraction(first_number, second_number)
    elif operator == '*':
        return multiplication(first_number, second_number)
    elif operator == '/':
        try: 
            return division(first_number, second_number)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            return "undefined"
    elif operator == '^':
        return power(first_number, second_number)
    elif operator == '√':
        try: 
            return square_root(first_number)
        except ValueError as e:
            print(f"Error: {e}")
            return "undefined"
    elif operator == '%':
        try: 
            return remainder(first_number, second_number)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            return "undefined"
    else:
        return "Invalid operator. Please try again."

# Format functions

def format_result(result, decimal_places):
    """
    Format result to decimal places.
    
    Args: 
        result (float): Result of calculation
        decimal_places (int): Number of decimal places to format result to
        
    Returns:
        formatted_result (str): Formatted result
    """
    if result == "undefined":
        return "undefined"
    else:
        return f"{result:.{decimal_places}f}"

def format_dict(first_number, second_number, operator, formatted_result):
    """
    Format result to dictionary.
    
    Args:
        first_number (float): First number
        second_number (float): Second number
        operator (str): Operator
        formatted_result (str): Formatted result
        
    Returns:
        result_dict (dict): Dictionary containing the operation and the formatted result.
    """
    # Create empty dictionary
    result_dict = {}
    
    # Format operation for special cases
    if operator == '√':
        result_dict['operation'] = f'{operator} {first_number}'
    else:
        result_dict['operation'] = f'{first_number} {operator} {second_number}'
    
    # Format result
    result_dict['result'] = formatted_result
    
    return result_dict
            
def calculate_option(calc_settings):
    """
    Calculate the result of a mathematical operation and create a dictionary.

    Returns:
        result_dict (dict): Dictionary containing the operation and the formatted result.
    """
    first_number, second_number, operator = get_input()
    result = calculate_result(first_number, second_number, operator)
    # Format result to decimal places
    formatted_result = format_result(result, calc_settings.decimal_places)
    # Create dictionary
    result_dict = format_dict(first_number, second_number, operator, formatted_result)
    # Save result to history
    save_result(result_dict, calc_settings.history_file_path, calc_settings.number_of_calculations)
    
    print("Result:", formatted_result)
    
    return result_dict