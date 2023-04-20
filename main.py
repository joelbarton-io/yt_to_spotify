from youtube_code import get_video_titles
from spotify_code import generate_playlist
from helpers import request_playlist_name, get_playlist_id

# fetch Playlist ID from user
youtube_playlist_id = get_playlist_id()

# fetch names of videos in YT playlist
playlist_items = get_video_titles(youtube_playlist_id)

# let user name their playlist
playlist_name = request_playlist_name()

# make spotify playlist
generate_playlist(playlist_name, playlist_items)
