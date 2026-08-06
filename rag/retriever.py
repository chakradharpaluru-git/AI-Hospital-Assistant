from langchain_chroma import Chroma

from rag.embeddings import get_embeddings


VECTOR_PATH = "rag/vectorstore"


def get_retriever():

    embeddings = get_embeddings()


    db = Chroma(
        persist_directory=VECTOR_PATH,
        embedding_function=embeddings,
        collection_name="medical_rag"
    )


    return db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 5,
            "score_threshold": 0.2
        }
    )