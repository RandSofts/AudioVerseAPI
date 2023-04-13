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