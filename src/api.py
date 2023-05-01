
from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.utilities import WikipediaAPIWrapper 

class Api:
    
    def __init__(self):
        load_dotenv(find_dotenv())
        self.llm = OpenAI(temperature=0.9, model_name="text-ada-001")
        self.tools = []
        self.tools.append(WikipediaAPIWrapper())

    def getWikipediaApi(self):
        return self.tools[0]