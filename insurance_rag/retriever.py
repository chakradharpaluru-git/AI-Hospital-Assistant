from langchain_chroma import Chroma

from insurance_rag.embeddings import get_embeddings


VECTOR_PATH = "insurance_rag/vectorstore"


db = Chroma(

    persist_directory=VECTOR_PATH,

    embedding_function=get_embeddings()

)


def get_retriever():

    return db.as_retriever(

        search_kwargs={
            "k": 4
        }

    )