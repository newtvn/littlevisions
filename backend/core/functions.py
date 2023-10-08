
from langchain.chains import LLMChain,SequentialChain
from langchain.llms import OpenAI
from .templates import *
from .openai_key import openai_key

from typing import List
llm = OpenAI()
def get_random_story_titles() -> List[dict]:
    chain = LLMChain(llm=llm,prompt=RANDOM_STORY_TITLES_PROMPT)
    res = chain.run(10)
    output = RANDOM_STORY_TITLES_PROMPT_PARSER.parse(res)
    return output.dict()


def get_narrative_paths(narrative) -> List[dict]:
    chain = LLMChain(llm=llm,prompt=PATH_CREATE_PROMPT) 
    res = chain.run(narrative)
    output = PATH_CREATE_PROMPT_PARSER.parse(res)
    return output.dict()

def extend_narrative_given_prompt(pre_narrative: str,prompt: str) -> dict:
    narrative_chain = LLMChain(llm=llm,prompt=EXTEND_STORY_WITH_CUSTOM_PROMPT,output_key="narrative")
    res = narrative_chain.run({"pre_narrative":pre_narrative,"prompt":prompt})
    output = STORY_CREATE_PROMPT_PARSER.parse(res)
    return output.dict()
    # paths_chain = LLMChain(llm=llm,prompt=PATH_CREATE_PROMPT,output_key="paths")
    # chain = SequentialChain(
    #     chains=[narrative_chain,paths_chain],
    #     input_variables= ['pre_narrative','prompt'],
    #     output_variables= ["narrative","paths"],
    # )
    # result = chain({"prompt":prompt,"pre_narrative":pre_narrative})
    # narrative = result["narrative"]
    # paths = result["paths"]

    # return {
    #     "paths": PATH_CREATE_PROMPT_PARSER.parse(paths).dict(),
    #     "narrative": STORY_CREATE_PROMPT_PARSER.parse(narrative).dict()
    # }
