# Import functions from console_calculator.py
from history_handling import save_result
from console_calculator import calculate_option, settings_option

from history_handling import HISTORY_FILE, number_of_calculations

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
            settings_option()
        elif choice == '3':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3).")

if __name__ == "__main__":
    main()