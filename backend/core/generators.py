from abc import ABC, abstractmethod
import os
from urllib.request import urlretrieve


class Generator(ABC):
    @abstractmethod
    def generate(self):
        pass

    def url_to_file(self, url: str, filepath: str):
        urlretrieve(url, filepath)

    def write_to_file(self, url: str, filepath: str):
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.url_to_file(url, filepath)
