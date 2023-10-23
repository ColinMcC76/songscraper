import database
import sqlite3

def clear_database():
    # Connect to the database
    # print("this aint working dog")
    conn, c= database.connect_to_database()
    # print(conn,c)
    

    # Clear the table
    c.execute('DELETE FROM songs')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


clear_database()