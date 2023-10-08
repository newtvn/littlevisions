from fastapi import FastAPI
from core.functions import *
from models import *

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


@app.get("/story/{story_id}/build/path/")
async def story_paths(story_id: str):
    """
    Fetches the story path using id and gets the possible paths
    """
    return get_narrative_paths(test_narrative)


@app.post("/story/{story_id}/build/custom/")
async def build_story_custom(story_id: str, prompt: CustomPrompt):
    """
    Builds a story if a custom path is provided
    """
    return extend_narrative_given_prompt(pre_narrative=test_narrative,prompt=prompt.prompt)
