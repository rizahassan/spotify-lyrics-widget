import sys
import spotify as sp
import time

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_ACCESS_TOKEN = 'BQAnWfN7er18UuUMxbqDLLwK87IzwDc6Xsg20ngcLtRkF-ejytu2rvWX2jkmVz3ReD6O5E296BKfsNnkRLGqiJttuwHl_R3mt27plRkkokm9OHK1kFoyZYq5SfEwuXVLNXW-o-8PpLcK5RSlCaoCcw5Su2IMSd7dRob_eU1hL3D19be1VrdA8KeaHeZ3eq8wQ4FvOiCKyZYqx2-Clm2yARcYslJEQF0XlFaSfgoulPhy_wK66RgPMbrCktTaE1rrEsoMWF1zRAX4_bMrse2w2TeeePLmUG7-7ba0uTqOc7XT'
GENIUS_ACCESS_TOKEN = 'vNUTG15j16R3P1_szIA6cd9iEIrX19VBwFdCu4SE6zp1fDxuF_zL8m1PFiB2myWY'

def get_lyrics():
    current_track_id = None
    while True:

        player = sp.GetLyrics(GENIUS_ACCESS_TOKEN,SPOTIFY_ACCESS_TOKEN,SPOTIFY_GET_CURRENT_TRACK_URL)
        (new_track_id,lyric) = player.get_lyrics()

        if new_track_id != current_track_id:
            print(lyric)
            sys.stdout.flush()
            current_track_id = new_track_id

        time.sleep(1)

def get_song():

    player = sp.GetLyrics(GENIUS_ACCESS_TOKEN,SPOTIFY_ACCESS_TOKEN,SPOTIFY_GET_CURRENT_TRACK_URL)
    (song,artist) = player.get_current_track()
    print(song)
    sys.stdout.flush()

def get_artist():

    player = sp.GetLyrics(GENIUS_ACCESS_TOKEN,SPOTIFY_ACCESS_TOKEN,SPOTIFY_GET_CURRENT_TRACK_URL)
    (song,artist) = player.get_current_track()
    print(artist)
    sys.stdout.flush()

if __name__ == '__main__':
    get_lyrics()


