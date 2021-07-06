import sys
import spotify as sp
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_ACCESS_TOKEN = 'BQDaivubunCCCX1Jis_jaVnPMYQz6tZ3sDP4PCaE5EDk7uuGy4wAVZhC_ELImKlsHnFg7t9zpy6EIrWmNz49iD3RDh8sm2z1CurqqkNpL3XbFKHolAuSu8ie16P_D8pLquIvU_uYrILCVNQBBWujrf5ftPJXyQFjzC_eIYwsiU1_s0tWob4qIiVfOlxq2DXSUJNmEZ8vUGnTVnZ-59qjNU-TTHNISKmgGmIUgD9fEuBCEIDljyWfszpXzEl7tpDF05Ljz_S95-WS2jaQ2r4DsST51L531EjFr1iRonIh_Dp1'
GENIUS_ACCESS_TOKEN = 'vNUTG15j16R3P1_szIA6cd9iEIrX19VBwFdCu4SE6zp1fDxuF_zL8m1PFiB2myWY'
SPOTIFY_CLIENT_ID = 'f89255531ce34918923ba80a46b1d54a'
SPOTIFY_CLIENT_SECRET = '18228304d10c48e0a54a3f3ef558cc27'
scope = "user-read-playback-state"

# sp = SpotifyOAuth(
#     client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri = "http://localhost/callback",scope=scope)

# Get spotify access token after user authenticate
def authenticate():
    access_token = ""

    token_info = sp.get_access_token()

    if token_info:
        # print("Found cached token!")
        # access_token = token_info['access_token']
        print(token_info)
        sys.stdout.flush()
    # else:
    #     url = request.url
    #     code = sp_oauth.parse_response_code(url)
    #     if code:
    #         print "Found Spotify auth code in Request URL! Trying to get valid access token..."
    #         token_info = sp_oauth.get_access_token(code)
    #         access_token = token_info['access_token']
    

def get_lyrics():
    current_track_id = None
    while True:

        player = sp.GetLyrics(
            GENIUS_ACCESS_TOKEN, SPOTIFY_ACCESS_TOKEN, SPOTIFY_GET_CURRENT_TRACK_URL)
        (new_track_id, lyric) = player.get_lyrics()

        if new_track_id != current_track_id:
            print(lyric)
            sys.stdout.flush()
            current_track_id = new_track_id

        time.sleep(1)


def get_song():

    current_song = None
    while True:
        player = sp.GetLyrics(
            GENIUS_ACCESS_TOKEN, SPOTIFY_ACCESS_TOKEN, SPOTIFY_GET_CURRENT_TRACK_URL)
        (new_song, artist) = player.get_current_track()

        if new_song != current_song:
            print(new_song)
            sys.stdout.flush()
            current_song = new_song

        time.sleep(1)


def get_artist():
    current_artist = None
    while True:
        player = sp.GetLyrics(
            GENIUS_ACCESS_TOKEN, SPOTIFY_ACCESS_TOKEN, SPOTIFY_GET_CURRENT_TRACK_URL)
        (song, new_artist) = player.get_current_track()

        if new_artist != current_artist:
            print(new_artist)
            sys.stdout.flush()
            current_artist = new_artist

        time.sleep(1)


if __name__ == '__main__':

    if(sys.argv[1] == 'artist'):
        get_artist()
    if(sys.argv[1] == 'song'):
        get_song()
    if(sys.argv[1] == 'lyric'):
        get_lyrics()
    if(sys.argv[1] == 'authenticate'):
        authenticate()
