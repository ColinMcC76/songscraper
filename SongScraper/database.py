# This file manages the database operations.
from spotify_auth import liked_songs
from add_song import *
import sqlite3


def connect_to_database():
    # Connect to SQLite database
    conn = sqlite3.connect('spotifyLikedSongs.db')
    c = conn.cursor()

    # Create a table to store liked songs
    c.execute('''CREATE TABLE IF NOT EXISTS songs
                 (id INTEGER PRIMARY KEY,
                  name TEXT,
                  artist TEXT,
                  spotify_link TEXT,
                  youtube_link TEXT)''')
    
    return conn, c


