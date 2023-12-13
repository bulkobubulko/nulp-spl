# Constants
FOLDER_PATH = 'data/lab4/ASCII-arts/'
SETTINGS_FILE_PATH = 'data/lab4/settings.json'
            
def main():
    try: 
        settings_obj = AsciiArtSettings()
        settings_obj.set_settings_file_path(SETTINGS_FILE_PATH)
        settings_obj.load_settings()
        
        while True:
            print('Options (1/2/3):')
            print('1. Create ASCII-art')
            print('2. Show ASCII-art')
            print('3. Settings')
            print('4. Exit')
            
            user_input = input('Enter option number: ')
            
            if user_input == '1':
                create_ascii_art(FOLDER_PATH, settings_obj)
            elif user_input == '2':
                show_art(FOLDER_PATH)
            elif user_input == '3':
                settings(settings_obj)
            elif user_input == '4':
                break
            
    except ValueError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()