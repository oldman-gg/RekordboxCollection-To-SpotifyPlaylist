import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from fuzzywuzzy import fuzz

#Import Spotify API credentials and Rekordbox .csv
from environment_variables import spotify_client_id, spotify_client_secret, rekordbox_csv_input, output

#Set up Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Read the CSV file
try:
    df = pd.read_csv(rekordbox_csv_input)
except FileNotFoundError:
    print(f"File {rekordbox_csv_input} not found.")
    exit()

#Create a new column 'spotify_uri' and initialize it with None
df['spotify_uri'] = None

#Create a list of queries
queries = [f"{row['Artist']} {row['Track Title']}" for index, row in df.iterrows()]

# Iterate over the queries
for index, query in enumerate(queries):
    try:
        # Search for the song on Spotify
        results = sp.search(query)
    except Exception as e:
        print(f"An error occurred: {e}")
        continue

    #Check if the song is available and update the 'spotify_uri' column accordingly
    for track in results['tracks']['items']:
        #Use fuzzy matching to compare the song name in the CSV file with the song name on Spotify
        spotify_song = track['name']
        spotify_artist = track['artists'][0]['name']  #assuming the first artist is the main artist
        spotify_query = f'{spotify_artist} {spotify_song}'
        if fuzz.ratio(query.lower(), spotify_query.lower()) > 90:  #you can adjust the threshold as needed
            df.loc[index, 'spotify_uri'] = track['uri']
            break  #stop checking other tracks once a match is found

# Write the DataFrame back to the CSV file
df.to_csv(output, index=False)