# This file searches for songs on YouTube using the YouTube Data API
from database import connect_to_database
from update_youtube_link import update_link
from youtube_search import YoutubeSearch
import json

# Search for songs on YouTube
def search_youtube(songs):
    conn, c = connect_to_database()

    for song in songs:
        name = song[1]
        artist = song[2]
        query = f"{name} {artist} official video"
        results = YoutubeSearch(f'{query}', max_results=1).to_json()
        data = json.loads(results)
        url_suffix = data['videos'][0]['url_suffix']
        youtube_link = f'https://www.youtube.com{url_suffix}'

        # # Update database with YouTube link
        update_link(youtube_link, name, artist)

    # Commit changes and close connection
    conn.commit()
    conn.close()
