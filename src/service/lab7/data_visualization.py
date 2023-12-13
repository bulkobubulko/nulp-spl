from prettytable import PrettyTable

from service.lab7.spotify_api import get_track_artist, get_track_album, get_track_duration, get_track_popularity, get_track_release_date, get_track_genres, get_track_explicit
from service.lab7.spotify_api import get_artists_top_tracks, get_artists_albums, get_artists_related_artists, get_artist_followers, get_artist_genres
from shared.data_utils import save_data

FOLDER_PATH_OUTPUT = 'data/lab7/output/'

def display_data(data, field_names, entity_name):
    if not data:
        print(f"No {entity_name} data to display")
        return None
    
    table = PrettyTable()
    table.field_names = field_names
    for idx, item in enumerate(data, start=1):
        table.add_row([idx] + [item['name']])
    print(f"{entity_name.capitalize()} data:")
    print(table)

def display_artists_top_tracks(token, artist_id, artist_name):
    tracks = get_artists_top_tracks(token, artist_id)
    field_names = ["#", "Track name"]
    display_data(tracks, field_names, "track")
    save_data(tracks, FOLDER_PATH_OUTPUT, f'top_tracks_{artist_name}', 'json')

def display_artists_albums(token, artist_id, artist_name):
    albums = get_artists_albums(token, artist_id)
    field_names = ["#", "Album name"]
    display_data(albums, field_names, "album")
    save_data(albums, FOLDER_PATH_OUTPUT, f'albums_{artist_name}', 'json')

def display_artists_related_artists(token, artist_id, artist_name):
    related_artists = get_artists_related_artists(token, artist_id)
    field_names = ["#", "Artist name"]
    display_data(related_artists, field_names, "related artist")
    save_data(related_artists, FOLDER_PATH_OUTPUT, f'related_artists_{artist_name}', 'json')

def display_artists_followers(token, artist_id, artist_name):
    followers = get_artist_followers(token, artist_id)
    print(f"Followers for {artist_name}: {followers}")
    save_data(followers, FOLDER_PATH_OUTPUT, f'followers_{artist_name}', 'json')

def display_artists_genres(token, artist_id, artist_name):
    genres = get_artist_genres(token, artist_id)
    print(f"Genres for {artist_name}: {', '.join(genres)}")
    save_data(genres, FOLDER_PATH_OUTPUT, f'genres_{artist_name}', 'json')
    
def display_track_artist(token, track_id, track_name):
    artist = get_track_artist(token, track_id)
    print(f"Artist for {track_name}: {artist['name']}")
    save_data(artist, FOLDER_PATH_OUTPUT, f'artist_{track_name}', 'json')
    
def display_track_album(token, track_id, track_name):
    album = get_track_album(token, track_id)
    print(f"Album for {track_name}: {album['name']}")
    save_data(album, FOLDER_PATH_OUTPUT, f'album_{track_name}', 'json')
    
def display_track_duration(token, track_id, track_name):
    duration = get_track_duration(token, track_id)
    print(f"Duration for {track_name}: {duration}")
    save_data(duration, FOLDER_PATH_OUTPUT, f'duration_{track_name}', 'json')
    
def display_track_popularity(token, track_id, track_name):
    popularity = get_track_popularity(token, track_id)
    print(f"Popularity for {track_name}: {popularity}")
    save_data(popularity, FOLDER_PATH_OUTPUT, f'popularity_{track_name}', 'json')
    
def display_track_release_date(token, track_id, track_name):
    release_date = get_track_release_date(token, track_id)
    print(f"Release date for {track_name}: {release_date}")
    save_data(release_date, FOLDER_PATH_OUTPUT, f'release_date_{track_name}', 'json')
    
def display_track_genres(token, track_id, track_name):
    genres = get_track_genres(token, track_id)
    print(f"Genres for {track_name}: {', '.join(genres)}")
    save_data(genres, FOLDER_PATH_OUTPUT, f'genres_{track_name}', 'json')

def display_track_explicit(token, track_id, track_name):
    explicit = get_track_explicit(token, track_id)
    print(f"Explicit for {track_name}: {explicit}")
    save_data(explicit, FOLDER_PATH_OUTPUT, f'explicit_{track_name}', 'json')