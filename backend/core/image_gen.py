from PIL import Image
import os
import replicate
from urllib.request import urlretrieve
from .generators import Generator

class ImageGenerator(Generator):
    def __init__(self, prompt: str, style: str | None = "anime"):
        self.prompt = prompt
        self.style = style
    
    def generate(self) -> str:
        output = replicate.run(
            "stability-ai/sdxl:c221b2b8ef527988fb59bf24a8b97c4561f1c671f73bd389f866bfb27c061316",
            input={"prompt": self.prompt},
        )        
        return output[0]

