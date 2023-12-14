"""Calculator class for the calculator program."""

from shared.calculator_settings import CalculatorSettings
from ui.lab1.lab1_menu import menu
from config.path_config import SETTINGS_FILE_PATH_LAB2, HISTORY_FILE_LAB2
class Calculator():
    def __init__(self):
        self.calcultor_settings = CalculatorSettings()
        self.calcultor_settings.set_settings_file_path(SETTINGS_FILE_PATH_LAB2)
        self.calcultor_settings.set_history_file_path(HISTORY_FILE_LAB2)
        self.calcultor_settings.load_settings()
        
    def calculate(self):
        menu(self.calcultor_settings)