import os
import cohere
from dotenv import load_dotenv

load_dotenv()
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
    response = co.chat(
        model="command-r-plus-08-2024",
        messages=messages,
        documents=[context],
        temperature=0.0
    )

    print(response.message.citations)

    # Extrae la respuesta del modelo
    return response.message.content[0].text
