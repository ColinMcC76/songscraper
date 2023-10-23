# This file searches for songs on YouTube using the YouTube Data API
from database import connect_to_database
from update_youtube_link import update_link


from googleapiclient.discovery import build

# Set up YouTube API
api_key = 'AIzaSyCai5DlFA8ZZOVF7jRm4E6odsU0q27jEuo'
youtube = build('youtube', 'v3', developerKey=api_key)

# Search for songs on YouTube
def search_youtube(songs):
    conn, c = connect_to_database()
    print(songs)

    for song in songs:
        name = song[1]
        artist = song[2]
        query = f"{song[1]} {song[2]} official video"
        print(f"Parameters {query}")
        request = youtube.search().list(part='snippet', q=query, type='video', maxResults=1)
        response = request.execute()
        video_id = response['items'][0]['id']['videoId']
        youtube_link = f'https://www.youtube.com/watch?v={video_id}'

        # # Update database with YouTube link
        update_link(youtube_link, name, artist)

    # Commit changes and close connection
    conn.commit()
    conn.close()
