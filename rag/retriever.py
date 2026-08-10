from functools import lru_cache

from langchain_chroma import Chroma

from rag.embeddings import get_embeddings


VECTOR_PATH = "rag/vectorstore"


@lru_cache(maxsize=1)
def get_retriever():

    print("Loading Chroma medical retriever...")

    embeddings = get_embeddings()

    db = Chroma(
        persist_directory=VECTOR_PATH,
        embedding_function=embeddings,
        collection_name="medical_rag"
    )

    retriever = db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 5,
            "score_threshold": 0.2
        }
    )

    print("Chroma medical retriever loaded.")

    return retriever