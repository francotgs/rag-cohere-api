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
async def query_answer(query: Query):
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
