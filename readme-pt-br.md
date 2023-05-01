<table align="right">
 <tr><td><a href="https://github.com/isyuricunha/AudioVerseAPI/blob/main/README.md">:us: English</a></td></tr>
 <tr><td><a href="https://github.com/isyuricunha/AudioVerseAPI/blob/main/readme-pt-br.md">:brazil: Português</a></td></tr>
 <tr><td><a href="https://github.com/isyuricunha/AudioVerseAPI/blob/main/readme-fr.md">:fr: French</a></td></tr>
</table>

# AudioVerseAPI
AudioVerseAPI é um pacote Python para acessar e manipular dados relacionados à música. Ele fornece uma interface fácil de usar para interagir com a API do AudioVerse, que oferece um banco de dados abrangente de informações relacionadas à música, como artistas, álbuns, faixas e muito mais. Com o AudioVerseAPI, você pode acessar essas informações, extrair dados relevantes e executar várias operações neles.


## Instalação
Para instalar o AudioVerseAPI, simplesmente clone este repositório e execute o seguinte comando no diretório raiz:

```bash
pip install -r requirements.txt
```

## Uso
Para usar o AudioVerseAPI, importe o pacote e crie uma instância da classe AudioVerse:

```py
from Audioverse.spotify import spotify_api

# Cria um objeto do Spotify
spotify = spotify_api.SpotifyAPI(client_id="CLIENT_ID", client_secret="CLIENT_SECRET")

# Obter uma faixa
track = spotify.get_track("TRACK_ID")

# Obter um artista
artist = spotify.get_artist("ARTIST_ID")

# Obter um álbum
album = spotify.get_album("ALBUM_ID")

# Obter uma lista de reprodução
playlist = spotify.get_playlist("PLAYLIST_ID")
```

```py
from Audioverse.youtube import youtube_api

# Cria um objeto do YouTube
youtube = youtube_api.YoutubeAPI("API_KEY")

# Obter um vídeo
video = youtube.get_video("VIDEO_ID")

# Obter um canal
channel = youtube.get_channel("CHANNEL_ID")

# Obter uma lista de reprodução
playlist = youtube.get_playlist("PLAYLIST_ID")

```

## Licença
[MIT](https://choosealicense.com/licenses/mit/)

## Contribuição
Solicitações de pull são bem-vindas. Para alterações importantes, abra primeiro uma issue para discutir o que você gostaria de mudar. Por favor, certifique-se de atualizar os testes conforme apropriado.