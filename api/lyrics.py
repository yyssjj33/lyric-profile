from cfg.secrets import API_KEY
import requests
from utils.list_utils import flatten
from nlp.preprocess import analyse

base_url = "https://api.musixmatch.com/ws/1.1/"
matcher_lyrics_get = "{}track.lyrics.get".format(base_url)
artist_search = "{}artist.search".format(base_url)
artist_albums_get = "{}artist.albums.get".format(base_url)
album_tracks_get = "{}album.tracks.get".format(base_url)
track_lyrics_get = "{}track.lyrics.get".format(base_url)


def get_lyrics(title, artist=""):
    payload = {"apikey": API_KEY, "q_track": title, "q_artist": artist}
    resp = requests.get(matcher_lyrics_get, params=payload)
    return resp.json()


def get_artist(name):
    payload = {"apikey": API_KEY, "q_artist": name, "page_size": 5}
    resp = requests.get(artist_search, params=payload)
    if resp.json()["message"]["header"]["status_code"] == 200:
        if len(resp.json()["message"]["body"]["artist_list"]) == 0:
            return None
        return resp.json()["message"]["body"]["artist_list"][0]["artist"]["artist_id"]
    else:
        return None


def get_albums_by_artist(artist_id):
    if artist_id is None:
        return None
    payload = {"apikey": API_KEY, "artist_id": artist_id}
    resp = requests.get(artist_albums_get, params=payload)
    if resp.json()["message"]["header"]["status_code"] == 200:
        if len(resp.json()["message"]["body"]["album_list"]) == 0:
            return []
        return list(map(lambda x: x["album"]["album_id"], resp.json()["message"]["body"]["album_list"]))
    else:
        return []


def get_tracks_by_album(album_id):
    payload = {"apikey": API_KEY, "album_id": album_id}
    resp = requests.get(album_tracks_get, params=payload)
    if resp.json()["message"]["header"]["status_code"] == 200:
        if len(resp.json()["message"]["body"]["track_list"]) == 0:
            return []
        return list(map(lambda x: x["track"]["track_id"], resp.json()["message"]["body"]["track_list"]))[0:1]
    else:
        return []


def get_lyric_by_track(track_id):
    payload = {"apikey": API_KEY, "track_id": track_id}
    resp = requests.get(track_lyrics_get, params=payload)
    if resp.json()["message"]["header"]["status_code"] == 200:
        if len(resp.json()["message"]["body"]) == 0:
            return None
        return resp.json()["message"]["body"]["lyrics"]["lyrics_body"]
    else:
        return None


def get_lyrics_by_artist(name):
    artist_id = get_artist(name)
    album_ids = get_albums_by_artist(artist_id)
    track_ids = flatten(list(map(get_tracks_by_album, album_ids)))
    return list(map(get_lyric_by_track, track_ids))


def get_lyrics_and_analyse(name):
    lyrics = get_lyrics_by_artist(name)
    res = analyse(lyrics)
    return res

