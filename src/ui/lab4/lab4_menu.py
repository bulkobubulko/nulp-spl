from service.lab4.ascii_art_generator import create_ascii_art
from shared.ascii_art_settings import AsciiArtSettings
from shared.ascii_utils import show_art
from ui.lab4.lab4_settings_menu import settings
from config.path_config import SETTINGS_FILE_PATH_LAB3, FOLDER_PATH_LAB3

def main():
    try: 
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
                settings(settings_obj)
            elif user_input == '4':
                break
            
    except ValueError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()