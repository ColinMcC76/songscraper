from database import connect_to_database
import sqlite3

def clear_database():
    # Connect to the database
    conn, c= connect_to_database()

    # Clear the table
    c.execute('DELETE FROM songs')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

clear_database()