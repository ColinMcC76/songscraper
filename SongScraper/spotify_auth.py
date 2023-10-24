import spotipy
from add_songs import add_song
from database import connect_to_database 
from credentials import *
from spotipy.oauth2 import SpotifyOAuth
 

# Set up authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                               client_secret=spotify_client_secret,
                                               redirect_uri=spotify_redirect_uri,
                                               scope='user-library-read'))


liked_songs = sp.current_user_saved_tracks()
total_songs = liked_songs['total']
# Fetch liked songs
# Make multiple requests to retrieve all songs
def songs_to_database():
    offset = 0
    max_songs = 2331
    while offset < max_songs:
        results = sp.current_user_saved_tracks(limit=50, offset=offset)
        songs = results['items']
        for song in songs:
            name = song['track']['name']
            artist = song['track']['artists'][0]['name']
            spotify_link = song['track']['external_urls']['spotify']
            add_song(name, artist,spotify_link, "")
        offset += len(songs)
    
    return songs
    