from pydantic import BaseModel, Field
from typing import List


class Story(BaseModel):
    title :str = Field(description="Story title")
    mood :str = Field(description="Mood of the story")

class StoryList(BaseModel):
    stories: List[Story]

class StoryPart(BaseModel):
    narrative: str = Field(description="30 words max narrative text, extending or starting a story. 30 words maximum")
    title: str = Field(description="Small title based off the narrative")
    image_description: str = Field(
        description="Image generation prompt based of keywords on the narrative"
    )
    music_description:str = Field(description="Description for a background music generation prompt, include instruments, eras or whatever's relevant")


class PathPart(BaseModel):
    narrative: str = Field(
        description="A different path narrative for the stort to take"
    )
    title: str = Field(description="Small title, 3 words max, based off the narrative")



class PathList(BaseModel):
    paths: List[PathPart] = Field(description="Ensure the list is valid JSON. Emphasis on valid JSON")


class Character(BaseModel):
    name: str = Field(description="Character Name. 2 words Max")
    description: str = Field(
        description="Character Description personality wise. 10 words max"
    )
    image_description: str = Field(
        description="Image generation prompt for the character. Preferrably portrait in a solid background"
    )


class CharacterList(BaseModel):
    characters: List[Character]
