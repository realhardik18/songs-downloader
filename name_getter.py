from requests.models import RequestEncodingMixin
import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(
    client_id="xxx",
    client_secret="xxx"
)

sp = spotipy.Spotify(auth_manager=auth_manager)


def track_name_getter(user, playlist_id):
    track_ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        track_ids.append(track['id'])
    song_names = []
    for track_id in track_ids:
        track_info = sp.track(track_id)
        name = track_info["name"]
        song_names.append(name)
    return song_names
