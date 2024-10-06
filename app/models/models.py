"""
Este módulo define los modelos de datos utilizados en la aplicación.
Utiliza Pydantic para validar y estructurar los datos entrantes a través de la API.

Modelos:
- Query: Representa la estructura de la consulta que los usuarios envían a la API.
"""

from pydantic import BaseModel

class Query(BaseModel):
    """
    Modelo que representa la consulta del usuario a la API.
    """
    user_name: str
    question: str
