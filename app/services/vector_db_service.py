import chromadb
from chromadb.config import Settings
from app.services.embedding_service import get_embeddings

client = chromadb.Client(Settings(persist_directory="./chroma_db", is_persistent=True))
"""print("ChromaDB client initialized with settings:", client.get_settings())"""
collection = client.get_or_create_collection("documents")
print("Collection created or retrieved.")
"""client.delete_collection("documents")"""

def add_documents(documents):
    for i, doc in enumerate(documents):
        embedding = get_embeddings(doc)
        collection.add(
            embeddings=[embedding],
            documents=[doc],
            metadatas=[{"source": f"doc_{i}"}],
            ids=[f"id_{i}"]
        )
        """all_docs = collection.get()
        for doc in all_docs['documents']:
            print(doc)
        collections = client.list_collections()
        print(collections)"""

def search_similar_documents(query: str, n_results: int = 1):
    query_embedding = get_embeddings(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    print(results)
    return results['documents'][0] if results['documents'] else []
