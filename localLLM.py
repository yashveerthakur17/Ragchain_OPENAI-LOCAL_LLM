from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

#setting the environment variables without hardcoding
#os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]=os.getenv("LANGSMITH_TRACING")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGSMITH_API_KEY")

#promt template
prompt = ChatPromptTemplate.from_template(
    "System: You are an assistant, please respond to the questions.\nUser: Question: {question}"
)

st.title('LangchainProject1 with local llama 3.2:1b')
input_text=st.text_area('Search something')

#openai llms
llm=Ollama(model='llama3.2:1b')
output_parser=StrOutputParser()

#chain formation
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question', input_text}))