from langchain_chroma import Chroma
from rag.embeddings import get_embeddings


VECTOR_PATH="rag/vectorstore"



def get_retriever():

    db = Chroma(

        persist_directory=VECTOR_PATH,

        embedding_function=get_embeddings()

    )


    retriever = db.as_retriever(

        search_kwargs={
            "k":5
        }

    )


    return retriever