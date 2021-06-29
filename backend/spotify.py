import requests
import time
from bs4 import BeautifulSoup
from pprint import pprint
import urllib



class GetLyrics():

    def __init__(self, genius_key, access_token,spotify_url):
        self.genius_key = genius_key
        self.spotify_token = access_token
        self.spotify_url = spotify_url


    def get_current_track(self):
        response = requests.get(
            self.spotify_url,
            headers={
                "Authorization": f"Bearer {self.spotify_token}"
            }
        )
        json_resp = response.json()

        track_id = json_resp['item']['id']
        track_name = json_resp['item']['name']
        artists = [artist for artist in json_resp['item']['artists']]

        link = json_resp['item']['external_urls']['spotify']

        # artist_names = ', '.join([artist['name'] for artist in artists])
        artist_names = artists[0]['name']
        current_track_info = {
            "id": track_id,
            "track_name": track_name,
            "artists": artist_names,
            "link": link
        }
        self.track_id = track_id
        self.track_name = track_name
        self.track_artists = artist_names

        return (self.track_name,self.track_artists)

    def request_song_info(self,track_name, track_artist):
        base_url = 'http://api.genius.com'
        headers = {'Authorization': 'Bearer ' + self.genius_key}
        data = track_name + ' ' + track_artist
        data = data.replace(" ","%20")

        search_url = base_url + '/search?q=' + data
        
        response = requests.get(search_url, headers=headers)
        self.response = response
        return self.response
    
    def check_hits(self):
        json = self.response.json()
        remote_song_info = None
        
        for hit in json['response']['hits']:
            
            if self.track_artists.lower() in hit['result']['primary_artist']['name'].lower():
                remote_song_info = hit
                break
        self.remote_song_info = remote_song_info
        return self.remote_song_info
    
    def get_url(self):
        song_url = self.remote_song_info['result']['url']
        self.song_url = song_url
        return self.song_url

    def scrape_lyrics(self):
        page = requests.get(self.song_url)
        html = BeautifulSoup(page.text, 'html.parser')
        lyrics1 = html.find("div", class_="lyrics")
        lyrics2 = html.find("div", class_="Lyrics__Container-sc-1ynbvzw-7 jjqBBp")
        if lyrics1:
            lyrics = lyrics1.get_text()
        elif lyrics2:
            lyrics = lyrics2.get_text()
        elif lyrics1 == lyrics2 == None:
            lyrics = None
        return lyrics
    
    def get_lyrics(self):
        (track_name,track_artists) = GetLyrics.get_current_track(self)
        song_lyrics = []
        response = GetLyrics.request_song_info(self, self.track_name, self.track_artists)
        remote_song_info = GetLyrics.check_hits(self)
        if remote_song_info == None:
            lyrics = None
            print(f"Track {self.track_name} is not in the Genius database.")
        else:
            url = GetLyrics.get_url(self)
            lyrics = GetLyrics.scrape_lyrics(self)
            if lyrics == None:
                print(f"Track {self.track_name} is not in the Genius database.")
            else:
                print(f"Retrieved track {self.track_name} lyrics!")
        song_lyrics.append(lyrics)
        return (self.track_id,song_lyrics)

# def main():
#     current_track_id = None
#     while True:

#         player = GetLyrics(GENIUS_ACCESS_TOKEN,SPOTIFY_ACCESS_TOKEN,SPOTIFY_GET_CURRENT_TRACK_URL)
#         (new_track_id,lyric) = player.get_lyrics()

#         if new_track_id != current_track_id:
#             print(lyric)
#             current_track_id = new_track_id

#         time.sleep(1)

	# current_track_id = None
	# while True:
	#     current_track_info = get_current_track(ACCESS_TOKEN)

	#     if current_track_info['id'] != current_track_id:
	# 	    pprint(
	# 	    	current_track_info,
	# 	    	indent=4,
	# 	    )
	# 	    current_track_id = current_track_info['id']

	#     time.sleep(1)

if __name__ == '__main__':
    main()