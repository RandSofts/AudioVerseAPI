import requests
from bs4 import BeautifulSoup
import json

class SpotifyAPI(object):
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = self.get_token()

    def get_token(self):
        url = "https://accounts.spotify.com/api/token"
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        r = requests.post(url, data=data)
        token = r.json()["access_token"]
        return token
    
    def get_track(self, track_id):
        url = f"https://api.spotify.com/v1/tracks/{track_id}"
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(url, headers=headers)
        return r.json()
    
    def get_artist(self, artist_id):
        url = f"https://api.spotify.com/v1/artists/{artist_id}"
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(url, headers=headers)
        return r.json()
    
    def get_album(self, album_id):
        url = f"https://api.spotify.com/v1/albums/{album_id}"
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(url, headers=headers)
        return r.json()
    
    def get_playlist(self, playlist_id):
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(url, headers=headers)
        return r.json()
    
    def get_track_features(self, track_id):
        url = f"https://api.spotify.com/v1/audio-features/{track_id}"
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(url, headers=headers)
        return r.json()
    
    def get_track_analysis(self, track_id):
        url = f"https://api.spotify.com/v1/audio-analysis/{track_id}"
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.get(url, headers=headers)
        return r.json()


class SpotifySearch(object):
    def __init__(self, query):
        self.query = query
        self.url = f"https://open.spotify.com/search/{self.query}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        self.r = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.r.text, "html.parser")
        self.json_data = json.loads(self.soup.find("script", {"id": "embedded-preloaded-data"}).text)
    
    def get_tracks(self):
        tracks = self.json_data["search"]["tracks"]["items"]
        return tracks
    
    def get_artists(self):
        artists = self.json_data["search"]["artists"]["items"]
        return artists
    
    def get_albums(self):
        albums = self.json_data["search"]["albums"]["items"]
        return albums
    
    def get_playlists(self):
        playlists = self.json_data["search"]["playlists"]["items"]
        return playlists
    
