# Import functions from console_calculator.py
from history_handling import load_history, save_history
from console_calculator import calculate_option, settings_option

# Import global variables 
from history_handling import HISTORY_FILE
from console_calculator import number_of_calculations

def main():
    # Use global variable to change value outside of function
    global number_of_calculations
    
    while True:
        print("\nOptions:")
        print("1. Perform calculation")
        print("2. Settings")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            history = load_history(HISTORY_FILE)
            result_dict = calculate_option()
            if number_of_calculations is not None:
                if len(history) >= number_of_calculations:
                    history.pop(0)
            history.append(result_dict)
            save_history(HISTORY_FILE, history)
        elif choice == '2':
            settings_option()
        elif choice == '3':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3).")

if __name__ == "__main__":
    main()