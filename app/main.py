"""
Este es el módulo principal de la aplicación.

Este módulo inicializa y ejecuta la aplicación FastAPI. Contiene una ruta
de prueba para verificar el estado del servicio.
"""

from app.config import create_app

app = create_app()

@app.get("/health")
def health_check() -> dict:
    """
    Ruta de verificación del estado de la API.

    Returns:
        dict: Un diccionario que indica que la API está operativa.
    """
    return {"status": "ok"}
