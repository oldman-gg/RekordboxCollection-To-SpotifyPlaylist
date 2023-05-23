#Rekordbox Collection Spotify URI Finder

This script searches for Spotify URIs corresponding to the songs listed in a exported Rekordbox CSV file. The Spotify URIs are then added back into the CSV file.

The script uses the Spotipy, Pandas, and FuzzyWuzzy libraries to perform its functions.

## Dependencies
- pandas
- spotipy
- fuzzywuzzy

You can install these dependencies via pip:

```
pip install pandas spotipy fuzzywuzzy python-Levenshtein
```

Note: `python-Levenshtein` is an optional speedup for FuzzyWuzzy library.

## Usage

First, make sure to import your Spotify API credentials and Rekordbox .csv file paths:

```python
from environment_variables import spotify_client_id, spotify_client_secret, rekordbox_csv, rekordbox_csv_output
```

The `environment_variables.py` file should look like this:

```python
spotify_client_id = "your_spotify_client_id"
spotify_client_secret = "your_spotify_client_secret"
rekordbox_csv = "path_to_your_rekordbox_csv"
output = "path_to_your_output_csv"
```
Note: https://developer.spotify.com/ is where you will generate / find your Spotify client ID and secret 

To run the script:

```
python script_name.py
```

Replace `script_name.py` with the name of your script.

## Rekordbox Collection .CSV File
To get your Rekordbox collection into a .csv:
1. Add all of your songs to a single playlist
2. Playlist -> Export a playlist to a file ->
4. Import file into a spreadsheet (I recommend Google Sheets as schema detection works well)
5. File -> Export/Save As -> .csv

## How it works

1. Set up Spotify client with your Spotify API credentials.

2. Read the CSV file with pandas.

3. Create a new column 'spotify_uri' and initialize it with None.

4. Create a list of queries, which are combinations of the 'Artist' and 'Track Title' fields of each row in the dataframe.

5. Iterate over the queries and search for the song on Spotify. If an error occurs during the search, it will print the error and continue with the next query.

6. For each track in the search results, it compares the song name in the CSV file with the song name on Spotify using fuzzy matching. The threshold for the fuzzy matching can be adjusted as needed.

7. If a match is found, it will update the 'spotify_uri' column with the Spotify URI of the track and stop checking other tracks for that query.

8. Finally, it will write the dataframe back to the CSV file.

## Error Handling

The script has basic error handling for file not found error and Spotipy exceptions. It prints a helpful error message and continues with the rest of the processing. This ensures that a single error does not stop the whole process.

## Customization

You can customize the fuzzy matching threshold and the CSV file paths according to your needs.  I recommend using 95 from limited testing.
