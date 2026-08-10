import os
from functools import lru_cache

from langchain_chroma import Chroma

from insurance_rag.embeddings import get_embeddings


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

VECTOR_PATH = os.path.join(
    BASE_DIR,
    "insurance_rag",
    "vectorstore"
)


@lru_cache(maxsize=1)
def get_retriever():

    print("Loading insurance Chroma retriever...")

    embeddings = get_embeddings()

    db = Chroma(
        persist_directory=VECTOR_PATH,
        embedding_function=embeddings
    )

    retriever = db.as_retriever(
        search_kwargs={
            "k": 4
        }
    )

    print("Insurance Chroma retriever loaded.")

    return retriever