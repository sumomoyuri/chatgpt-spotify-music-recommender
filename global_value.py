
LIMIT = 20 # upper limit on number of recommended tracks (default = 20)
IS_PUBLIC_PLAYLIST = False # playlist's public/private status

OPENAI_API_KEY = "<your API key>" # setting OpenAI API key

REDIRECT_URI = 'http://XXXXXXXXXXXXXXX' # for Spotify authentication
CLIENT_ID = "<your client ID>" # Spotify client ID
CLIENT_SECRET = "<your client secret>" # Spotify client secret

# CODE = None # authorization() 
# SPOTIFY_TOKEN = None # authenticateSpotifyAPI() # authentication Spotify API
# USER_ID = None # getSpotifyUserID() # getting spotify UserID
# GENRES_LIST = None # getSpotifyGenres() # getting spotify music genre
# GENRES_TEXT = None # "\n".join(GENRES_LIST) # convert genre list into plain text

#common prompt for genres selection and params setting
PROMPT_COMMON = '''
You are an assistant that recommends music perfectly suited for the customer.
The customer will ask you about the image of music they might want to hear.
'''
#prompt for genres selection
PROMPT_GENRES = '''
Please select at least 1 up to 4 "music genres" you would recommend, from the following choices of "music genres".

choices of "music genres":
'''
#prompt for params setting
PROMPT_PARAMS = '''
Please tune the parameters that represent characteristics of music you would recommend.
'''

# OUTPUT_PARSER_GENRES = None # CommaSeparatedListOutputParser() # define OutputParser
# PROMPT_GENRES_SELECTION = None # createPrompt() # create a prompt for genres selection

# RESPONSE_SCHEMAS_PARAMS = None # define response schemas
# OUTPUT_PARSER_PARAMS = None # StructuredOutputParser.from_response_schemas(RESPONSE_SCHEMAS_PARAMS) # define OutputParser
# PROMPT_PARAMS_SETTING = None # createPrompt() # create a prompt for params setting