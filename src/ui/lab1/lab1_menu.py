from service.lab1.calculator_service import calculate_option
from ui.lab1.lab1_settings_menu import settings_option
from shared.calculator_settings import CalculatorSettings
from config.path_config import SETTINGS_FILE_PATH_LAB1, HISTORY_FILE_LAB1

def main():    
    calculator_settings = CalculatorSettings()
    calculator_settings.set_settings_file_path(SETTINGS_FILE_PATH_LAB1)
    calculator_settings.set_history_file_path(HISTORY_FILE_LAB1)
    calculator_settings.load_settings()
    
    menu(calculator_settings)
    
def menu(calculator_settings):
    while True:
        print("\nOptions:")
        print("1. Perform calculation")
        print("2. Settings")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            calculate_option(calculator_settings)
        elif choice == '2':
            settings_option(calculator_settings)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3).")
    
if __name__ == "__main__":
    main()