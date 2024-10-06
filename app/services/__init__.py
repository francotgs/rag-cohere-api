"""
Este módulo sirve como punto de entrada para los servicios relacionados 
con la generación de respuestas de LLM y la gestión de embeddings y 
documentos en la base de datos vectorial.

Funciones disponibles:
- get_llm_response: Obtiene una respuesta del modelo de lenguaje (LLM) para una consulta dada.
- get_query_embeddings: Genera embeddings a partir de una consulta de usuario.
- get_document_embeddings: Genera embeddings a partir de un documento cargado.
- add_documents: Agrega documentos a la base de datos vectorial.
- search_similar_documents: Busca documentos similares en la base de datos vectorial.
"""

from .llm_service import get_llm_response
from .embedding_service import get_query_embeddings, get_document_embeddings
from .vector_db_service import add_documents, search_similar_documents
