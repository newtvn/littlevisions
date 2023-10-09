from .firebase import store
import time
from firebase_admin import firestore


async def get_story(story_id: str):
    """
    Fetches a story from the database given a story id
    """
    doc_ref = store.collection("stories").document(story_id)
    return doc_ref


async def create_story(story_document: dict, board_document: dict):
    """

    Creates a story and its first storyboard and pushes it to firebaee
    """
    story_document["datetime"] = firestore.SERVER_TIMESTAMP
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

    _,ref = await store.collection("stories").document(story_id).collection("storyboard").add(document)
    return ref.id
