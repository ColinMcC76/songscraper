import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='189efcff65934a48b7d96fe6f7118c2c',
                                               client_secret='f8e0ab07ba6e4e96a108f968bea7378c',
                                               redirect_uri='https://example.com/callback',
                                               scope='user-library-read'))

# Fetch liked songs
liked_songs = sp.current_user_saved_tracks()

