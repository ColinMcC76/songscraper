from spotify_auth import songs_to_database
from database import *
from convert_to_mp3 import *
from search_youtube import search_youtube
from grab_all_songs import grab_all_songs

spotify_library = songs_to_database()
songs =grab_all_songs()

search_youtube(songs)


songs = grab_all_songs()
convert_to_MP3(songs)