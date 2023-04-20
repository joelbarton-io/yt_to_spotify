import spotipy
from spotipy.oauth2 import SpotifyOAuth


def generate_playlist(playlist_name, playlist_items):
    # Replace with your own client ID and client secret
    CLIENT_ID = 'Your_Spotify_Client_ID'
    CLIENT_SECRET = 'Your_Spotify_Client_Secret'

    # Replace with the ID of your Spotify account
    USERNAME = 'YOUR_SPOTIFY_USERNAME/ID'

    # Authenticate with the Spotify API
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri='http://localhost:8888/callback',
        scope='playlist-modify-public',
        username=USERNAME
    ))

    # Create a new playlist
    playlist = sp.user_playlist_create(USERNAME, playlist_name)

    # Add the tracks to the playlist
    for item in playlist_items:
        # Search for the track on Spotify
        title = item["snippet"]["title"]
        artist = item["snippet"].get("videoOwnerChannelTitle", "")
        query = f"{title} {artist}"
        results = sp.search(query, limit=1, type="track")

        if results["tracks"]["items"]:
            track = results["tracks"]["items"][0]["uri"]
            sp.user_playlist_add_tracks(USERNAME, playlist["id"], [track])
            print(
                f'Added "{results["tracks"]["items"][0]["name"]}" to the playlist.')
        else:
            print(f'Could not find a track for "{title}".')
