# Spotify Playlist Exporter

This is a basic program written in Python that generate a json file from your Spotify playlists .<br />

It uses the Spotipy module and therefore the Spotify Web API<br />
https://github.com/plamere/spotipy<br />

## Setup:
 
You will need Python 3.X to run this program.<br />
Install the required packages with: <br />
    `$ pip install -r requirements.txt`<br />

Create a file "credentials.txt" in the project root repository with:<br />
    CLIENT_KEY<br />
    CLIENT_SECRET<br />
    Spotify username<br />
This isnt in any way a a safe method for storing credentials, since I only use this script from time to time, I prefer to just remove the credentials.txt file everytime. A safer alternative can be achieved by using [gpg](https://gnupg.org/)

Where CLIENT_KEY and CLIENT_SECRET are your user keys. You can find those key at: https://developer.spotify.com/dashboard/<br />
To test the program, you can use the username "spotify"<br />

## Execution:

Simply run `$ python app.py`<br />

