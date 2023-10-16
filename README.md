# chatgpt-spotify-music-recommender

## Overview
This app creates a playlist of recommended tracks based on the user's natural language input, using ChatGPT API and Spotify API.  

## Preparation
you need to pay to use a [OpenAI account](https://platform.openai.com/login), and have a [Spotify Premium account](https://www.spotify.com/premium/).
Before using this app, please prepare the following three items.

1. Please create an API key from [the OpenAI account screen](https://platform.openai.com/account/api-keys) and obtain it.  
   <img width="500" alt="preparation_chatgpt" src="https://github.com/sumomoyuri/chatgpt-spotify-music-recommender/assets/116475757/c8fd9caf-75f0-40e6-96be-79a98e1f294c">


2. Please create any app from the [Spotify for Developers Dashboard](https://developer.spotify.com/dashboard) and retrieve the `Client ID`, `Client Secret` and `Redirect URIs` from the settings screen.  
   (`Redirect URIs` is whatever you originally entered, and it can be anything.)  
   <img width="500" alt="preparation_spotify" src="https://github.com/sumomoyuri/chatgpt-spotify-music-recommender/assets/116475757/54945f93-f705-4b62-bd06-ba99b5827a51">


3. Please Please fill in `OPENAI_API_KEY`, `REDIRECT_URI`, `CLIENT_ID`, `CLIENT_SECRET` in `global_values.py`.  
   <img width="500" alt="preparation" src="https://github.com/sumomoyuri/chatgpt-spotify-music-recommender/assets/116475757/87126128-1d63-48a9-ab7a-243478530f6f">


### Execution
Let's start with `python music_recommender.py`.

1. enter the avobe URL on browser, and input 'code' in redirected URL.
   example: http://localhost:3000/?code=AQDM_QoB...lDN_tlBJGef8&state=bYT6X8jpHttTKT43
   → code is `AQDM_QoB...lDN_tlBJGef8`
   
```  
user@host chatgpt-spotify-music-recommender % python music_recommender.py
start user authorization...

https://accounts.spotify.com/authorize?XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Prease enter the avobe URL on browser, and input `code` in redirected URL into the input field below..
code: 
```

   after authentication is successed, you can input the image of music you are looking for.
   example: 

```
Prease enter the avobe URL on browser, and input 'code' in redirected URL into the input field below..
code: XXXXXXXXXX(your input)
authentication is successed!

you: 
```

2. Based on your inout, chatGPT returns recommended music genres and parameters, which are then used by Spotify to create playlists of recommended songs.
   (ChatGPT recommends at least 1 up to 4 "music genres", and parameter ranges from 0 to 1.)
```
you: Teach me some upbeat Latin music.

ChatGPT's recommend_genres: ['salsa', 'latin', 'reggaeton', 'forro'], (NG_genres[])

ChatGPT's recommend_params: {'target_danceability': '1.0', 'target_acousticness': '0.5', 'target_energy': '1.0', 'target_instrumentalness': '0.5', 'target_valence': '1.0'}

creating playlist started...
Playlist is successfully created!
playlist's URL: https://open.spotify.com/user/XXXXXXXXXXXXXXXXXXXXX
```
   Please check playlist's URL, a playlist has been created. (default is 20 tracks) 
   <img width="500" alt="preparation" src="https://github.com/sumomoyuri/chatgpt-spotify-music-recommender/assets/116475757/6f6858b8-0bf9-464f-b9e4-904290a601f9">
   <img width="500" alt="preparation" src="https://github.com/sumomoyuri/chatgpt-spotify-music-recommender/assets/116475757/e0bee530-1c5f-4d18-846d-bda3cd4159ac">
