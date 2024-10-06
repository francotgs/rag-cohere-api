"""
Este módulo inicializa y ejecuta la aplicación FastAPI.
Contiene una ruta de prueba para verificar el estado del servicio.
"""

from app.config import create_app

app = create_app()

@app.get("/health")
def health_check():
    return {"status": "ok"}
