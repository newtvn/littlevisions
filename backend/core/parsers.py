from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel


def create_parser(model: BaseModel):
    parser = PydanticOutputParser(model)
    return parser
