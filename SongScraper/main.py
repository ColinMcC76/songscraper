from spotify_auth import songs_to_database
from database import *
from convert_to_mp3 import *
from youtube_search import search_youtube
from grab_all_songs import grab_all_songs
from update_youtube_link import update_link
from delete_youtube_link import delete_link
# from add_songs import *
# import spotipy
import sqlite3

spotify_library = songs_to_database()
songs =grab_all_songs()

# search_youtube(songs)
songs = grab_all_songs()
convert_to_MP3(songs)