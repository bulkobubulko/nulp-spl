"""This module contains functions for making requests to the Spotify API.

How authentication works in Spotify API:

Two types of authentication:
    1. Client Credentials Flow:
        - Used for non-user related endpoints
    2. Authorization Code Flow
        - Used for user-related endpoints

We are using Client Credentials Flow. It works like this:
    1. Request access token from Spotify API (send client_id, 
       client_secret, grant_type=client_credentials)
    2. Server returns access token.
    3. Use access token to make requests to Spotify Web API.
"""

import os
import json
import base64
from requests import get, post

# Get client id and secret from environment variables
client_id=os.environ.get("SPOTIFY_CLIENT_ID")
client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET")

def get_token():
    """Request access token from Spotify API.
    Returns:
        token (str): Access token.
    Raises:
        Exception: raise an HTTPError if the HTTP request returned an 
        unsuccessful status code.
    """
    auth_string = client_id + ':' + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')
    
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + auth_base64, 
        'Content-Type': 'application/x-www-form-urlencoded'
        }
    data = {'grant_type': 'client_credentials'}
    
    try: 
        result = post(url, headers=headers, data=data)
        result.raise_for_status()
        json_result = json.loads(result.content)
        token = json_result['access_token']
        return token
    except Exception as e:
        print('Error getting token: ' + str(e))
        return None

def get_auth_token(token):
    """Construct authorization header to be used in requests to Spotify API."""
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    """Search for artist by name.
    
    Args:
        token (str): Access token.
        artist_name (str): Artist name.
        
    Returns:
        json_result (dict): JSON object with artist data.
        
    Raises:
        Exception: raise an HTTPError if the HTTP request returned an 
        unsuccessful status code.
    """
    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_token(token)
    query = f'?q={artist_name}&type=artist&limit=1'
    
    query_url = url + query
    
    try: 
        result = get(query_url, headers=headers)
        result.raise_for_status()  # Check for HTTP errors
        json_result = json.loads(result.content)['artists']['items']
        
        if not json_result:
            print(f'No results found for artist: {artist_name}')
            return None
        
        return json_result[0]
    
    except Exception as e:
        print(f"Error searching for artist: {e}")
        return None
    
def search_for_track(token, track_name):
    """Search for track by name.

    Args:
        token (str): Access token.
        track_name (str): Track name.
        
    Returns:
        json_result (dict): JSON object with track data.
        
    Raises:
        Exception: raise an HTTPError if the HTTP request returned an 
        unsuccessful status code.
    """
    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_token(token)
    query = f'?q={track_name}&type=track&limit=1'
    
    query_url = url + query
    
    try: 
        result = get(query_url, headers=headers)
        result.raise_for_status()  # Check for HTTP errors
        json_result = json.loads(result.content)['tracks']['items']
        
        if not json_result:
            print(f'No results found for track: {track_name}')
            return None
        
        return json_result[0]
    
    except Exception as e:
        print(f"Error searching for track: {e}")
        return None  

# Get functions for artist data

def get_artists_top_tracks(token, artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US'
    headers = get_auth_token(token)
    
    try: 
        result = get(url, headers=headers)
        result.raise_for_status()
        json_result = json.loads(result.content)['tracks']
        return json_result
    except Exception as e:
        print(f"Error getting top tracks: {e}")
        return None 
    

def get_artists_albums(token, artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}/albums?country=US'
    headers = get_auth_token(token)
    
    try: 
        result = get(url, headers=headers)
        result.raise_for_status()
        json_result = json.loads(result.content)['items']
        return json_result
    except Exception as e:
        print(f"Error getting albums: {e}")
        return None
    
def get_artists_related_artists(token, artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}/related-artists'
    headers = get_auth_token(token)
    
    try: 
        result = get(url, headers=headers)
        result.raise_for_status()
        json_result = json.loads(result.content)['artists']
        return json_result
    except Exception as e:
        print(f"Error getting related artists: {e}")
        return None
    
def get_artist_followers(token, artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}'
    headers = get_auth_token(token)
    
    try: 
        result = get(url, headers=headers)
        result.raise_for_status()
        json_result = json.loads(result.content)['followers']['total']
        return json_result
    except Exception as e:
        print(f"Error getting followers: {e}")
        return None
    
def get_artist_genres(token, artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}'
    headers = get_auth_token(token)
    
    try:
        result = get(url, headers=headers)
        result.raise_for_status()
        json_result = json.loads(result.content)['genres']
        return json_result
    except Exception as e:
        print(f"Error getting genres: {e}")
        return None 
    
# Get functions for track data

def get_track_artist(token, track_id):
    url = f'https://api.spotify.com/v1/tracks/{track_id}'
    headers = get_auth_token(token)
    
    try: 
        result = get(url, headers=headers)
        result.raise_for_status()
        json_result = json.loads(result.content)['artists'][0]
        return json_result
    except Exception as e:
        print(f"Error getting artist: {e}")
        return None
    
def get_track_album(token, track_id):
    url = f'https://api.spotify.com/v1/tracks/{track_id}'
    headers = get_auth_token(token)
    
    try: 
        result = get(url, headers=headers)
        result.raise_for_status()
        json_result = json.loads(result.content)['album']
        return json_result
    except Exception as e:
        print(f"Error getting album: {e}")
        return None

def get_track_duration(token, track_id):
    url = f'https://api.spotify.com/v1/tracks/{track_id}'
    headers = get_auth_token(token)
    
    try: 
        result = get(url, headers=headers)
        result.raise_for_status()
        json_result = json.loads(result.content)['duration_ms']
        return json_result
    except Exception as e:
        print(f"Error getting duration: {e}")
        return None
    
def get_track_popularity(token, track_id):
    url = f'https://api.spotify.com/v1/tracks/{track_id}'
    headers = get_auth_token(token)
    
    try: 
        result = get(url, headers=headers)
        result.raise_for_status()
        json_result = json.loads(result.content)['popularity']
        return json_result
    except Exception as e:
        print(f"Error getting popularity: {e}")
        return None

def get_track_release_date(token, track_id):
    url = f'https://api.spotify.com/v1/tracks/{track_id}'
    headers = get_auth_token(token)
    
    try: 
        result = get(url, headers=headers)
        result.raise_for_status()
        json_result = json.loads(result.content)['album']['release_date']
        return json_result
    except Exception as e:
        print(f"Error getting release date: {e}")
        return None

def get_track_genres(token, track_id):
    url = f'https://api.spotify.com/v1/tracks/{track_id}'
    headers = get_auth_token(token)
    
    try: 
        result = get(url, headers=headers)
        result.raise_for_status()
        artist_id = json.loads(result.content)['artists'][0]['id']
        artist_genres = get_artist_genres(token, artist_id)
        return artist_genres
    except Exception as e:
        print(f"Error getting genres: {e}")
        return None
    
def get_track_explicit(token, track_id):
    url = f'https://api.spotify.com/v1/tracks/{track_id}'
    headers = get_auth_token(token)
    
    try: 
        result = get(url, headers=headers)
        result.raise_for_status()
        json_result = json.loads(result.content)['explicit']
        return json_result
    except Exception as e:
        print(f"Error getting explicit: {e}")
        return None