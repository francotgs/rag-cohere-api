"""
Este módulo proporciona servicios para interactuar con la base de datos vectorial ChromaDB.

Gestiona la adición de documentos (chunks de texto) a la base de datos vectorial y la búsqueda
de documentos similares basada en embeddings. Utiliza ChromaDB como motor de base de datos vectorial
para almacenar y recuperar eficientemente documentos y sus embeddings asociados.

Funciones principales:
- add_documents: Añade múltiples chunks de texto a la base de datos vectorial.
- search_similar_documents: Busca chunks de texto similares a una consulta dada (contexto).

Este módulo trabaja en conjunto con el servicio de embeddings para procesar y almacenar
documentos, y es crucial para la funcionalidad de recuperación de información del sistema RAG.
"""

import chromadb
from chromadb.config import Settings
from app.services import get_query_embeddings, get_document_embeddings
from app.utils.logger import get_logger

logger = get_logger()

client = chromadb.Client(Settings(persist_directory="./chroma_db", is_persistent=True))
collection = client.get_or_create_collection("documents")

def add_documents(documents):
    for i, doc in enumerate(documents):
        try:
            embedding = get_document_embeddings(doc)
            collection.add(
                embeddings=embedding,
                documents=[doc],
                metadatas=[{"source": f"doc_{i}"}],
                ids=[f"id_{i}"]
            )
        except Exception as e:
            logger.error("Error adding document %d to the vector database: %s", i, str(e), exc_info=True)
            raise

def search_similar_documents(query: str, n_results: int = 1):
    try:
        query_embedding = get_query_embeddings(query)
        results = collection.query(
            query_embeddings=query_embedding,
            n_results=n_results
        )
        return results['documents'][0] if results['documents'] else []
    except Exception as e:
        logger.error("Error searching for similar documents: %s", str(e), exc_info=True)
        raise
