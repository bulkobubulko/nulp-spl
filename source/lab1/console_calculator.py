from calculations import calculate
from input_handling import get_input
from history_handling import display_history, clear_history

from history_handling import HISTORY_FILE

# Default values
decimal_places = 2

def calculate_option():
    """
    Calculate the result of a mathematical operation and create a dictionary.

    Returns:
        result_dict (dict): Dictionary containing the operation and the formatted result.
    """
    # Get input
    first_number, second_number, operator = get_input()
    # Calculate result
    result = calculate(first_number, second_number, operator)
    # Format result to decimal places
    formatted_result = format_result(result, decimal_places)
    # Create dictionary
    result_dict = format_dict(first_number, second_number, operator, formatted_result)
    # Print result
    print("Result:", formatted_result)
        
    return result_dict

def settings_option():
    """Display settings options and perform the selected action."""
    while True:
        print("\nOptions:")
        print("1. Display calculation history")
        print("2. Clear history")
        print("3. Set memory functions")
        print("4. Set decimal places")
        print("5. Back")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            display_history(HISTORY_FILE)
        elif choice == '2':
            clear_history(HISTORY_FILE)
        elif choice == '3':
            set_memory_functions()
        elif choice == '4':
            set_decimal_places()
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5).")

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

# Settings functions 

def set_decimal_places():
    """Set decimal places option."""
    # Use global variable to change value outside of function
    global decimal_places
    
    while True:
        try:
            decimal_places = int(input("Enter decimal places: "))
            if decimal_places >= 0:
                print(f"Decimal places set to {decimal_places}.")
                break
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
def set_memory_functions():
    """Display memory functions options and perform the selected action."""
    print("1. Auto-delete history")
    print("2. Back")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        set_auto_delete_history()
    elif choice == '2':
        return
    else:
        print("Invalid choice. Please try again.")
        
def set_auto_delete_history():    
    """Set auto-delete history option."""
    # Use global variable to change value outside of function
    global number_of_calculations    
    
    while True:
        print("1. On")
        print("2. Off")
        print("3. Back")
        choice = input("Enter your choice (1/2): ")
        if choice == '1':
            while True:
                try:
                    number_of_calculations = int(input("Enter the number of calculations to store: "))
                    print("Auto-delete history is on.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            break
        elif choice == '2':
            number_of_calculations = None
            print("Auto-delete history is off.")
            break
        elif choice == '3':
            return
        else:
            print("Invalid choice. Please select a valid option (1/2).")