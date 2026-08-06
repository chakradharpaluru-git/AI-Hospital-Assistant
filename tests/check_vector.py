from rag.retriever import get_retriever


retriever = get_retriever()


docs = retriever.invoke(
    "diabetes symptoms"
)


print("Documents found:", len(docs))


for doc in docs:
    print("\n---")
    print(doc.page_content[:500])
    print(doc.metadata)