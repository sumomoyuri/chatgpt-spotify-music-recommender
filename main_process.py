import global_value as gv
from chatgpt_api import *
from spotify_api import *

##################################################################
### function for user authorization
##################################################################
def authorization():
    print("start user authorization...\n")
    requestUserAuthorization()
    print("Prease enter the avobe URL on browser, and input 'code' in redirected URL into the input field below..")
    gv.CODE = input("code: ")
    gv.SPOTIFY_TOKEN = authenticateSpotifyAPI() # authentication Spotify API
    gv.USER_ID = getSpotifyUserID() # getting spotify UserID

##################################################################
### function to initialize prompts
##################################################################

def initialization():
    gv.GENRES_LIST = getSpotifyGenres() # getting spotify music genre
    gv.GENRES_TEXT = "\n".join(gv.GENRES_LIST) # convert genre list into plain text
    createPromptGENRES()
    createPromptPARAMS()


##################################################################
### function to get recommendation using ChatGPT & Spotify API
##################################################################

def getRecomandation(input_question: str) -> dict:
  # get recommend genres
  recommend_genres = getRecommendedGenres(input_question)
  # get recommend params
  recommend_params = getRecommendedParams(input_question)
  # get recommend tracks
  recommend_tracks = getRecommendedtracks(recommend_genres, recommend_params)
  return recommend_tracks


##################################################################
### function to create recommended playlist
##################################################################

def createSpotifyPlaylist(user_input: str, recommend_tracks: dict):
  print("creating playlist started...")
  track_uris = []
  for track in recommend_tracks['tracks']:
    track_uris.append(track['uri'])
    # print(f"Artist: {track['artists'][0]['name']}")
    # print(f"Title: {track['name']}")
    # print(f"URL: {track['artists'][0]['external_urls']['spotify']}\n")
  playlist_id, playlist_url = createSpotifyEmptyPlaylist(user_input)
  addTracksToSpotifyPlaylist(playlist_id, track_uris)
  print("Playlist is successfully created!")
  print(f"playlist's URL: {playlist_url}\n")