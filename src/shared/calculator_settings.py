"""Module for storing settings for calculator."""
import json

class CalculatorSettings:
    """Class for storing settings for calculator.
    
    Attributes:
        decimal_places (int): Number of decimal places to format result to.
        number_of_calculations (int): Number of calculations to store in history.
    """
    def __init__(self):
        self.settings_file_path = None
        self.history_file_path = None
        self.decimal_places = None
        self.number_of_calculations = None
    
    def set_settings_file_path(self, settings_file_path):
        self.settings_file_path = settings_file_path
        
    def set_history_file_path(self, history_file_path):
        self.history_file_path = history_file_path
        
    def set_decimal_places(self, decimal_places):
        self.decimal_places = decimal_places
        self.save_settings()
        
    def set_number_of_calculations(self, number_of_calculations):
        self.number_of_calculations = number_of_calculations
        self.save_settings()    
        
    def show_settings(self):
        print('Current settings:')
        print(f'Decimal places: {self.decimal_places}')
        print(f'Number of calculations: {self.number_of_calculations}')
        
    def default_settings(self):
        self.decimal_places = 2
        self.number_of_calculations = 5
        
    def save_settings(self):
        settings_data = {
            'decimal_places': self.decimal_places,
            'number_of_calculations': self.number_of_calculations,
        }
        with open(self.settings_file_path, 'w') as file:
            json.dump(settings_data, file)

    def load_settings(self):
        try:
            with open(self.settings_file_path, 'r') as file:
                settings_data = json.load(file)
                self.decimal_places = settings_data['decimal_places']
                self.number_of_calculations = settings_data['number_of_calculations']
        except FileNotFoundError:
            # If file does not exist use default settings
            self.default_settings()