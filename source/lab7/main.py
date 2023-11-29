import sys
import os

# Include the parent directory in the system's import path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)     

from lab7.spotify_api import get_token
from lab7.user_input_handling import search_for_artist_menu, search_for_track_menu
from utility.data_utils import view_user_history

FOLDER_PATH_USER_LOGS = 'source/lab7/data/user_logs.log'
           
              
def main():
    token = get_token()
    while True:
        print("\nMAIN MENU")
        print("Options:")
        print("1. Search for an artist")
        print("2. Search for a track")
        print("3. Display history")
        print("0. Exit")
        
        user_input = input("Enter option: ")
        
        if user_input == '1':
            search_for_artist_menu(token)
        elif user_input == '2':
            search_for_track_menu(token)
        elif user_input == '3':
            print("User history:")
            view_user_history(FOLDER_PATH_USER_LOGS)
        elif user_input == '0':
            print("Exiting...")
            break
        else:
            print("Invalid option")
    
if __name__ == "__main__":
    main()