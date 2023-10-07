"""Calculator class for the calculator program."""

# Setting up the path to import modules from lab1
# home_path is the path to the root of the project
import sys 
from constants import home_path
sys.path.append(home_path + '/source/lab1')

# Importing functions from lab1
from history_handling import save_result
from console_calculator import calculate_option, settings_option

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
                result = calculate_option()
                self.save_result(result, HISTORY_FILE)
            elif choice == '2':
                self.settings_option()
            elif choice == '3':
                print("Exiting the calculator. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option (1/2/3).")
    
    def calculate_option(self):
        calculate_option() 
        
    def settings_option(self):
        settings_option()
        
    def save_result(self, result, HISTORY_FILE):
        save_result(result, HISTORY_FILE, self.number_of_calculations)