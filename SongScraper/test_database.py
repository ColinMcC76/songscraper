import unittest
from add_songs import add_song
from update_youtube_link import update_link
from delete_youtube_link import delete_link
from database import *

class TestDatabase(unittest.TestCase):
    
    def test_insert_song(self):
        # Test if a song is inserted correctly into the database
        # ...
        # add_song(name, artist, spotify_link, youtube_link)

    def test_update_song(self):
        # Test if a song's details are updated correctly in the database
        # ...
        # update_link(youtube_link, name, artist)
        # update_link("https://www.youtube.com/watch?v=tmbXQkoqUnQ", "Thunder 'N Lightnin'", "Hoyt Axton")



    def test_delete_song(self):
        # Test if a song is deleted correctly from the database
        # ...
        # delete_link(youtube_link, name, artist)
        # delete_link("Thunder 'N Lightnin'", "Hoyt Axton")


    # Add more test cases as needed
