from fastapi import FastAPI
from core.functions import *
from core.narration_gen import NarrationGenerator
from models import *
from firebase import functions as firebase_functions
from fastapi.middleware.cors import CORSMiddleware
from core.models import PathPart
from firebase import upload

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
test_narrative = "Long ago there lived a very funny but cruel panda that was stuck in a zoo. He didnt like his habitat"


def generate_image_and_upload(image_prompt: str, filename: str):
    """
    Generates an image given a prompt and uploads
    """
    image_gen = ImageGenerator(image_prompt)
    image_string = image_gen.generate()
    output_path = f"./tmp/images/{filename}.png"
    image_gen.write_to_file(image_string, output_path)
    public_url = upload.uploadFile(output_path)

    return public_url


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
    story_doc = {"title": story.title}

    story_id, board_id = await firebase_functions.create_story(
        story_document=story_doc, board_document=story.model_dump()
    )

    return {"message": "Story created", "story_id": story_id, "board_id": board_id}


@app.get("/story/{story_id}/build/{board_id}/path/")
async def story_paths(story_id: str, board_id: str):
    """
    Fetches the story path using id and gets the possible paths
    """
    storyboard_paths = await firebase_functions.get_story_board_paths(
        story_id, board_id
    )
    if len(storyboard_paths) > 0:
        return {"paths": storyboard_paths}
    else:
        pre_narrative = await firebase_functions.get_story_narrative(story_id)

        narrative_paths = get_narrative_paths(pre_narrative)
        await firebase_functions.create_narrative_paths(
            story_id=story_id, board_id=board_id, paths=narrative_paths["paths"]
        )
        return narrative_paths


@app.post("/story/{story_id}/build/continue/")
async def build_story(story_id: str, prompt: CustomPrompt):
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
    }


@app.get("/story/{story_id}/characters/")
async def get_story_characters(story_id: str):
    """
    Gets the story characters from the narrative
    """
    story_characters = await firebase_functions.get_story_characters(story_id)
    if len(story_characters) > 0:
        return {"characters": story_characters}
    else:
        narrative = await firebase_functions.get_story_narrative(story_id)
        characters = get_characters_from_narrative(narrative)
        characters_json = characters.model_dump()
        await firebase_functions.create_story_characters(
            story_id, characters_json["characters"]
        )
        return characters_json


@app.get("/story/{story_id}/image/generate/{board_id}")
async def generate_board_image(story_id: str, board_id: str):
    """
    Generates an image and returns a url for the image
    """
    storyboard = await firebase_functions.get_storyboard(story_id, board_id)

    storyboard = await storyboard.get()
    storyboard = storyboard.to_dict()
    if "image_url" in storyboard:
        return {"image_url": storyboard["image_url"]}
    else:
        image_prompt = storyboard["image_description"]
        image_gen = ImageGenerator(image_prompt)
        image_string = image_gen.generate()
        output_path = f"./tmp/images/{board_id}.png"
        image_gen.write_to_file(image_string, output_path)
        public_url = upload.uploadFile(output_path)
        await firebase_functions.update_storyboard(
            story_id, board_id, {"image_url": public_url}
        )
        return {"image_url": public_url}


@app.get("/story/{story_id}/character/{character_id}/image/generate")
async def generate_character_image(story_id: str, character_id: str):
    """
    Generates a character image and uploads to firebase
    """
    character = await firebase_functions.get_character(story_id, character_id)
    character = await character.get()
    character = character.to_dict()
    if "image_url" in character:
        return {"image_url": character["image_url"]}
    else:
        image_prompt = character["image_description"]
        public_url = generate_image_and_upload(image_prompt, character_id)
        await firebase_functions.update_character(
            story_id, character_id, {"image_url": public_url}
        )
        return {"image_url": public_url}


@app.get("/story/{story_id}/narration/generate/{board_id}")
async def generate_board_narration(story_id: str, board_id: str):
    """
    Generates the text narration as a url for a given storyboard
    """
    storyboard = await firebase_functions.get_storyboard(story_id, board_id)

    storyboard = await storyboard.get()
    storyboard = storyboard.to_dict()
    if "narration_url" in storyboard:
        return {"narration_url": storyboard["narration_url"]}
    else:
        narrative = storyboard["narrative"]
        audio_gen = NarrationGenerator(text=narrative)
        audio_bytes = audio_gen.generate()
        output_path = f"./tmp/narrations/{board_id}.mp3"

        audio_gen.write_to_file(audio_bytes, output_path)
        public_url = upload.uploadFile(output_path)
        await firebase_functions.update_storyboard(
            story_id, board_id, {"narration_url": public_url}
        )
        return {"narration_url": public_url}
