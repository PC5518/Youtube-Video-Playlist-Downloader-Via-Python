import yt_dlp

# Define the playlist URL
playlist_url = "playlist url"    # paste the url here 

# Define the download path (change this to your desired path)
download_path = r"directory  or the folder u wanna place the downloaded youtube vidoes"  #  in r"  "   Write the YouTube playlist link.

# Set up options for yt-dlp
ydl_opts = {
    'quiet': True,  # Suppress output from yt-dlp
    'outtmpl': download_path + '/%(title)s.%(ext)s',  # Path to save the video
}

# Function to extract video links from the playlist
def extract_playlist_links(playlist_url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)

        # Check if the playlist contains videos
        if 'entries' in playlist_info:
            video_urls = []
            for video in playlist_info['entries']:
                video_urls.append(f"https://www.youtube.com/watch?v={video['id']}")
            return video_urls
        else:
            print("No videos found in the playlist.")
            return []

# Function to download videos from the list of links
def download_videos(video_links):
    for video_link in video_links:
        try:
            # Use yt-dlp to download the video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_link])
            print(f"Download complete: {video_link}")
        except Exception as e:
            print(f"Failed to download {video_link}: {e}")

# Extract video links from the playlist
video_links = extract_playlist_links(playlist_url)

# If video links are found, proceed with downloading
if video_links:
    download_videos(video_links)
