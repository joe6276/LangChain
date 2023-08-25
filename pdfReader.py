

# from PyPDF2 import PdfReader
# # read the pdf
# from langchain.embeddings.openai import OpenAIEmbeddings
# #relatedness of a text string
# from langchain.text_splitter import CharacterTextSplitter
# #split it into special character i.e ne line
# from langchain.vectorstores import FAISS
# # store here

from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
import os
os.environ["OPENAI_API_KEY"]="YOUR_KEY"

from typing_extensions import Concatenate

pdfreader= PdfReader('cleanCode.pdf')


from typing_extensions import Concatenate
# read text from pdf
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



query = "what is clean code "
docs = document_search.similarity_search(query)
answer =chain.run(input_documents=docs, question=query)

print(answer)

