from .firebase import store
import time
from firebase_admin import firestore


async def get_story(story_id: str):
    """
    Fetches a story from the database given a story id
    """
    doc_ref = await store.collection("stories").document(story_id)
    return doc_ref


async def get_storyboard(story_id: str, board_id: str):
    """
    Fetches a storyboard from the database given a story id and board id
    """
    doc_ref = (
        store.collection("stories")
        .document(story_id)
        .collection("storyboard")
        .document(board_id)
    )
    return doc_ref


async def get_character(story_id: str, character_id: str):
    """
    Fetches a character from the database given a story id and board id
    """
    doc_ref = (
        store.collection("stories")
        .document(story_id)
        .collection("characters")
        .document(character_id)
    )
    return doc_ref


async def update_storyboard(story_id: str, board_id: str, extra_data: dict):
    """
    Updates a storyboard from the database given a story id and board id
    """
    doc_ref = (
        store.collection("stories")
        .document(story_id)
        .collection("storyboard")
        .document(board_id)
    )
    await doc_ref.update(extra_data)


async def update_character(story_id: str, character_id: str, extra_data: dict):
    """
    Updates a character from the database given a story id and character id
    """
    doc_ref = (
        store.collection("stories")
        .document(story_id)
        .collection("characters")
        .document(character_id)
    )
    await doc_ref.update(extra_data)


async def create_story(story_document: dict, board_document: dict):
    """

    Creates a story and its first storyboard and pushes it to firebaee
    """
    story_document["datetime"] = firestore.SERVER_TIMESTAMP
    story_document["finished"] = False
    _, ref = await store.collection("stories").add(story_document)
    story_board_ref = await create_story_board(ref.id, board_document)

    return ref.id, story_board_ref


async def get_story_narrative(story_id: str):
    """
    Fetches the story narrative from the database given a story id
    """

    storyboard_ref = (
        store.collection("stories")
        .document(story_id)
        .collection("storyboard")
        .order_by("datetime")
    )
    storyboard_ref_stream = storyboard_ref.stream()
    narrative = ""
    async for doc in storyboard_ref_stream:
        narrative += doc.get("narrative")
    return narrative


async def create_story_board(story_id: str, document: dict):
    """
    Pushes a story's storyboard to firebase
    """
    document["datetime"] = firestore.SERVER_TIMESTAMP

    _, ref = (
        await store.collection("stories")
        .document(story_id)
        .collection("storyboard")
        .add(document)
    )
    return ref.id


async def get_story_board_paths(story_id: str, board_id: str) -> list:
    paths = (
        await store.collection("stories")
        .document(story_id)
        .collection("storyboard")
        .document(board_id)
        .collection("paths")
        .get()
    )
    return list(map(lambda x: x.to_dict(), paths))


async def get_story_characters(story_id: str) -> list:
    """
    Get story characters from firebase by id
    """
    characters = (
        await store.collection("stories")
        .document(story_id)
        .collection("characters")
        .get()
    )
    return list(map(lambda x: x.to_dict(), characters))


async def create_story_characters(story_id: str, characters: list):
    """
    Creates story characters from firebase by id
    """
    for character in characters:
        await store.collection("stories").document(story_id).collection(
            "characters"
        ).add(character)


async def create_narrative_paths(story_id: str, board_id: str, paths: list):
    """
    Creates a narrative path given a story id, board id and a list of paths
    """
    for path in paths:
        await store.collection("stories").document(story_id).collection(
            "storyboard"
        ).document(board_id).collection("paths").add(path)

async def finish_story(story_id: str, document):
    """
    Sets a story to finished
    """
    document["date_finished"] = firestore.SERVER_TIMESTAMP
    await store.collection("stories").document(story_id).update(document)
    return True