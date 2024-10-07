"""
Este módulo define las rutas y la lógica de manejo de solicitudes para la API RAG.

Implementa el endpoints de la API, gestionando las solicitudes entrantes, procesando
las consultas de los usuarios y coordinando la interacción entre los diferentes servicios
(embeddings, LLM, base de datos vectorial) para generar respuestas.

Rutas principales:
- /query_answer: Endpoint POST para procesar preguntas de usuarios y generar respuestas
                 utilizando el enfoque de Generación Aumentada por Recuperación (RAG).

Este módulo utiliza FastAPI para la definición de rutas y manejo de solicitudes, e integra
la funcionalidad de otros módulos del sistema para proporcionar respuestas coherentes y
contextualizadas a las consultas de los usuarios.
"""

from langid import classify
from fastapi import APIRouter, HTTPException
from app.models.models import Query
from app.services import get_llm_response, search_similar_documents
from app.utils.logger import get_logger

logger = get_logger()

router = APIRouter()

@router.post("/query_answer")
def query_answer(query: Query) -> dict:
    """
    Procesa una consulta del usuario y genera una respuesta utilizando RAG.

    Esta función maneja las solicitudes POST al endpoint /query_answer. Utiliza
    el enfoque de Generación Aumentada por Recuperación (RAG) para generar una
    respuesta contextualizada a la pregunta del usuario.

    Args:
        query (Query): Un objeto Query que contiene la pregunta del usuario.

    Returns:
        dict: Un diccionario con la respuesta generada.

    Raises:
        HTTPException: Si no se encuentra contexto relevante o ocurre un error inesperado.
    """
    try:
        context = search_similar_documents(query.question)
        if not context:
            raise HTTPException(status_code=404, detail="No relevant context found")
        logger.info("Context retrieved successfully")
        language, _ = classify(query.question)
        response = get_llm_response(query.question, context[0], language)
        logger.info("Response generated successfully.")
        return {"response": response}
    except HTTPException as http_ex:
        logger.error("HTTPException: %s", http_ex.detail)
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.") from e
