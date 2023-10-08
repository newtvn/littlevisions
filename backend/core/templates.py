from langchain.prompts import PromptTemplate
from .parsers import create_parser
from .models import StoryPart, PathList, CharacterList, StoryList


STORY_CREATE_PROMPT_PARSER = create_parser(StoryPart)
STORY_CREATE_PROMPT = PromptTemplate(
    input_variables=["topic"],
    template="Write an intro to a child's story using the following prompt {topic}.{format_instructions}",
    partial_variables={
        "format_instructions": STORY_CREATE_PROMPT_PARSER.get_format_instructions()
    },
)

PATH_CREATE_PROMPT_PARSER = create_parser(PathList)
PATH_CREATE_PROMPT = PromptTemplate(
    input_variables=["narrative"],
    template="Give me 4 possible paths in 20 words that extend the following narrative. Your response should be a valid extension on the narrative: {narrative}. {format_instructions}",
    partial_variables={
        "format_instructions": PATH_CREATE_PROMPT_PARSER.get_format_instructions()
    },
)


CHARACTER_LIST_PROMPT = PromptTemplate(
    input_variables=["narrative"],
    template="Provide the characters that exist in the following narrative: {narrative}. {format_instructions}",
    partial_variables={
        "format_instructions": create_parser(CharacterList).get_format_instructions()
    },
)

RANDOM_STORY_TITLES_PROMPT_PARSER = create_parser(StoryList)

RANDOM_STORY_TITLES_PROMPT = PromptTemplate(
    input_variables=["count"],
    template="Give me about {count} random story titles for kids. {format_instructions}",
    partial_variables={
        "format_instructions": RANDOM_STORY_TITLES_PROMPT_PARSER.get_format_instructions()
    },
)

EXTEND_STORY_WITH_CUSTOM_PROMPT = PromptTemplate(
    input_variables= ["pre_narrative","prompt"],
    template= "Extend this narrative {pre_narrative} using the following prompt {prompt}. Return only the extended part. {format_instructions}",
    partial_variables= {
        "format_instructions": STORY_CREATE_PROMPT_PARSER.get_format_instructions()
    }
)