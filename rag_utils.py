# rag_utils.py
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def create_vectorstore_from_pdf(pdf_path: str, persist_dir: str = "./rag_db"):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(chunks, embeddings, persist_directory=persist_dir)
    return vectordb
