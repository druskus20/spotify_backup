import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

def run():
    
    keys = [line.rstrip('\n') for line in open('credentials.txt')]
    print(keys)
    os.environ['SPOTIPY_CLIENT_ID'] = keys[0]
    os.environ['SPOTIPY_CLIENT_SECRET'] = keys[1]
    #os.environ['SPOTIPY_REDIRECT_URI'] = "http://127.0.0.1:8080/callback"


    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


    playlists = sp.user_playlists(keys[2])
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
if __name__ == "__main__":
    run()