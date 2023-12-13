"""Calculator class for the calculator program."""

from shared.calculator_settings import CalculatorSettings
from ui.lab1.lab1_menu import menu

SETTINGS_FILE_PATH = 'src/data/lab2/calculator_settings.json'
HISTORY_FILE = 'src/data/lab2/history.txt'

class Calculator():
    def __init__(self):
        self.calcultor_settings = CalculatorSettings()
        self.calcultor_settings.set_settings_file_path(SETTINGS_FILE_PATH)
        self.calcultor_settings.set_history_file_path(HISTORY_FILE)
        self.calcultor_settings.load_settings()
        
    def calculate(self):
        menu(self.calcultor_settings)