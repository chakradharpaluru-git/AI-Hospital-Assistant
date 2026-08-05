import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from insurance_rag.embeddings import get_embeddings


DOCUMENT_PATH = "insurance_rag/documents"
VECTOR_PATH = "insurance_rag/vectorstore"


def load_documents():

    documents = []

    for file in os.listdir(DOCUMENT_PATH):

        if file.endswith(".pdf"):

            loader = PyPDFLoader(
                os.path.join(DOCUMENT_PATH, file)
            )

            documents.extend(
                loader.load()
            )

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1000,

        chunk_overlap=200

    )

    return splitter.split_documents(
        documents
    )


def ingest():

    docs = load_documents()

    chunks = split_documents(
        docs
    )

    db = Chroma.from_documents(

        documents=chunks,

        embedding=get_embeddings(),

        persist_directory=VECTOR_PATH

    )

    print(f"Indexed {len(chunks)} chunks.")
    print("Insurance Vector Database Created Successfully.")


if __name__ == "__main__":
    ingest()