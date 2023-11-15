from data_visualization import display_artists_top_tracks, display_artists_albums, display_artists_related_artists, display_artists_followers, display_artists_genres
from data_visualization import display_track_artist, display_track_album, display_track_duration, display_track_popularity, display_track_release_date, display_track_genres, display_track_explicit

def search_for_artist_options_menu(token, artist_id, artist_name):
    while True:
        print("\nARTIST SEARCH MENU")
        print("Options:")
        print("1. Get Top Tracks")
        print("2. Get Albums")
        print("3. Get Related Artists")
        print("4. Get Followers")
        print("5. Get Genres")
        print("0. Back")
        
        user_input = input("Enter option: ")
        
        if user_input == '1':
            display_artists_top_tracks(token, artist_id, artist_name)
        elif user_input == '2':
            display_artists_albums(token, artist_id, artist_name)
        elif user_input == '3':
            display_artists_related_artists(token, artist_id, artist_name)
        elif user_input == '4':
            display_artists_followers(token, artist_id, artist_name)
        elif user_input == '5':
            display_artists_genres(token, artist_id, artist_name)
        elif user_input == '0':
            break
        else:
            print("Invalid option")
                
def search_for_track_options_menu(token, track_id, track_name):
    while True:
        print("\nTRACK SEARCH MENU")
        print("Options:")
        print("1. Get Artist")
        print("2. Get Album")
        print("3. Get Duration")
        print("4. Get Popularity")
        print("5. Get Release Date")
        print("6. Get Genres")
        print("7. Get Explicit")
        print("0. Back")
        
        user_input = input("Enter option: ")
        
        if user_input == '1':
            display_track_artist(token, track_id, track_name)
        elif user_input == '2':
            display_track_album(token, track_id, track_name)
        elif user_input == '3':
            display_track_duration(token, track_id, track_name)
        elif user_input == '4':
            display_track_popularity(token, track_id, track_name)
        elif user_input == '5':
            display_track_release_date(token, track_id, track_name)
        elif user_input == '6':
            display_track_genres(token, track_id, track_name)
        elif user_input == '7':
            display_track_explicit(token, track_id, track_name)
        elif user_input == '0':
            break
        else:
            print("Invalid option")  
    