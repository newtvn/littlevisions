import replicate
from urllib.request import urlretrieve
from .generators import Generator

class MusicGenerator(Generator):
    def __init__(self, prompt, duration=15) -> None:
        self.prompt = prompt
        self.duration = duration

    def generate(self) -> str:
        output = replicate.run(
            "meta/musicgen:7a76a8258b23fae65c5a22debb8841d1d7e816b75c2f24218cd2bd8573787906",
            input={
                "model_version": "melody",
                "prompt": self.prompt,
                "duration": self.duration,
            },
        )
    

