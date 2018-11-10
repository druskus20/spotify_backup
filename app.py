import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

def run():
    
    keys = [line.rstrip('\n') for line in open('credentials.txt')]
    print(keys)
    os.environ['SPOTIPY_CLIENT_ID'] = keys[0]
    os.environ['SPOTIPY_CLIENT_SECRET'] = keys[1]
    #os.environ['SPOTIPY_REDIRECT_URI'] = "http://127.0.0.1:8080/callback"
    username = keys[2]

    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        print ()
        print (playlist['name'])
        print ('  total tracks', playlist['tracks']['total'])
        results = sp.user_playlist(username, playlist['id'],
            fields="tracks,next")
        tracks = results['tracks']
        show_tracks(tracks)
        while tracks['next']:
            tracks = sp.next(tracks)
            show_tracks(tracks)

def show_tracks(tracks):
    for item in tracks['items']:
        track = item['track']
        print ("%s - %s" % (track['artists'][0]['name'],
            track['name']))


if __name__ == "__main__":
    run()
