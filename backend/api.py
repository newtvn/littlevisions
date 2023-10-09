from fastapi import FastAPI
from core.functions import *
from models import *
from firebase import functions as firebase_functions

app = FastAPI()

test_narrative = "Long ago there lived a very funny but cruel panda that was stuck in a zoo. He didnt like his habitat"


@app.get("/")
async def index():
    return {
        "message": "Welcome to the LittleVisions API. "
        "I am just slowly building this lol"
    }


@app.get("/story/templates")
async def story_templates():
    try:
        return get_random_story_titles()
    except:
        return get_random_story_titles()


@app.post("/story/create/prompt")
async def story_create_from_prompt(prompt: CustomPrompt):
    """
    Creates a story from a prompt
    """
    story = create_story_from_prompt(prompt.prompt)
    story_doc = {"title": "story.title"}

    story_id, board_id = await firebase_functions.create_story(
        story_document=story_doc, board_document=story.model_dump()
    )

    return {"message": "Story created", "story_id": story_id, "board_id": board_id}


@app.get("/story/{story_id}/build/path/")
async def story_paths(story_id: str):
    """
    Fetches the story path using id and gets the possible paths
    """
    pre_narrative = await firebase_functions.get_story_narrative(story_id)

    return get_narrative_paths(pre_narrative)


@app.post("/story/{story_id}/build/custom/")
async def build_story_custom(story_id: str, prompt: CustomPrompt):
    """
    Builds a story if a custom path is provided
    """
    pre_narrative = await firebase_functions.get_story_narrative(story_id)

    extended_narrative_dict = extend_narrative_given_prompt(
        pre_narrative=pre_narrative, prompt=prompt.prompt
    )
    board_id = await firebase_functions.create_story_board(
        story_id, extended_narrative_dict
    )
    return {
        "message": "Board created",
        "board_id": board_id,
        "narrative": extended_narrative_dict,
    }


@app.get("story/{story_id}/image/generate/{board_id}")
async def generate_board_image(story_id: str, board_id: str):
    """
    Generates an image and returns a url for the image
    """
    pass


@app.get("story/{story_id}/narration/generate/{board_id}")
async def generate_board_narration(story_id: str, board_id: str):
    """
    Generates the text narration as a url for a given storyboard
    """
    pass
