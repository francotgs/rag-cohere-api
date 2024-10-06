"""
Este módulo proporciona servicios de generación de embeddings utilizando la API de Cohere.

Contiene funciones para generar embeddings tanto para consultas de búsqueda como para
documentos, utilizando el modelo 'embed-multilingual-v3.0' de Cohere. Estos embeddings
son fundamentales para la funcionalidad de búsqueda semántica y recuperación de información
en la aplicación RAG.

Funciones principales:
- get_query_embeddings: Genera embeddings para consultas de búsqueda.
- get_document_embeddings: Genera embeddings para documentos.

Este módulo requiere que se configure correctamente la API key de Cohere en las variables
de entorno o en un archivo .env.
"""

import os
import cohere
from dotenv import load_dotenv
from app.utils.logger import get_logger

load_dotenv()

logger = get_logger()
cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.ClientV2(cohere_api_key)

def get_query_embeddings(text: str):
    # Genera embeddings usando el método embed
    try:
        response = co.embed(
            texts=[text],
            model="embed-multilingual-v3.0",
            input_type="search_query",
            embedding_types=["float"]
        )
        # Devuelve los embeddings
        return response.embeddings.float
    except Exception as e:
        logger.error("Error generating embedding: %s", str(e), exc_info=True)
        raise

def get_document_embeddings(text: str):
    # Genera embeddings usando el método embed
    try:
        response = co.embed(
            texts=[text],
            model="embed-multilingual-v3.0",
            input_type="search_document",
            embedding_types=["float"]
        )
        # Devuelve los embeddings
        return response.embeddings.float
    except Exception as e:
        logger.error("Error generating embedding: %s", str(e), exc_info=True)
        raise
