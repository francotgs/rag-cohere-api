"""
Este módulo define los modelos de datos utilizados en la aplicación.
Utiliza Pydantic para validar y estructurar los datos entrantes a través de la API.

Modelos:
- Query: Representa la estructura de la consulta que los usuarios envían a la API.
"""

from pydantic import BaseModel

class Query(BaseModel):
    """
    Modelo de datos para la consulta del usuario.

    Este modelo valida y estructura la información de la consulta que un usuario 
    envía a la API, la cual contiene el nombre del usuario y su pregunta.

    Attributes:
        user_name (str): El nombre del usuario que hace la pregunta.
        question (str): La pregunta que el usuario desea realizar.
    """
    user_name: str
    question: str
