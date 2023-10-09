from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from .templates import *
from .openai_key import openai_key
from .image_gen import ImageGenerator
from typing import List

llm = OpenAI(temperature=0.4)


def create_story_from_prompt(prompt: str) -> StoryPart:
    """
    Generates a story introduction from a prompt
    """
    chain = LLMChain(llm=llm, prompt=STORY_CREATE_PROMPT)
    res = chain.run(prompt)
    output = STORY_CREATE_PROMPT_PARSER.parse(res)
    return output


def get_random_story_titles() -> List[dict]:
    """
    Generates 10 random story titles
    """
    chain = LLMChain(llm=llm, prompt=RANDOM_STORY_TITLES_PROMPT)
    res = chain.run(10)
    output = RANDOM_STORY_TITLES_PROMPT_PARSER.parse(res)
    return output.dict()


def get_narrative_paths(narrative) -> List[dict]:
    """
    Get the next possible paths from a narrative
    """
    chain = LLMChain(llm=llm, prompt=PATH_CREATE_PROMPT)
    res = chain.run(narrative)
    output = PATH_CREATE_PROMPT_PARSER.parse(res)
    return output.dict()


def extend_narrative_given_prompt(pre_narrative: str, prompt: str) -> dict:
    """
    Extends a narrative from the provided prompt
    """

    narrative_chain = LLMChain(
        llm=llm, prompt=EXTEND_STORY_WITH_CUSTOM_PROMPT, output_key="narrative"
    )
    res = narrative_chain.run({"pre_narrative": pre_narrative, "prompt": prompt})
    output = STORY_CREATE_PROMPT_PARSER.parse(res)
    return output.dict()


def get_characters_from_narrative(narrative: str) -> CharacterList:
    """
    Gets the characters from a narrative
    """
    chain = LLMChain(llm=llm, prompt=CHARACTER_LIST_PROMPT)
    res = chain.run(narrative)
    output = CHARACTER_LIST_PROMPT_PARSER.parse(res)
    return output


def generate_image_from_prompt(prompt: str) -> str:
    """
    Calls an image generation api and returns a base64 image string
    """
    image_gen = ImageGenerator(prompt=prompt)
    return image_gen.generate()
