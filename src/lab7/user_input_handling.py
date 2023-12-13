from spotify_api import search_for_artist, search_for_track
from menus import search_for_artist_options_menu, search_for_track_options_menu
from utility.data_utils import log_user_history

FOLDER_PATH_USER_LOGS = 'source/lab7/data/user_logs.log'

def get_artist_name_from_user():
    artist_name = input("Enter artist name: ")
    if not artist_name.strip():
        raise ValueError("Artist name cannot be empty")
    return artist_name

def get_track_name_from_user():
    track_name = input("Enter track name: ")
    if not track_name.strip():
        raise ValueError("Track name cannot be empty")
    return track_name

def search_for_artist_menu(token):
    try: 
        artist_name = get_artist_name_from_user()
        result = search_for_artist(token, artist_name)
        if result:
            artist_id = result['id']
            log_message = f"Artist found: {result['name']}"
            print(log_message)
            search_for_artist_options_menu(token, artist_id, artist_name)
        else:
            log_message = f"No results found for artist: {artist_name}"
            print(log_message)
        log_user_history("Search for Artist", artist_name, log_message, FOLDER_PATH_USER_LOGS)
    except ValueError as e:
        print(f"An error occurred: {e}")

def search_for_track_menu(token):    
    try: 
        track_name = get_track_name_from_user()
        result = search_for_track(token, track_name)
        if result:
            track_id = result['id']
            log_message = f"Track found: {result['name']}"
            print(log_message)
            search_for_track_options_menu(token, track_id, track_name)
        else:
            log_message = f"No results found for track: {track_name}"
            print(log_message)
        log_user_history("Search for Track", track_name, log_message, FOLDER_PATH_USER_LOGS)
    except ValueError as e:
        print(f"An error occurred: {e}")