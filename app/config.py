"""
Este módulo contiene la configuración principal de la aplicación FastAPI.

Define la creación de la instancia de la aplicación e incluye las rutas de la API.
Además, se encarga de la carga inicial de los documentos al iniciar la aplicación,
los cuales se utilizarán para generar embeddings y realizar búsquedas en la base
de datos vectorial.

Functions:
    create_app: Crea y configura la aplicación FastAPI, incluyendo las rutas y 
    realizando la carga de documentos.
"""

from fastapi import FastAPI
from app.api.routes import router
from app.utils.load_documents import load_document
from app.utils.logger import get_logger

logger = get_logger()

def create_app() -> FastAPI:
    """
    Crea y configura una instancia de la aplicación FastAPI.

    Esta función inicializa la aplicación, incluyendo las rutas de la API
    y asegurando la carga de los documentos necesarios para su posterior 
    procesamiento. La función `load_document` se llama durante la inicialización
    para preparar los documentos que serán utilizados en el modelo de embeddings.

    Returns:
        FastAPI: Instancia de la aplicación FastAPI configurada con las rutas 
        y los documentos cargados.
    """
    app = FastAPI()
    app.include_router(router) # Inclusión de las rutas del módulo de enrutamiento
    load_document("./data/documento.docx")  # Carga inicial del documento
    logger.info("Application loaded successfully.")
    return app
