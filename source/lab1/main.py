# Include the parent directory in the system's import path
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import functions from console_calculator.py
from lab1.history_handling import save_result
from lab1.console_calculator import calculate_option, settings_option
from lab1.console_calculator import number_of_calculations

HISTORY_FILE = 'source/lab1/history.txt'

def main():    
    while True:
        print("\nOptions:")
        print("1. Perform calculation")
        print("2. Settings")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            result = calculate_option()
            save_result(result, HISTORY_FILE, number_of_calculations)
        elif choice == '2':
            settings_option(HISTORY_FILE)
        elif choice == '3':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3).")

if __name__ == "__main__":
    main()