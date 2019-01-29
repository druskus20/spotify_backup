import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

def run():
    
    keys = [line.rstrip('\n') for line in open('credentials.txt')]
    
    #print(keys)    
    os.environ['SPOTIPY_CLIENT_ID'] = keys[0]
    os.environ['SPOTIPY_CLIENT_SECRET'] = keys[1]
    username = keys[2]

    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    output_file = open('output.out', 'w')
    output_file.write('{\n')
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        output_file.write(' "playlist": {\n')
        output_file.write('  "name": %s\n' % playlist['name'])    
        output_file.write('  "total tracks": %s\n' % playlist['tracks']['total'])    
        print ('PLAYLIST: ' + playlist['name'])
        print ('TOTAL TRACKS: ', playlist['tracks']['total'])
        results = sp.user_playlist(username, playlist['id'],
            fields="tracks,next")
        output_file.write('  "tracks": [\n')    
        tracks = results['tracks']
        print_tracks(output_file, tracks)
       
        while tracks['next']:
            tracks = sp.next(tracks)   
            print_tracks(output_file, tracks)
        output_file.write('   null\n')
        output_file.write('  ]\n')
        output_file.write(' }\n')
    output_file.write('}\n')
    output_file.close()

def print_tracks(output_file, tracks):
    for item in tracks['items']:
        track = item['track']
        output_file.write('   {"name": %s, "author": %s },\n' % (track['artists'][0]['name'], track['name']))
        print ("%s - %s" % (track['artists'][0]['name'], track['name']))


if __name__ == "__main__":
    run()