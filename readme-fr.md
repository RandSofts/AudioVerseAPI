<table align="right">
 <tr><td><a href="https://github.com/isyuricunha/AudioVerseAPI/blob/main/README.md">:us: English</a></td></tr>
 <tr><td><a href="https://github.com/isyuricunha/AudioVerseAPI/blob/main/readme-pt-br.md">:brazil: Português</a></td></tr>
 <tr><td><a href="https://github.com/isyuricunha/AudioVerseAPI/blob/main/readme-fr.md">:fr: French</a></td></tr>
</table>

# AudioVerseAPI
AudioVerseAPI est une bibliothèque Python pour accéder et manipuler des données liées à la musique. Il fournit une interface facile à utiliser pour interagir avec l'API AudioVerse, qui offre une base de données complète d'informations liées à la musique telles que les artistes, les albums, les pistes et bien plus encore. Avec AudioVerseAPI, vous pouvez accéder à ces informations, extraire les données pertinentes et effectuer diverses opérations dessus.


## Installation
Pour installer AudioVerseAPI, il suffit de cloner ce dépôt et d'exécuter la commande suivante dans le répertoire racine:

```bash
pip install -r requirements.txt
```

## Usage
Pour utiliser AudioVerseAPI, importez le package et créez une instance de la classe AudioVerse:

```py
from Audioverse.spotify import spotify_api

# Créer un objet Spotify
spotify = spotify_api.SpotifyAPI(client_id="CLIENT_ID", client_secret="CLIENT_SECRET")

# Obtenir une piste
track = spotify.get_track("TRACK_ID")

# Obtenir un artiste
artist = spotify.get_artist("ARTIST_ID")

# Obtenir un album
album = spotify.get_album("ALBUM_ID")

# Obtenir une liste de lecture
playlist = spotify.get_playlist("PLAYLIST_ID")
```

```py
from Audioverse.youtube import youtube_api

# Créer un objet YouTube
youtube = youtube_api.YoutubeAPI("API_KEY")

# Obtenir une vidéo
video = youtube.get_video("VIDEO_ID")

# Obtenir une chaîne
channel = youtube.get_channel("CHANNEL_ID")

# Obtenir une liste de lecture
playlist = youtube.get_playlist("PLAYLIST_ID")

```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contribuer
Les demandes de pull sont les bienvenues. Pour les changements importants, veuillez ouvrir une issue d'abord pour discuter de ce que vous souhaitez changer. Veuillez vous assurer de mettre à jour les tests si nécessaire.