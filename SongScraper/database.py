# This file manages the database operations.
from spotify_auth import liked_songs
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('SpotifyLikedSongs.db')
c = conn.cursor()

# # Create a table to store liked songs
# c.execute('''CREATE TABLE songs
#              (id INTEGER PRIMARY KEY,
#               name TEXT,
#               artist TEXT,
#               spotify_link TEXT,
#               youtube_link TEXT)''')

# Save liked songs to the database
for song in liked_songs['items']:
    name = song['track']['name']
    artist = song['track']['artists'][0]['name']
    spotify_link = song['track']['external_urls']['spotify']

    c.execute("INSERT INTO songs (name, artist, spotify_link) VALUES (?, ?, ?)",
              (name, artist, spotify_link))

# Commit changes and close connection
conn.commit()
conn.close()
