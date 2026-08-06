import os

os.environ["ANONYMIZED_TELEMETRY"] = "False"


from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from rag.embeddings import get_embeddings


PDF_PATH = "rag/documents/who_guidelines.pdf"

VECTOR_PATH = "rag/vectorstore"



def ingest():

    print("Loading medical documents...")


    loader = PyPDFLoader(
        PDF_PATH
    )

    documents = loader.load()


    print(
        f"Loaded {len(documents)} pages"
    )


    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )


    chunks = splitter.split_documents(
        documents
    )


    print(
        f"Created {len(chunks)} chunks"
    )


    embeddings = get_embeddings()


    print(
        "Creating Chroma database..."
    )


    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_PATH,
        collection_name="medical_rag"
    )


    print(
        "Medical Vector Database Created Successfully"
    )



if __name__ == "__main__":
    ingest()