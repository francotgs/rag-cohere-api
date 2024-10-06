"""
Este módulo gestiona la interacción con el modelo de lenguaje (LLM) de Cohere para generar
respuestas basadas en contexto.

Proporciona funcionalidad para construir prompts estructurados, enviar solicitudes al
modelo LLM de Cohere y procesar las respuestas generadas. El módulo está diseñado para
trabajar con el modelo 'command-r-plus-08-2024' de Cohere, generando respuestas que siguen
instrucciones específicas en cuanto a formato y contenido.

Funciones principales:
- get_llm_response: Genera una respuesta del LLM basada en un mensaje, contexto y 
lenguaje específicos.

Este módulo requiere una configuración adecuada de la API key de Cohere y está diseñado
para integrarse con otros componentes del sistema RAG.
"""

import os
import cohere
from dotenv import load_dotenv
from app.utils.logger import get_logger

load_dotenv()

logger = get_logger()
cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.ClientV2(cohere_api_key)

def get_llm_response(message: str, context: str, language: str):
    # Instrucciones para el modelo
    system_message = (
        "Responde a la siguiente pregunta siguiendo las instrucciones\n"
        "Instrucciones:\n"
        "1. Responde en una sola oración.\n"
        f"2. Responde en idioma ({language})\n"
        "3. Usa la tercera persona.\n"
        "4. Incluye 3 emojis que resuman el contenido de la respuesta.\n"
        "5. Asegúrate de que la respuesta sea consistente para la misma pregunta."
    )

    # Genera los mensajes para el chat
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": message},
    ]

    # Realiza la llamada al modelo de chat
    try:
        response = co.chat(
            model="command-r-plus-08-2024",
            messages=messages,
            documents=[context],
            temperature=0.0
        )
        # Extrae la respuesta del modelo
        return response.message.content[0].text
    except Exception as e:
        logger.error("Error generating response: %s", str(e), exc_info=True)
        raise
