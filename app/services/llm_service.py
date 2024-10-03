import os
import cohere
from dotenv import load_dotenv

load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(cohere_api_key)

def get_llm_response(question: str, context: str, language: str):
    prompt = f"""
    Responde a la siguiente pregunta basándote en el contexto proporcionado.
    Pregunta: {question}
    Contexto: {context}
    Instrucciones:
    1. Responde en una sola oración.
    2. Responde en el mismo idioma que la pregunta ({language}).
    3. Usa la tercera persona.
    4. Incluye emojis que resuman el contenido de la respuesta.
    5. Asegúrate de que la respuesta sea consistente para la misma pregunta.
    Respuesta:"""

    response = co.generate(
        model='command-r-plus',
        prompt=prompt,
        max_tokens=100,
        temperature=0.1,
        k=0
    )
    return response.generations[0].text.strip()
