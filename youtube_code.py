from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def get_video_titles(playlist_id):
    API_KEY = 'Your_YouTube_Data_API_Key'

    youtube = build('youtube', 'v3', developerKey=API_KEY
                    )

    # Retrieve the list of videos in the playlist
    try:
        playlist_items = []
        next_page_token = None
        while True:
            playlist_request = youtube.playlistItems().list(
                part='snippet',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
            )
            playlist_response = playlist_request.execute()
            playlist_items += playlist_response['items']
            next_page_token = playlist_response.get('nextPageToken')
            if not next_page_token:
                break
    except HttpError as e:
        print(f'An error occurred: {e}')
        playlist_items = None

    # Print the list of video titles
    if playlist_items is not None:
        return playlist_items
    else:
        return []
