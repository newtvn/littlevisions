from PIL import Image
import os
import replicate
from urllib.request import urlretrieve


class ImageGenerator:
    def __init__(self, prompt: str, style: str | None = "anime"):
        self.prompt = prompt
        self.style = style

    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

    def get_headers(self):
        api_key = os.environ.get("STABILITYAI_API_KEY")
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }

        return headers

    def get_body(self):
        return {
            "steps": 40,
            "width": 1024,
            "height": 1024,
            "seed": 0,
            "cfg_scale": 5,
            "style_preset": self.style,
            "samples": 1,
            "text_prompts": [
                {"text": self.prompt, "weight": 1},
                {"text": "blurry, bad", "weight": -1},
            ],
        }

    def generate(self) -> str:
        output = replicate.run(
            "stability-ai/sdxl:c221b2b8ef527988fb59bf24a8b97c4561f1c671f73bd389f866bfb27c061316",
            input={"prompt": self.prompt},
        )        
        return output[0]
    
    def url_to_image(self, image_url:str,filepath:str):
        urlretrieve(image_url,filepath)



    def write_to_file(self, image_url: str, filepath: str):
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.url_to_image(image_url,filepath)
        
