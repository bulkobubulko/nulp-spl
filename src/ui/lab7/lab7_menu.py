from service.lab7.spotify_api import get_token
from service.lab7.user_input_handling import search_for_artist_api, search_for_track_api
from shared.data_utils import view_user_history
from config.path_config import FOLDER_PATH_USER_LOGS_LAB7
              
def main():
    token = get_token()
    menu(token)
    
def menu(token):
    while True:
        print("\nMAIN MENU")
        print("Options:")
        print("1. Search for an artist")
        print("2. Search for a track")
        print("3. Display history")
        print("0. Exit")
        
        user_input = input("Enter option: ")
        
        if user_input == '1':
            search_for_artist_api(token)
        elif user_input == '2':
            search_for_track_api(token)
        elif user_input == '3':
            print("User history:")
            view_user_history(FOLDER_PATH_USER_LOGS_LAB7)
        elif user_input == '0':
            print("Exiting...")
            break
        else:
            print("Invalid option")
    
if __name__ == "__main__":
    main()