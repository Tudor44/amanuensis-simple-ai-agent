
#                                                                                                                                                            #
# Tudor44                                                                                                                                                    #
# Amanuensis is a simple AI Agent for demostrating the possibility of Langchain of using Large Language Models with other API and custom components          #
#                                                                                                                                                            #   

from api import Api
import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

#external class for api integrations, 
api = Api()

#llm default OpenAPI
llm = api.llm

#wikipedia api
wiki = api.getWikipediaApi()

#streamlit view component
st.title('📖 Amanuensis Simple AI Agent 🤖')
prompt = st.text_input('Tell me a topic, I ll write for you') 

#1 prompt template
prompt_template = PromptTemplate(
    input_variables=['topic','wikipedia_research'], 
    template='write me a short article on {topic}, with the title {topic}, add this {wikipedia_research} and return me the output in markdown format'
)

#2 chain for run queries with apis
chain = LLMChain(llm=llm, prompt=prompt_template, verbose = True)

#3 prompt execution and view rendering
if prompt_template: 
    wiki_research = wiki.run(prompt) 
    result = chain.run(topic=prompt, wikipedia_research=wiki_research)

    with st.expander('Result'): 
         st.markdown(result) 
    st.balloons()