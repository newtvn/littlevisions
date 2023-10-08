from langchain.prompts import PromptTemplate
from .parsers import create_parser
from .models import StoryPart, PathList

STORY_CREATE_PROMPT = PromptTemplate(
    input_variables=["topic"],
    template="Write an intro to a child's story using the following prompt {topic}.{format_instructions}",
    partial_variables={
        "format_instructions": create_parser(StoryPart).get_format_instructions()
    },
)
PATH_CREATE_PROMPT = PromptTemplate(
    input_variables=["narrative"],
    template="Give me 4 possible paths in 20 words that extend the following narrative. Your response should be a valid extension on the narrative: {narrative}. {format_instructions}",
    partial_variables={
        "format_instructions": create_parser(PathList).get_format_instructions
    },
)
