from Audioverse.youtube import youtube_api

# Create a YouTube object
youtube = youtube_api.YoutubeAPI("API_KEY")

# Get a video
video = youtube.get_video("VIDEO_ID")

# Get a channel
channel = youtube.get_channel("CHANNEL_ID")

# Get a playlist
playlist = youtube.get_playlist("PLAYLIST_ID")
