from pydantic import BaseModel

class CustomPrompt(BaseModel):
    prompt:str

class Character(BaseModel):
    name: str
    personality: str
    actions: str