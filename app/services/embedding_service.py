import os
import cohere
from dotenv import load_dotenv

load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.ClientV2(cohere_api_key)

def get_query_embeddings(text: str):
    # Genera embeddings usando el método embed
    response = co.embed(
        texts=[text],
        model="embed-multilingual-v3.0",
        input_type="search_query",
        embedding_types=["float"]
    )
    # Devuelve los embeddings
    return response.embeddings.float

def get_document_embeddings(text: str):
    # Genera embeddings usando el método embed
    response = co.embed(
        texts=[text],
        model="embed-multilingual-v3.0",
        input_type="search_document",
        embedding_types=["float"]
    )
    # Devuelve los embeddings
    return response.embeddings.float
