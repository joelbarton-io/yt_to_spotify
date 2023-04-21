Please note that this will require some setup steps and the use of third-party libraries, which I will explain along the way.

## Prep

- python needs to be installed on your machine as well as the python package manager `pip` (which should automatically download when you issue the: `brew install python` command)
- additionally, you need to have the `python` or `python3` executable to issue commands from the CLI (e.g. `python3 myprogram.py` runs the code present in the file `myprogram.py`)
- you obviously need a Google account and a Spotify account
- assuming you have all of the required software on your computer, we should be ready to begin initializing the two APIs

## Setting up the YouTube API

1. Go to the Google Developers Console. (https://console.developers.google.com/)
2. Create a new project.
3. In the project dashboard, click on "Enable APIs and Services".
4. Search for "YouTube Data API v3" and enable it.
5. Create a new API key in the "Credentials" section.

## Setting up the Spotify API

1. Go to the Spotify Developer Dashboard. (https://developer.spotify.com/dashboard/)
2. Create a new app.
3. In the app dashboard, click on "Edit Settings".
4. Add a new redirect URI (e.g. http://localhost:8888/callback), you can type whatever in the description box.
5. Copy the Client ID and Client Secret values.

Note that you will also need to install the necessary libraries for the code to run. You can do this by running the following commands in your terminal:

```zsh
pip3 install google-auth google-auth-oauthlib google-auth-httplib2
pip3 install spotipy
```

## Steps

1. In `youtube_code.py`, plug in the YouTube data `API_Key`
2. In `spotify_code.py`, plug in the Spotify `Client_ID`, `Client_Secret`, and your Spotify account username (mine is a number)
3. Theoretically, everything should be in order at this point. Using either the `python3` or `python` executable, type the following: `python3 main.py` into the command line and provide the requested information when prompted.
4. You should now be able to see a new playlist in your Spotify populated with the songs that were present in the original YouTube playlist whose URL you input in step 3.
