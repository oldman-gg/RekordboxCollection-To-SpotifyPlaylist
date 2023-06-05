import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from fuzzywuzzy import fuzz

#import Spotify API credentials and Rekordbox .csv
from environment_variables import spotify_client_id, spotify_client_secret, rekordbox_csv_input, output, username, playlist_id, redirect_uri

#set up Spotify client
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id, client_secret=spotify_client_secret, redirect_uri=redirect_uri, scope=scope, username=username))

#read Rekordbox CSV file
try:
    df = pd.read_csv(rekordbox_csv_input)
except FileNotFoundError:
    print(f"File {rekordbox_csv_input} not found.")
    exit()

#create a new column 'spotify_uri' and initialize it with None
df['spotify_uri'] = None

#create a list of queries
queries = [f"{row['Artist']} {row['Track Title']}" for index, row in df.iterrows()]

#iterate over the queries
for index, query in enumerate(queries):
    try:
        # Search for the song on Spotify
        results = sp.search(query)
    except Exception as e:
        print(f"An error occurred: {e}")
        continue

    #check if the song is available and update the 'spotify_uri' column accordingly
    for track in results['tracks']['items']:
        #use fuzzy matching to compare the song name in the CSV file with the song name on Spotify
        spotify_song = track['name']
        spotify_artist = track['artists'][0]['name']  #assuming the first artist is the main artist
        spotify_query = f'{spotify_artist} {spotify_song}'
        if fuzz.ratio(query.lower(), spotify_query.lower()) > 90:  #you can adjust the threshold as needed
            df.loc[index, 'spotify_uri'] = track['uri']
            # Add track to the playlist
            try:
                sp.user_playlist_add_tracks(username, playlist_id, [track['uri']])
            except Exception as e:
                print(f"Failed to add track to playlist: {e}")
            break  #stop checking other tracks once a match is found

# Write the DataFrame back to the CSV file
df.to_csv(output, index=False)  #replace with your rekordbox file