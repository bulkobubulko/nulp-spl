"""ASCII-art generator."""

import os
import pyfiglet
from pyfiglet import Figlet
from colorama import Fore

# To initialize colorama and configure its behavior
from colorama import init as colorama_init

# Initialize colorama
# autoreset=True -> Color settings will automatically reset after each print statement
colorama_init(autoreset=True)

from shared.user_input_utils import get_phrase
from shared.ascii_utils import set_size, set_font, set_symbols, set_color
from shared.ascii_utils import check_size, change_symbols, preview_art

def settings(settings_obj):    
    while True:
        print('Options (1/2/3/4/5/6):')
        print('0. Show current settings')
        print('1. Change font')
        print('2. Change size')
        print('3. Change symbol')
        print('4. Change color')
        print('5. Reset settings')
        print('6. Back')
        
        user_input = input('Enter option number: ')
        if user_input == '0':
            settings_obj.show_settings()
        if user_input == '1':
            settings_obj.set_font(set_font())
        elif user_input == '2':
            settings_obj.set_size(*set_size())
        elif user_input == '3':
            settings_obj.set_symbols(*set_symbols())
        elif user_input == '4':
            settings_obj.set_color(set_color())
        elif user_input == '5':
            settings_obj.default_settings()
        elif user_input == '6':
            break

def create_ascii_art(FOLDER_PATH, settings_obj):
    """Ask user for phrase and show ASCII-art.
    
    Args:
        settings_obj (AsciiArtSettings): Object with settings.
    """
    user_input = get_phrase() 
    width, height = settings_obj.size
    try:
        check_size(user_input, width, height)
    except ValueError as e:
        print(f"An error occurred: {e}")
        return None
    
    art = Figlet(font=settings_obj.font, width=settings_obj.size[0])
    art = art.renderText(user_input)
    
    if settings_obj.symbols:
        art = change_symbols(art, settings_obj.symbols[0])
        
    art = settings_obj.color + art
    
    preview_art(FOLDER_PATH, art)
    
