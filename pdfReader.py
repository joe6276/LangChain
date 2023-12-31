
import os
os.environ["OPENAI_API_KEY"]="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"

from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS


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
print(texts)
embeddings = OpenAIEmbeddings()
document_search = FAISS.from_texts(texts, embeddings)

print(document_search)


from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

chain = load_qa_chain(OpenAI(), chain_type="stuff",verbose=True)



query = "what is a laptop "
docs = document_search.similarity_search(query)
answer =chain.run(input_documents=docs, question=query)

print(answer)

