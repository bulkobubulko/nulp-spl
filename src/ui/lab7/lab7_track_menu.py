def search_for_track_options_menu(token, artist_id, artist_name):
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