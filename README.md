# Spotify Playlist Exporter

This is a basic program written in Python (version 3.6) to generate a json file with your playlists and songs data.<br />

It uses the Spotipy API and therefore the Spotify Web API<br />
https://github.com/plamere/spotipy<br />

## Setup:
 
You need Python 3.X to run this program.<br />
Install the required packages with: <br />
    $ pip install -r requirements.txt<br />

Create a file "credentials.txt" in the project root repository with:<br />
    CLIENT_KEY<br />
    CLIENT_SECRET<br />
    user_name<br />

Where CLIENT_KEY and CLIENT_SECRET are your user keys. You can find those key at: https://developer.spotify.com/dashboard/<br />
To test, you can user the user_name "spotify"<br />

(those keys are yet not encoded, im planning on doing so in the near future)<br />

## Execution:

Run "$ python app.py"<br />

