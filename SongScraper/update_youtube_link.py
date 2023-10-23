from database import connect_to_database
import sqlite3

def update_link(youtube_link, name, artist):
    try:
        # Connect to the database)
        conn, c = connect_to_database()

        # Insert the song details into the database
        c.execute("UPDATE songs SET youtube_link = ? WHERE name = ? AND artist = ?",
                  (youtube_link, name, artist))

        # Commit changes and close connection
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()