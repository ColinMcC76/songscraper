from spotify_auth import songs_to_database
from database import *
from convert_to_mp3 import *
from youtube_search import search_youtube
# from add_songs import *
# import spotipy
import sqlite3

spotify_library = songs_to_database()

search_youtube(spotify_library)

