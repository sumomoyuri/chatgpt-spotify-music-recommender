import global_value as gv
from prompt import *
from langchain.output_parsers import RetryWithErrorOutputParser
from langchain.llms import OpenAI

##################################################
### function to check ChatGPT-recommended genres
##################################################
# extract genres that included in spotify music genres from ChatGPTs responses

def checkGenres(genres: list):
  response_genres_ok_list = [] # included in spotify music genres
  response_genres_ng_list = [] # not included in spotify music genres
  genres = [x.lower() for x in genres]
  # chaeck
  for word in genres:
    if word in gv.GENRES_LIST:
      response_genres_ok_list.append(word)
    else:
      response_genres_ng_list.append(word)
  # deduplication
  response_genres_ok_list = list(dict.fromkeys(response_genres_ok_list))
  return response_genres_ok_list, response_genres_ng_list

##################################################################
### functions to get ChatGPT's answer to input sentence
##################################################################

# Return recommended genres in ChatGPT's response
def getRecommendedGenres(input_question: str) -> list:
  # print("getting ChatGPT-recommended genres...")
  model = OpenAI(openai_api_key=gv.OPENAI_API_KEY)
  input = gv.PROMPT_GENRES_SELECTION.format_prompt(question=input_question)
  output = model(input.to_string())
  recommend_genres = gv.OUTPUT_PARSER_GENRES.parse(output)
  recommend_genres_OK, recommend_genres_NG = checkGenres(recommend_genres)
  print(f"ChatGPT's recommend_genres: {recommend_genres_OK}, (NG_genres{recommend_genres_NG})\n")
  return recommend_genres_OK

# Return recommended params in ChatGPT's response
def getRecommendedParams(input_question: str) -> dict:
  # print("getting ChatGPT-recommended params...")
  recommend_params = None
  model = OpenAI(openai_api_key=gv.OPENAI_API_KEY)
  input = gv.PROMPT_PARAMS_SETTING.format_prompt(question=input_question)
  output = model(input.to_string())
  try:
    recommend_params = gv.OUTPUT_PARSER_PARAMS.parse(output)
    print(f"ChatGPT's recommend_params: {recommend_params}\n")
  except:
    # fix response if conversion to JSON fails
    recommend_params = retryParser(output, input, model)
  return recommend_params

# fix response
def retryParser(inpur, output, model):
  # print("excuting retryParser...")
  retry_parser = RetryWithErrorOutputParser.from_llm(
    parser=gv.OUTPUT_PARSER_PARAMS,
    model=OpenAI(openai_api_key=gv.OPENAI_API_KEY)
  )
  result = retry_parser.parse_with_prompt(output, input)
  # print("Response is successfully fixed!\n")
  return result