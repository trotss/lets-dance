import os
from googleapiclient.discovery import build
import csv
from pytubefix import YouTube

def descarga_audio(url, output_pth):           
    yt = YouTube(url)
    print(f"Descargando video: {yt.title} ...")
    audio = yt.streams.filter(only_audio=True, file_extension='mp3').first()    
    out_file = audio.download(output_path=output_pth)

def get_youtube_service():
    """Initializes and returns the YouTube Data API service."""
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY)

def get_top_songs(youtube_service, artist_name, num_songs=5):
    """
    Searches for an artist's top songs on YouTube based on view count.
    Returns a list of dictionaries with 'title' and 'video_id'.
    """
    print(f"\nSearching for top {num_songs} songs by {artist_name}...")
    try:
        search_response = youtube_service.search().list(
            q=f"{artist_name} official music video", # Prioritize official music videos
            type="video",
            order="viewCount", # Sort by view count
            part="id,snippet",
            maxResults=num_songs * 2 # Get more results and filter later if needed
        ).execute()
        songs = []
        for item in search_response.get("items", []):
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            # Basic filtering to try and get relevant music videos
            if "music" in title.lower() or "official" in title.lower() or "video" in title.lower():
                songs.append({"title": title, "video_id": video_id})
            if len(songs) >= num_songs:
                break
        return songs
    except Exception as e:
        print(f"An error occurred while searching for {artist_name}: {e}")
        return []

if __name__ == "__main__":
    
    YOUTUBE_API_KEY = " "
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    
    output_path = "musica"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    ARTISTS = [
        "Queen",
        "Adele",
        "Metallica"
    ]
    NUMBER_OF_SONGS_PER_ARTIST = 5

    youtube = get_youtube_service()
    with open("musica.csv", mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "url"])  
        
        for artist in ARTISTS:
            top_songs = get_top_songs(youtube, artist, NUMBER_OF_SONGS_PER_ARTIST)
            if top_songs:
                for song in top_songs:
                    video_url = f"https://www.youtube.com/watch?v={song['video_id']}"
                    writer.writerow([song['title'], video_url])
                    try:
                        descarga_audio(video_url, output_path)
                    except:
                        continue # Algunos videos pueden no descargarse (restricciones edad, etc requiere confirmación) 
            else:
                print(f"Could not find top songs for {artist}.")






    