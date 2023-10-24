# This file converts YouTube links to MP3 files using youtube-dl.
import os
import subprocess

# Create directory for MP3 files
os.makedirs('spotify_saved_songs', exist_ok=True)

# Convert YouTube links to MP3
def convert_to_MP3(songs):
    for song in songs:
        youtube_link = song[4]
        mp3_filename = f"spotify_saved_songs/{song[1]}_{song[2]}.mp3"
        # print(f"Parameters : {youtube_link}, {mp3_filename}")

    # Use youtube-dl to download audio as MP3
        subprocess.run(['yt-dlp', '--verbose', '--extract-audio', '--audio-format', 'mp3', '-o', mp3_filename, youtube_link])
