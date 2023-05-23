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

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/spotify-rekordbox-track-matcher.git
```

2. Change to the project directory:

```bash
cd spotify-rekordbox-track-matcher
```

3. Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

4. Set up the environment variables by creating a file named `environment_variables.py` in the project root directory. Open the file and define the following variables:

```python
spotify_client_id = 'your-client-id'
spotify_client_secret = 'your-client-secret'
rekordbox_csv_input = 'path-to-rekordbox-csv-file.csv'
output = 'path-to-output-csv-file.csv'
username = 'your-spotify-username'
playlist_id = 'your-spotify-playlist-id'
redirect_uri = 'your-redirect-uri'
```

Make sure to replace `'your-client-id'`, `'your-client-secret'`, `'path-to-rekordbox-csv-file.csv'`, `'path-to-output-csv-file.csv'`, `'your-spotify-username'`, `'your-spotify-playlist-id'`, and `'your-redirect-uri'` with the appropriate values.

### Usage

To use the script, simply run the following command:

```bash
python Spotify_Main.py
```

The script will start processing the Rekordbox CSV file and matching the tracks with their corresponding tracks on Spotify. The progress and any errors encountered will be displayed in the console. Once the matching process is complete, the updated CSV file will be saved to the specified output file.

### Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository. If you'd like to contribute code, please fork the repository, create a new branch, make your changes, and submit a pull request.

### Acknowledgements

- The Spotipy library: [https://spotipy.readthedocs.io](https://spotipy.readthedocs.io)
- The fuzzywuzzy library: [https://github.com/seatgeek/fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy)