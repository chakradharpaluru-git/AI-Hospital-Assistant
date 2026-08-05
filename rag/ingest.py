import os

from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma

from rag.embeddings import get_embeddings


DOCUMENT_PATH = "rag/documents"

VECTOR_PATH = "rag/vectorstore"



def create_vector_database():

    documents=[]


    for file in os.listdir(DOCUMENT_PATH):

        if file.endswith(".pdf"):

            loader = PyPDFLoader(
                f"{DOCUMENT_PATH}/{file}"
            )

            docs = loader.load()

            documents.extend(docs)



    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1000,

        chunk_overlap=200

    )


    chunks = splitter.split_documents(
        documents
    )


    embeddings = get_embeddings()


    db = Chroma.from_documents(

        chunks,

        embeddings,

        persist_directory=VECTOR_PATH

    )


    db.persist()


    print("Medical Vector Database Created")



if __name__=="__main__":

    create_vector_database()