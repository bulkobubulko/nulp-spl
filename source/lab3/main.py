""" Main module for the ASCII-art program."""
from ascii_art_settings import AsciiArtSettings
from ascii_art_generator import create_ascii_art, show_art, settings

def main():    
    settings_obj = AsciiArtSettings()
    
    while True:
        print('Options (1/2/3):')
        print('1. Create ASCII-art')
        print('2. Show ASCII-art')
        print('3. Settings')
        print('4. Exit')
        
        user_input = input('Enter option number: ')
        
        if user_input == '1':
            create_ascii_art(settings_obj)
        elif user_input == '2':
            show_art()
        elif user_input == '3':
            settings(settings_obj)
        elif user_input == '4':
            break
    
if __name__ == "__main__":
    main()