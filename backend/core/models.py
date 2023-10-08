from pydantic import BaseModel, Field
from typing import List


class StoryPart(BaseModel):
    narrative: str = Field(description="30 words max text on a narrative")
    title: str = Field(description="Small title based off the narrative")
    image_description: str = Field(
        description="Image generation prompt based of keywords on the narrative"
    )


class PathPart(BaseModel):
    narrative: str = Field(
        description="A different path narrative for the stort to take"
    )
    title: str = Field(description="Small title, 3 words max, based off the narrative")
    image_description: str = Field(
        description="Image generation prompt based of keywords on the narrative"
    )
    mood: str = Field(description="The general mood of the narrative")


class PathList(BaseModel):
    paths: List[PathPart]
