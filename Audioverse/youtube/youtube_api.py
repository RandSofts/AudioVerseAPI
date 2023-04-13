import requests
from bs4 import BeautifulSoup
import json

class YoutubeAPI(object):
    def __init__(self, api_key):
        self.api_key = api_key


    def search(self, query, max_results=10):
        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            "part": "snippet",
            "q": query,
            "key": self.api_key,
            "maxResults": max_results,
            "type": "video",
        }
        r = requests.get(url, params=params)
        return r.json()
    
    def get_channel(self, channel_id):
        url = "https://www.googleapis.com/youtube/v3/channels"
        params = {
            "part": "snippet",
            "id": channel_id,
            "key": self.api_key,
        }
        r = requests.get(url, params=params)
        return r.json()

    def get_video(self, video_id):
        url = "https://www.googleapis.com/youtube/v3/videos"
        params = {
            "part": "snippet",
            "id": video_id,
            "key": self.api_key,
        }
        r = requests.get(url, params=params)
        return r.json()
    
    def get_playlist(self, playlist_id):
        url = "https://www.googleapis.com/youtube/v3/playlistItems"
        params = {
            "part": "snippet",
            "playlistId": playlist_id,
            "key": self.api_key,
        }
        r = requests.get(url, params=params)
        return r.json()
    
    def get_playlist_videos(self, playlist_id):
        url = "https://www.googleapis.com/youtube/v3/playlistItems"
        params = {
            "part": "snippet",
            "playlistId": playlist_id,
            "key": self.api_key,
        }
        r = requests.get(url, params=params)
        return r.json()
    
    def get_playlist_videos(self, playlist_id):
        url = "https://www.googleapis.com/youtube/v3/playlistItems"
        params = {
            "part": "snippet",
            "playlistId": playlist_id,
            "key": self.api_key,
        }
        r = requests.get(url, params=params)
        return r.json()
    
    def get_playlist_videos(self, playlist_id):
        url = "https://www.googleapis.com/youtube/v3/playlistItems"
        params = {
            "part": "snippet",
            "playlistId": playlist_id,
            "key": self.api_key,
        }
        r = requests.get(url, params=params)
        return r.json()
