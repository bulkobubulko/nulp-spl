from service.lab1.input_service import get_decimal_places, get_number_of_calc
from service.lab1.history_service import display_history, clear_history

def settings_option(calculator_settings):
    """Display settings options and perform the selected action."""   
    while True:
        print("\nOptions:")
        print("1. Display calculation history")
        print("2. Clear history")
        print("3. Set auto-delete history")
        print("4. Set decimal places")
        print("5. Back")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            display_history(calculator_settings.history_file_path)
        elif choice == '2':
            clear_history(calculator_settings.history_file_path)
        elif choice == '3':
            number_of_calc = auto_delete_menu()
            calculator_settings.set_number_of_calculations(number_of_calc)
        elif choice == '4':
            decimal_places = decimal_places_menu()
            calculator_settings.set_decimal_places(decimal_places)
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5).")
            
def auto_delete_menu():
    """Set auto-delete history option."""     
    while True:
        print("1. On")
        print("2. Off")
        choice = input("Enter your choice (1/2): ")
        if choice == '1':
            while True:
                try:
                    number_of_calc = get_number_of_calc()
                    print("Auto-delete history is on.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            break
        elif choice == '2':
            number_of_calc = None
            print("Auto-delete history is off.")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2).")
    return number_of_calc
            
def decimal_places_menu():
    """Set number of decimal places."""   
    # Use global variable to change value outside of function
    global decimal_places
     
    while True:
        try:
            decimal_places = get_decimal_places()
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return decimal_places