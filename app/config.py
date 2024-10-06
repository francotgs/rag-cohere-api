"""
Este módulo contiene la configuración principal de la aplicación FastAPI.
Incluye la definición y configuración de las rutas y servicios adicionales.
"""

from fastapi import FastAPI
from app.api.routes import router
from app.utils.load_documents import load_document

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router) # Inclusión de las rutas del módulo de enrutamiento
    load_document("./data/documento.docx") # Carga inicial de documentos
    return app
