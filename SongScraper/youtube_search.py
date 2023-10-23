# This file searches for songs on YouTube using the YouTube Data API.

from googleapiclient.discovery import build

# Set up YouTube API
api_key = 'AIzaSyCBCbo9RukCrhhZDfsMwRH5m-PBREovK1U'
youtube = build('youtube', 'v3', developerKey=api_key)

# Search for songs on YouTube
def search_youtube(spotify_library):
    # print(spotify_library)
    for song in spotify_library:
        query = f"{song['track']['name']} {song['track']['artists'][0]['name']} official video"
        request = youtube.search().list(part='snippet', q=query, type='video', maxResults=1)
        response = request.execute()

        video_id = response['items'][0]['id']['videoId']
        # print(video_id)
        youtube_link = f'https://www.youtube.com/watch?v={video_id}'

        # # Update database with YouTube link
        c.execute("UPDATE songs SET youtube_link = ? WHERE name = ? AND artist = ?",
              (youtube_link, name, artist))

    # Commit changes and close connection
    conn.commit()
    conn.close()
