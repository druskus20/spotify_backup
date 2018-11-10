# Spotify Playlist Exporter

This is a basic program written in Python (version 3.6) to generate a json file with your playlists and songs data.

It uses the Spotipy API and therefore the Spotify Web API
https://github.com/plamere/spotipy

## Setup:
 
You need Python 3.X to run this program.
Install the required packages with: 
    $ pip install -r requirements.txt

Create a file "credentials.txt" in the project root repository with:
    CLIENT_KEY
    CLIENT_SECRET
    user_name

Where CLIENT_KEY and CLIENT_SECRET are your user keys. You can find those key at: https://developer.spotify.com/dashboard/
To test, you can user the user_name "spotify"

(those keys are yet not encoded, im planning on doing so in the near future)

## Execution:

Run "$ python app.py"

