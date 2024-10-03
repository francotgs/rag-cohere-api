import os
from langchain.embeddings import CohereEmbeddings
from dotenv import load_dotenv

load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")
embeddings = CohereEmbeddings(cohere_api_key=cohere_api_key)

def get_embeddings(text: str):
    return embeddings.embed_query(text)
