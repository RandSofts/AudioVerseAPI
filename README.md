# AudioVerseAPI
AudioVerseAPI is a Python package for accessing and manipulating music-related data. It provides an easy-to-use interface to interact with the AudioVerse API, which offers a comprehensive database of music-related information such as artists, albums, tracks, and more. With AudioVerseAPI, you can access this information, extract relevant data, and perform various operations on it.

## Installation
To install AudioVerseAPI, simply clone this repository and run the following command in the root directory:
```bash
pip install -r requirements.txt
```

## Usage
To use AudioVerseAPI, import the package and create an instance of the AudioVerse class:
```py
from Audioverse.spotify import spotify_api

# Create a Spotify object
spotify = spotify_api.SpotifyAPI(client_id="CLIENT_ID", client_secret="CLIENT_SECRET")

# Get a track
track = spotify.get_track("TRACK_ID")

# Get an artist
artist = spotify.get_artist("ARTIST_ID")

# Get an album
album = spotify.get_album("ALBUM_ID")

# Get a playlist
playlist = spotify.get_playlist("PLAYLIST_ID")
```

```py
from Audioverse.youtube import youtube_api

# Create a YouTube object
youtube = youtube_api.YoutubeAPI("API_KEY")

# Get a video
video = youtube.get_video("VIDEO_ID")

# Get a channel
channel = youtube.get_channel("CHANNEL_ID")

# Get a playlist
playlist = youtube.get_playlist("PLAYLIST_ID")

```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.
