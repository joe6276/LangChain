import os 
from constants import Api_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory

import streamlit as st

os.environ["OPENAI_API_KEY"]=Api_key
# set up streamlit

st.title("LangChain Demo with OpenAI API")
#Memories

person_memory= ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory= ConversationBufferMemory(input_key='person', memory_key='chat_history')


# Get some Input

input_text =st.text_area("Search Your Clelebrity :")

first_input_prompt=PromptTemplate(
    input_variables=['name'],
    template= "Tell me about celebrity:  {name}"
)
#Use OpenAI LLMS
llm =OpenAI(temperature =0.8)
chain=LLMChain(llm=llm,prompt=first_input_prompt, verbose=True,output_key='person' ,memory=person_memory)


second_input_prompt=PromptTemplate(
    input_variables=['person'],
    template= "when was {person} Born"
)


chain2=LLMChain(llm=llm,prompt=second_input_prompt, verbose=True,output_key='dob',memory=dob_memory)

parent_chain =SequentialChain(chains=[chain,chain2],input_variables=['name'], output_variables =['person', 'dob'], verbose=True)

if input_text:
   st.write(parent_chain({'name':input_text}))
   
   with st.expander('Person Name'):
        st.info(person_memory.buffer)
   with st.expander("Dob"):
        st.info(dob_memory.buffer)