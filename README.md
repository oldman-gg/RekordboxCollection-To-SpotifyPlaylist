## Rekordbox Collection -> Spotify Playlist

![GitHub last commit](https://img.shields.io/github/last-commit/oldman-gg/Rekordbox-Spotify-URI-Finder)

This script allows you to match tracks from a Rekordbox CSV file with their corresponding tracks on Spotify, exports the Spotify URI to the corresponding row in .csv, and adds tracks to a Spotify playlist. It utilizes the Spotipy library, a Python wrapper for the Spotify Web API, and the fuzzywuzzy library for fuzzy string matching.

### Features
- Matches tracks from a Rekordbox CSV file with their corresponding tracks on Spotify.
- Uses fuzzy string matching to handle slight variations in song names.
- Updates the CSV file with the Spotify URIs of the matching tracks.
- Adds the matching tracks to a specified Spotify playlist.

### Prerequisites
Before using this script, make sure you have the following:

- Python 3.x installed on your system.
- The necessary dependencies: `pandas`, `spotipy`, `fuzzywuzzy`.
- Rekordbox collection .csv file

To create the Rekordbox file, add the songs you want to a given Rekordbox playlist, Playlist > Export playlist to a file > Export playlist to a file (*.txt)  
  

### Installation
1. Clone the repository:

```bash
git clone https://github.com/your-username/Rekordbox-Spotify-URI-Finder.git
```

2. Set up the environment variables by creating a file named `environment_variables.py`in the project root directory. Open the file and define the following variables:
```python
spotify_client_id = 'your-client-id' #found on https://developer.spotify.com/
spotify_client_secret = 'your-client-secret' #found on https://developer.spotify.com/
username = 'your-spotify-username'
playlist_id = 'your-spotify-playlist-id'
rekordbox_csv_input = 'path-to-rekordbox-csv-file.csv'
output = 'path-to-output-csv-file.csv'
redirect_uri = 'your-redirect-uri' #try http://localhost:8080/callback
```
**Note:** In the project, you will see an example `environment_variables.py` titled `environment_variables_git.py`

**Note:** Make sure that you add http://localhost:8080/callback to your redirect uri within your Spotify App settings.

### Usage
To use the script, simply run the following command:
```bash
python Spotify_Main.py
```
The script will start processing the Rekordbox CSV file and matching the tracks with their corresponding tracks on Spotify. The progress and any errors encountered will be displayed in the console. Once the matching process is complete, the updated CSV file will be saved to the specified output file and the tracks will be added to the specific playlist.
### Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository. If you'd like to contribute code, please fork the repository, create a new branch, make your changes, and submit a pull request.

### Acknowledgements

- The Spotipy library: [https://spotipy.readthedocs.io](https://spotipy.readthedocs.io)
- The fuzzywuzzy library: [https://github.com/seatgeek/fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy)