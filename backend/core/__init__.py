import os
from .openai_key import openai_key,stabilityai_key
os.environ['OPENAI_API_KEY'] = openai_key
os.environ['STABILITYAI_API_KEY'] = stabilityai_key