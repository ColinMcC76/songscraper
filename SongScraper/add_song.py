import database 
import sqlite3

def add_song(name, artist, spotify_link, youtube_link):
    # Connect to the database
    conn, c = database.connect_to_database()

    # Insert the song details into the database
    c.execute("INSERT INTO songs (name, artist, spotify_link, youtube_link) VALUES (?, ?, ?, ?)",
              (name, artist, spotify_link, youtube_link))

    # Commit changes and close connection
    conn.commit()
    conn.close()
