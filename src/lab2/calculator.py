"""Calculator class for the calculator program."""

# Include the parent directory in the system's import path
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Importing functions from lab1
from lab1.history_handling import save_result
from lab1.console_calculator import calculate_option, settings_option

HISTORY_FILE = 'source/lab2/history.txt'

class Calculator():
    def __init__(self):
        self.number_of_calculations = None
            
    def calculate(self):
        while True:
            print("\nOptions:")
            print("1. Perform calculation")
            print("2. Settings")
            print("3. Quit")
            choice = input("Enter your choice (1/2/3): ")
            if choice == '1':
                result = self.calculate_option()
                self.save_result(result, HISTORY_FILE, self.number_of_calculations)
            elif choice == '2':
                self.settings_option(HISTORY_FILE)
            elif choice == '3':
                print("Exiting the calculator. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option (1/2/3).")
    
    def calculate_option(self):
        return calculate_option()
        
    def settings_option(self, HISTORY_FILE):
        settings_option(HISTORY_FILE)
        
    def save_result(self, result, HISTORY_FILE, number_of_calculations):
        save_result(result, HISTORY_FILE, number_of_calculations)