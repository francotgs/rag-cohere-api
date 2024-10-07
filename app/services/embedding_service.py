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
from typing import List
import cohere
from dotenv import load_dotenv
from app.utils.logger import get_logger

load_dotenv()

logger = get_logger()
cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.ClientV2(cohere_api_key)

def get_query_embeddings(text: str) -> List[List[float]]:
    """
    Genera embeddings para una consulta de búsqueda.

    Esta función utiliza el modelo 'embed-multilingual-v3.0' de Cohere para generar
    embeddings vectoriales de una consulta dada. Los embeddings son útiles para
    realizar búsquedas semánticas.

    Args:
        text (str): El texto de la consulta para el cual se generarán los embeddings.

    Returns:
        list: Una lista de listas de valores float que representa el embedding de la consulta.

    Raises:
        Exception: Si ocurre un error durante la generación del embedding.
    """
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

def get_document_embeddings(text: str) -> List[List[float]]:
    """
    Genera embeddings para un documento.

    Esta función utiliza el modelo 'embed-multilingual-v3.0' de Cohere para generar
    embeddings vectoriales de un documento dado. Los embeddings son útiles para
    indexar y buscar documentos de manera semántica.

    Args:
        text (str): El texto del documento para el cual se generarán los embeddings.

    Returns:
        list: Una lista de listas de valores float que representa el embedding del documento.

    Raises:
        Exception: Si ocurre un error durante la generación del embedding.
    """
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
