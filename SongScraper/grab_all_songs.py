from database import connect_to_database
import sqlite3

def grab_all_songs():
    # Connect to the database
    conn, c = connect_to_database()

    # Execute a query to retrieve all data
    c.execute('SELECT * FROM songs')
    # Fetch data as a list of tuples
    data_list = c.fetchall()


    # Commit changes and close connection
    conn.commit()
    conn.close()
    return(data_list) 