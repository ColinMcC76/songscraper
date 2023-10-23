from spotify_auth import liked_songs
from database import *
from convert_to_mp3 import *
from youtube_search import *
from add_song import *
# import spotipy
import sqlite3

spotify_library = liked_songs

for song in liked_songs['items']:
    name = song['track']['name']
    artist = song['track']['artists'][0]['name']
    spotify_link = song['track']['external_urls']['spotify']

    add_song(name, artist,spotify_link, "")