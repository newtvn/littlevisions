import base64
import requests
import os


class ImageGenerator:
    def __init__(self, prompt: str, style: str | None = None):
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
        response = requests.post(
            self.url,
            headers=self.get_headers(),
            json=self.get_body(),
        )
        if response.status_code != 200:
            raise Exception("Non-200 response: " + str(response.text))
        else:
            data = response.json()
            image = data["artifacts"][0]
            return image["base64"]

    def write_to_file(self,base64String:str,filepath:str):
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(filepath, "wb") as fh:
            fh.write(base64.b64decode(base64String))