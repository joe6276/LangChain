from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
import  streamlit as st

pdfreader= PdfReader('CleanCode.pdf')

raw_text = ''
for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        raw_text += content

        text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 800,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)
# print(texts)
embeddings = OpenAIEmbeddings()
document_search = FAISS.from_texts(texts, embeddings)


from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

chain = load_qa_chain(OpenAI(), chain_type="stuff")
def get_Input(input):
    input_text =st.text_input('You', key=input)
    return input_text



def getResponse(query):
    docs = document_search.similarity_search(query)
    answer =chain.run(input_documents=docs, question=query)
    return answer
query = get_Input("input")
response= getResponse(query)
submit = st.button("Generate")

if submit:
    st.subheader("Jonathan AI")
    st.write(response)



