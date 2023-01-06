import requests 
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urlencode
import base64
import webbrowser
from dotenv import load_dotenv
import os
import pandas as pd
import json
from csv import writer

filename = input("Please type name of file: ")

load_dotenv()

client_id = os.getenv("CLIENT_ID", "")
client_secret = os.getenv("CLIENT_SECRET", "")
username = os.getenv("USERNAME", "")
redirect_url = os.getenv("REDIRECT_URL", "")

auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": redirect_url,
    "scope": "playlist-modify-public"
}

webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))
#copy code in the navigation bar and store it in .env

code = os.getenv("CODE","")

encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}

token_data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": redirect_url
}

r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

token = r.json()["access_token"]

print("token:",token)

class SongMetadata:

    def __init__(self):
        self.user_id = username
        self.token = token
        self.csv = filename
        self.tuples = self.get_song_names()

    # Step 1: Get list of tuples containing song and artist names from csv file.
    def get_song_names(self):
        df = pd.read_csv(self.csv)
        df = df.sample(frac=1) # shuffle the dataframe so songs are not ordered based on genre
        tuple_list = list(zip(df.track, df.artist))
        return tuple_list


    # Step 3: Get each song's Spotify uri
    #def get_spotify_uri(self, song, artist):
    
    def get_spotify_info(self, song, artist):
        query = "https://api.spotify.com/v1/search?query=track%3A{}&type=track&offset=0&limit=1".format(song, artist)
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.token)
            }
        )
        response_json = response.json()
        prettify_response_json = json.dumps(response_json, indent = 2)
        #print(prettify_response_json)
        try:
            uri = response_json["tracks"]["items"][0]["uri"]
        except:
            uri = 'N/A'
        try:
            artist_name = response_json["tracks"]["items"][0]["album"]["artists"][0]["name"]
        except:
            artist_name = 'N/A'
        try:
            popularity = response_json["tracks"]["items"][0]["popularity"]
        except:
            popularity = 'N/A'    
        try:
            song_name = response_json["tracks"]["items"][0]["name"]
        except:
            song_name = 'N/A'    
        try:
            release_date = response_json["tracks"]["items"][0]["album"]["release_date"]
        except:
            release_date = 'N/A' 
        try:
            duration_ms = response_json["tracks"]["items"][0]["duration_ms"]
        except:
            duration_ms = 'N/A' 
        
        #songs = response_json["tracks"]
        
        #songs = prettify_response_json
        #print("type of response_json",type(response_json))
        #print("response_json:",prettify_response_json,'\n')
        #print("type of duration_ms",type(duration_ms))
       # print("duration_ms:", duration_ms)
        
        # URI
        #uri = songs[0]["uri"]
        
        #print("uri:",uri)
        #return uri
        return song_name, artist_name, uri, release_date, duration_ms, popularity

    # Step 4: Add songs to a list
    def add_to_list(self):
        '''
        uri_s = []
        artist_name_s = []
        popularity_s = [] 
        song_name_s = []
        release_date_s = [] 
        duration_ms_s = [] 
        '''
        info = []
        
        # Loop through tuples and get URIs
        for i, j in self.tuples[:10]:
            info.append(self.get_spotify_info(i, j))
            
        print("info: ", info)
        print("type of info", type(info))
        return info

if __name__ == '__main__':
    cp = SongMetadata()
    data = cp.add_to_list()
    
    header = ['Song Name','Artist Name', 'uri', 'Release Date','Duration (ms)','Popularity']
    with open('spotify_output.csv','w', encoding = 'UTF-8', newline = '') as f:
        w = writer(f)
        w.writerow(header)
        for row in data:
            w.writerow(row)

