import spotipy
from add_songs import add_song
from database import connect_to_database 
from spotipy.oauth2 import SpotifyOAuth

# Set up authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='189efcff65934a48b7d96fe6f7118c2c',
                                               client_secret='f8e0ab07ba6e4e96a108f968bea7378c',
                                               redirect_uri='https://example.com/callback',
                                               scope='user-library-read'))

# Fetch liked songs
# Make multiple requests to retrieve all songs
def songs_to_database():
    offset = 0
    max_songs = 10
    while offset < max_songs:
        results = sp.current_user_saved_tracks(limit=10, offset=offset)
        songs = results['items']
        for song in songs:
            name = song['track']['name']
            artist = song['track']['artists'][0]['name']
            spotify_link = song['track']['external_urls']['spotify']
            add_song(name, artist,spotify_link, "")
        offset += len(songs)
    
    return songs
    