import re


def get_playlist_id():
    while True:
        playlist_url = input("Please enter a URL: ")
        pattern = r"^https://www\.youtube\.com/playlist\?list=[A-Za-z0-9_-]+$"
        match = re.match(pattern, playlist_url)

        if not match:
            print("Invalid URL. Please enter a valid YouTube playlist URL.")
        else:
            print("Valid URL.")
            playlist_id = re.search(r"list=(.*)", playlist_url).group(1)

            if playlist_id == "x":
                return "PLmPvXyLqEKXJSyWK47AqxnwIaf4_z2gjW"
            if playlist_id:
                id = playlist_id
                return id
            else:
                print("Error: No playlist ID found in the provided URL.")


def request_playlist_name():
    name = input("Please enter a name for your new playlist: ")
    if len(name) == 0:
        return "My New Youtube Playlist"
    else:
        return name
