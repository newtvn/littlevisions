from langchain.prompts import PromptTemplate
from .parsers import create_parser
from .models import Story, StoryPart, PathList, CharacterList, StoryList


STORY_CREATE_PROMPT_PARSER = create_parser(StoryPart)
STORY_CREATE_PROMPT = PromptTemplate(
    input_variables=["topic"],
    template="Write an introduction to a child's story using the following prompt as a guide {topic}.{format_instructions}",
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

CHARACTER_LIST_PROMPT_PARSER = create_parser(CharacterList)
CHARACTER_LIST_PROMPT = PromptTemplate(
    input_variables=["narrative"],
    template="Provide the characters that exist in the following narrative: {narrative}. {format_instructions}",
    partial_variables={
        "format_instructions": CHARACTER_LIST_PROMPT_PARSER.get_format_instructions()
    },
)

CHARACTER_CREATE_PROMPT = PromptTemplate(
    input_variables=["name", "actions", "personality", "narrative"],
    template="Extend this narrative relevantly by creating a character with the following description: name: {name}, descriptions: {personality}, actions: {actions} Return only the extended part.{narrative} In 30 words max. {format_instructions}",
    partial_variables={
        "format_instructions": STORY_CREATE_PROMPT_PARSER.get_format_instructions()
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
    input_variables=["pre_narrative", "prompt"],
    template="Extend this narrative {pre_narrative} using the following prompt {prompt}. Return only the extended part. {format_instructions}",
    partial_variables={
        "format_instructions": STORY_CREATE_PROMPT_PARSER.get_format_instructions()
    },
)

STORY_CONCLUSION_PROMPT = PromptTemplate(
    input_variables=['narrative'],
    template="Finish this story with a relevant conclusion. Return only the concluded part{narrative}. {format_instructions}",
    partial_variables= {
        "format_instructions": STORY_CREATE_PROMPT_PARSER.get_format_instructions()
    }
)

STORY_PARSER = create_parser(Story)
FINISH_STORY_PROMPT = PromptTemplate(
    input_variables= ["narrative"],
    template = "Given the following narrative {narrative}, generate the following: {format_instructions}",
    partial_variables= {
        "format_instructions": STORY_PARSER.get_format_instructions()
    }
)