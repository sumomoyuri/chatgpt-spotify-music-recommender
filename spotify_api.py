import global_value as gv
import random
import string
import requests
import urllib.parse
import base64
import json

##################################################
### function to prepare for authenticate Spotify API
##################################################

def requestUserAuthorization() -> str:
  state = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))
  scope = "playlist-modify-public playlist-modify-private user-read-private user-read-email"
  params = {
      'response_type': 'code',
      'client_id': gv.CLIENT_ID,
      'scope': scope,
      'redirect_uri': gv.REDIRECT_URI,
      'state': state
  }
  endpoint = f'https://accounts.spotify.com/authorize?{urllib.parse.urlencode(params)}'
  response = requests.post(endpoint)
  print(f"{endpoint}\n")


##################################################
### function to authenticate Spotify API
##################################################
# ref: https://developer.spotify.com/documentation/web-api

def authenticateSpotifyAPI() -> str:
  # print("authenticating Spotify user...")
  spotify_token = None
  headers = {"Authorization": "Basic " + (base64.b64encode((gv.CLIENT_ID + ":" + gv.CLIENT_SECRET).encode())).decode()}
  data = {
    'code': gv.CODE,
    'redirect_uri': gv.REDIRECT_URI,
    'grant_type': "authorization_code"
  }
  response = requests.post("https://accounts.spotify.com/api/token", data=data, headers=headers)
  if response.status_code == 200:
    response = json.loads(response.content.decode())
    spotify_token = response['access_token']
    print("authentication is successed!\n")
  else:
    print(f"Error {response.status_code}: {response.text}")
  return spotify_token


##################################################
### function to get Spotify userID
##################################################
# ref: https://developer.spotify.com/documentation/web-api/reference/get-current-users-profile

def getSpotifyUserID() -> str:
  # print("getting Spotify's userID...")
  user_id = None
  endpoint = "https://api.spotify.com/v1/me"
  headers = {'Authorization': f"Bearer {gv.SPOTIFY_TOKEN}"}
  response = requests.get(endpoint, headers=headers)
  if response.status_code == 200:
    data = response.json()
    user_id = data['id']
    # print("UserID is successfully returned!\n")
  else:
    print(f"Error {response.status_code}: {response.text}")
  return user_id

##################################################
### function to get spotify music genre
##################################################
# ref: https://developer.spotify.com/documentation/web-api/reference/get-recommendation-genres

def getSpotifyGenres() -> list:
  # print("getting Spotify's music genres...")
  genres_list = []
  endpoint = "https://api.spotify.com/v1/recommendations/available-genre-seeds"
  headers = {'Authorization': f"Bearer {gv.SPOTIFY_TOKEN}"}
  response = requests.get(endpoint, headers=headers)
  if response.status_code == 200:
    data = response.json()
    genres_list = data['genres']
    # print(f"genres: {genres_list}") 
    # print(f"Total: {len(genres_list)} genres\n")
  else:
    print(f"Error {response.status_code}: {response.text}")
  return genres_list


##################################################################
### function to get recommended tracks using Spotify API with genres and params as args
##################################################################
# ref: https://developer.spotify.com/documentation/web-api/reference/get-recommendations

def getRecommendedtracks(genres: list, params: dict) -> dict:
  # print("getting Spotify's recommendation...")
  recommend_tracks = None
  genres_join = ",".join(genres)
  params = {
    "seed_genres": genres_join,
    "limit": gv.LIMIT,
    "target_acousticness": params['target_acousticness'],
    "target_danceability": params['target_danceability'],
    "target_energy": params['target_energy'],
    "target_instrumentalness": params['target_instrumentalness'],
    "target_valence": params['target_valence']
  }  
  endpoint = f'https://api.spotify.com/v1/recommendations?{urllib.parse.urlencode(params)}'
  headers = {'Authorization': f"Bearer {gv.SPOTIFY_TOKEN}"}
  response = requests.get(endpoint, headers=headers)
  if response.status_code == 200:
    recommend_tracks = response.json()
    # print("Recommendation is returned!\n")
  else:
    print(f"Error {response.status_code}: {response.text}")
  return recommend_tracks


##################################################
### functions to create spotify playlist
##################################################
# ref: https://developer.spotify.com/documentation/web-api/reference/create-playlist
# ref: https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist

def createSpotifyEmptyPlaylist(user_input: str):
  # print("creating a empty playlist...")
  playlist_id = None
  playlist_url = None
  endpoint = f"https://api.spotify.com/v1/users/{gv.USER_ID}/playlists"
  payload = {
    "name": f"{user_input}",
    "description": f"created using ChatGPT and Sportify's get recommendation based on the input {user_input}",
    "public": gv.IS_PUBLIC_PLAYLIST
  }
  headers = {
    'Authorization': f"Bearer {gv.SPOTIFY_TOKEN}",
    'Content-Type': 'application/json'
  }
  response = requests.post(endpoint, headers=headers, json=payload)
  if response.status_code == 201:
    data = response.json()
    playlist_id = data['id']
    playlist_url = data['owner']['external_urls']['spotify']
    # print("A empty  playlist is successfully created!\n")
  else:
    print(f"Error {response.status_code}: {response.text}")
  return playlist_id, playlist_url

def addTracksToSpotifyPlaylist(playlist_id: str, track_uris: str):
  # print("adding tracks to the playlist...")
  track_uris_join = ",".join(track_uris)
  endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?position=0&uris={track_uris_join}"
  payload = {
    "uris": ["string"],
    "position": 0
  }
  headers = {
    'Authorization': f"Bearer {gv.SPOTIFY_TOKEN}",
    'Content-Type': 'application/json'
  }
  response = requests.post(endpoint, headers=headers, json=payload)
  if response.status_code == 201:
    # print("Tracks is successfully added!\n")
    pass
  else:
    print(f"Error {response.status_code}: {response.text}")