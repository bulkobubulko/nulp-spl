from shared.ascii_art_settings import AsciiArtSettings
from service.lab3.ascii_art_generator import create_ascii_art
from ui.lab3.lab3_settings_menu import settings_menu
from shared.ascii_utils import show_art
from config.path_config import SETTINGS_FILE_PATH_LAB3, FOLDER_PATH_LAB3

def main():    
    settings_obj = AsciiArtSettings()
    settings_obj.set_settings_file_path(SETTINGS_FILE_PATH_LAB3)
    settings_obj.load_settings()
    
    while True:
        print('Options (1/2/3):')
        print('1. Create ASCII-art')
        print('2. Show ASCII-art')
        print('3. Settings')
        print('4. Exit')
        
        user_input = input('Enter option number: ')
        
        if user_input == '1':
            create_ascii_art(FOLDER_PATH_LAB3, settings_obj)
        elif user_input == '2':
            show_art(FOLDER_PATH_LAB3)
        elif user_input == '3':
            settings_menu(settings_obj)
        elif user_input == '4':
            break