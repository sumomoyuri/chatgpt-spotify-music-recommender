import global_value as gv
from langchain.output_parsers import CommaSeparatedListOutputParser, StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate

##################################################################
### function to create prompts
##################################################################

def createPrompt(prompt: str, format_instructions: str):
  prompt = PromptTemplate(
    template=f'''
    {prompt}
    \n{{format_instructions}}\n{{question}}'
    ''',
    input_variables=['question'],
    partial_variables={'format_instructions': format_instructions}
  )
  return prompt


#######################
# for genres selection
#######################
def createPromptGENRES():
    # define OutputParser
    gv.OUTPUT_PARSER_GENRES = CommaSeparatedListOutputParser()
    # create a prompt for genres selection
    gv.PROMPT_GENRES_SELECTION = createPrompt(
    f'''
    {gv.PROMPT_COMMON}
    {gv.PROMPT_GENRES}
    {gv.GENRES_TEXT}
    ''',
    gv.OUTPUT_PARSER_GENRES.get_format_instructions() # create template instructions
    )


#######################
# for params setting
#######################

def createPromptPARAMS():
    # define response schemas
    gv.RESPONSE_SCHEMAS_PARAMS = [
    ResponseSchema(name="target_danceability", description="A range from 0.0 to 1.0 that indicates whether a music is suitable for dancing. 1.0 is the most danceable. Default is 0.5."),
    ResponseSchema(name="target_acousticness", description="A range from 0.0 to 1.0 that indicates whether a music is acoustic. 1.0 is the most acoustic. Default is 0.5."),
    ResponseSchema(name="target_energy", description="A range from 0.0 to 1.0 that indicates whether a music is energetic. 1.0 is the most energetic. Default is 0.5."),
    ResponseSchema(name="target_instrumentalness", description="A range from 0.0 to 1.0 that indicates whether a music is instrumentalness. 1.0 is the most instrumentalness. Default is 0.5."),
    ResponseSchema(name="target_valence", description="A range from 0.0 to 1.0 that indicates whether a music is positivity. 1.0 is the most positivity. Default is 0.5.")
    ]
    # define OutputParser
    gv.OUTPUT_PARSER_PARAMS = StructuredOutputParser.from_response_schemas(gv.RESPONSE_SCHEMAS_PARAMS)
    # create a prompt for params setting
    gv.PROMPT_PARAMS_SETTING = createPrompt(
    f'''
    {gv.PROMPT_COMMON}
    {gv.PROMPT_PARAMS}
    ''',
    gv.OUTPUT_PARSER_PARAMS.get_format_instructions() # create template instructions
    )