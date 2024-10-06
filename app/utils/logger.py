"""
Este módulo configura un logger para el proyecto RAG Challenge.
El logger guarda los registros en un archivo con rotación y también los muestra
en la consola.

El logger está configurado para:

- Crear un directorio para almacenar los archivos de log si no existe.
- Registrar mensajes de nivel DEBUG o superior en un archivo con rotación.
- Registrar mensajes de nivel INFO o superior en la consola.
- Usar un formato de log consistente que incluye la fecha, el nombre del logger,
  el nivel de gravedad y el mensaje.

Funciones:
- get_logger(): Devuelve una instancia del logger configurado para su uso en
  otras partes de la aplicación.

Ejemplo de uso:
    from app.logger import get_logger
    
    logger = get_logger()
    logger.info("Este es un mensaje informativo.")
    logger.error("Este es un mensaje de error.")
"""

import logging
import os
from logging.handlers import RotatingFileHandler

# Crea directorio de logs
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Configura el logger
logger = logging.getLogger("rag_challenge")
logger.setLevel(logging.DEBUG)

# Crea un manejador para archivo con rotación
file_handler = RotatingFileHandler(
    os.path.join(LOG_DIR, "rag_challenge.log"),
    maxBytes=10485760,  # 10MB
    backupCount=5
)
file_handler.setLevel(logging.DEBUG)

# Crea un manejador para consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Crea un formato para los logs
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Agrega los manejadores al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def get_logger() -> logging.Logger:
    """
    Devuelve la instancia del logger configurado.
    """
    return logger
