"""
Este módulo proporciona funcionalidades para cargar y procesar documentos Word (.docx)
para su uso en el sistema RAG (Retrieval Augmented Generation).

El módulo contiene funciones para extraer texto de documentos Word, dividirlo en chunks
(fragmentos) manejables, y añadir estos chunks a la base de datos vectorial del sistema.

Funciones principales:
- extract_chunks: Extrae párrafos no vacíos de un documento Word.
- load_document: Carga un documento Word, lo procesa y añade sus contenidos a la base de
datos vectorial.

Este módulo es crucial para la fase de ingesta de datos del sistema RAG, permitiendo
la incorporación de información al corpus de conocimiento del sistema.

Nota: Este módulo requiere la biblioteca 'python-docx' para procesar archivos .docx.
"""

from typing import List
from docx import Document
from app.services import add_documents
from app.utils.logger import get_logger

logger = get_logger()

def extract_chunks(doc: Document) -> List[str]:
    """
    Extrae y procesa los párrafos de un documento Word.

    Esta función recorre todos los párrafos del documento, eliminando espacios en blanco
    innecesarios y filtrando párrafos vacíos.

    Args:
        doc (Document): Un objeto Document de python-docx representando el documento Word.

    Returns:
        list: Una lista de strings, donde cada string es un párrafo no vacío del documento.
    """
    paragraphs = []
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            paragraphs.append(paragraph.text.strip())
    return paragraphs

def load_document(file_path: str) -> None:
    """
    Carga un documento Word, lo procesa y añade su contenido a la base de datos vectorial.

    Esta función abre el documento especificado, extrae sus párrafos utilizando extract_chunks,
    y luego añade estos párrafos (chunks) a la base de datos vectorial utilizando la función
    add_documents del servicio de base de datos.

    Args:
        file_path (str): La ruta al archivo .docx que se va a cargar y procesar.

    Raises:
        FileNotFoundError: Si el archivo especificado no se encuentra en la ruta dada.
        ValueError: Si ocurre un error al procesar el documento (por ejemplo, si no es 
        un archivo .docx válido).
        Exception: Para cualquier otro error inesperado durante el proceso.
    """
    try:
        doc = Document(file_path)
        chunks = extract_chunks(doc)
        add_documents(chunks)
    except FileNotFoundError:
        logger.error("Error: The file %s was not found. Please check the path.", file_path)
    except ValueError as ve:
        logger.error("Error: %s. Please ensure that the file is a valid document.", ve)
    except Exception as e:
        logger.error("An unexpected error occurred: %s", e, exc_info=True)
