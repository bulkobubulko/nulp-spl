"""
Module for storing settings for ASCII-art.
"""
import json

SETTINGS_FILE_PATH = 'source/lab3/settings.json'

class AsciiArtSettings:
    """
    Class for storing settings for ASCII-art.
    
    Attributes:
        font (str): Font name.
        size (tuple): Size of ASCII-art.
        symbol (str): Symbol to replace.
        color (str): Color of ASCII-art.
    """
    def __init__(self):
        self.font = None
        self.size = None
        self.symbol = None
        self.color = None
        
        self.load_settings()

    def set_font(self, font):
        self.font = font
        self.save_settings()

    def set_size(self, width, height):
        self.size = (width, height)
        self.save_settings()

    def set_symbol(self, symbol):
        self.symbol = symbol
        self.save_settings()

    def set_color(self, color):
        self.color = color
        self.save_settings()

    def default_settings(self):
        self.font = 'standard'
        self.size = (80, 25)
        self.symbol = None
        self.color = '\x1b[39m'
        self.save_settings()
        
    def save_settings(self):
        settings_data = {
            'font': self.font,
            'size': self.size,
            'symbol': self.symbol,
            'color': self.color
        }
        with open(SETTINGS_FILE_PATH, 'w') as file:
            json.dump(settings_data, file)

    def load_settings(self):
        try:
            with open(SETTINGS_FILE_PATH, 'r') as file:
                settings_data = json.load(file)
                self.font = settings_data['font']
                self.size = settings_data['size']
                self.symbol = settings_data['symbol']
                self.color = settings_data['color']
        except FileNotFoundError:
            # If file does not exist use default settings
            self.default_settings()