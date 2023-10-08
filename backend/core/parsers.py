from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel


def create_parser(model: BaseModel):
    parser = PydanticOutputParser(pydantic_object= model)
    return parser
