import os 
from constants import Api_key
from langchain.llms import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"]=Api_key
# set up streamlit

st.title("LangChain Demo with OpenAI API")

# Get some Input

input_text =st.text_area("Search What you want:")


#Use OpenAI LLMS
llm =OpenAI(temperature =0.8)

if input_text:
    st.write(llm(input_text))