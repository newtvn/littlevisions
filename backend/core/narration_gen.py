import requests
import os
import io


class NarrationGenerator:
    def __init__(self, text, voice_id="JByRp0YGeGLj8wdR9Am5") -> None:
        self.text = text
        self.voice_id = voice_id
        self.url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    def get_headers(self):
        return {
            "accept": "audio/mpeg",
            "content-type": "application/json",
            "xi-api-key": os.environ.get("ELEVEN_LABS_API_KEY"),
        }

    def get_body(self):
        return {"text": self.text}

    def generate(self):
        response = requests.post(
            self.url,
            headers=self.get_headers(),
            json=self.get_body(),
        )
        if response.status_code != 200:
            raise Exception("Non-200 response: " + str(response.text))
        else:
            data = response.content

            return data

    def write_to_file(self, bytes: bytes, filepath: str):
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(filepath, "wb") as fh:
            fh.write(bytes)
