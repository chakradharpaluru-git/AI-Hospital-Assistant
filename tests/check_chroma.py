from langchain_chroma import Chroma

from rag.embeddings import get_embeddings


db = Chroma(
    persist_directory="rag/vectorstore",
    embedding_function=get_embeddings(),
    collection_name="medical_rag"
)


data = db.get()


print(
    "Total stored documents:",
    len(data["documents"])
)


if len(data["documents"]) > 0:

    print("\nFirst document:")
    print(
        data["documents"][0][:500]
    )


    print("\nMetadata:")
    print(
        data["metadatas"][0]
    )