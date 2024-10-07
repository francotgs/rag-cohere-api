# RAG API

Esta es una API que implementa una solución de **Retrieval Augmented Generation (RAG)** utilizando **FastAPI**, **LangChain** y **ChromaDB**.

La aplicación se puede ejecutar tanto localmente como dentro de un contenedor Docker.

- [Requisitos](#requisitos)
- [Instalación y ejecución en local](#instalación-y-ejecución-en-local)
- [Ejecución en docker](#ejecución-en-docker)
- [Uso de la API](#uso-de-la-api)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Desarrollo](#desarrollo)
- [Colección de Postman](#colección-de-postman)
- [Licencia](#licencia)

## Requisitos

- Python 3.8.8 o superior
- Docker (si se desea ejecutar en un contenedor)

## Instalación y ejecución en local

1. **Clonar el repositorio** (si aún no lo has hecho):

   ```bash
   git clone https://github.com/francotgs/rag-cohere-api && cd rag-cohere-api
   ```

2. **Crear y activar un entorno virtual**

    ```bash
    python3 -m venv venv && source venv/bin/activate
    ```

3. **Instalar las dependencias**

    ```bash
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    ```

4. **Introducir la API Key de Cohere como variable de entorno**

    Asegúrate de reemplazar <TU_API_KEY> con tu clave:

    ```bash
    export COHERE_API_KEY=<TU_API_KEY>
    ```

    O crear un archivo .env en la raíz de tu proyecto y agregar la variable en el mismo:
    
    ```bash
    COHERE_API_KEY=<TU_API_KEY>
    ```

5. **Ejecutar la aplicación**

    ```bash
    uvicorn app.main:app --reload
    ```

6. **Acceder a la API**

    Abre tu navegador y ve a http://localhost:8000/health para verificar que la API está funcionando.

    Utiliza la ruta http://localhost:8000/docs para poder realizar consultas a la api.
    
## Ejecución en docker

1. **Construir la imagen Docker**

    Construir la imagen puede demorar unos minutos.

    ```bash
    docker build -t rag-api .
    ```

2. **Ejecutar el contenedor**

    Asegúrate de reemplazar <TU_API_KEY> con tu clave de API:

    ```bash
    docker run -d --name rag-container -e COHERE_API_KEY=<TU_API_KEY> -p 8000:8000 rag-api && docker logs -f rag-container
    ```

    Esperar unos segundos para que la aplicación arranque completamente.

3. **Acceder a la API**

    Abre tu navegador y ve a http://localhost:8000/health para verificar que la API está funcionando.

    Utiliza la ruta http://localhost:8000/docs para poder realizar consultas a la api.

## Uso de la API

Para hacer una consulta, envía una solicitud POST a `/query_answer` con el siguiente formato:

```json
{
  "user_name": "John Doe",
  "question": "¿Cómo funciona el sistema RAG?"
}
```

La API devolverá una respuesta.

## Estructura del Proyecto

```bash
project_root/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── models/
│   │   └── __init__.py
│   │   └── models.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── embedding_service.py
│   │   ├── llm_service.py
│   │   └── vector_db_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── load_documents.py
│   │   └── logger.py
│   └── api/
│       ├── __init__.py
│       └── routes.py
│
├── data/
│   └── documento.docx
│
├── tests/
│   └── __init__.py
│
├── .dockerignore
├── .gitignore
├── requirements.txt
├── README.md
└── Dockerfile
```

## Desarrollo

* Utiliza FastAPI como framework para la API.
* Implementa embeddings y LLM utilizando Cohere.
* Utiliza ChromaDB como base de datos vectorial.
* Se puede ejecutar tanto en local como dockerizado.
* Soporta consultas en múltiples idiomas.
* El proyecto sigue una arquitectura limpia con separación de responsabilidades.
* Se utiliza variable de entorno para manejar la API key de Cohere.
* Se utiliza logging para el seguimiento de errores y eventos importantes.
* Los servicios de embeddings, LLM y base de datos vectorial están separados para
mayor modularidad.

## Colección de Postman

Para importar y usar la colección de Postman para probar la API RAG, sigue estos pasos:

1. Descarga e instala Postman desde postman.com si aún no lo tienes.

2. Abre Postman y haz clic en "Import" en la esquina superior izquierda.

3. Copia y pega el siguiente JSON en la ventana de importación:

```json
{
  "info": {
    "name": "RAG API Collection",
    "_postman_id": "rag-api-collection",
    "description": "Colección para probar la API RAG",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Query (Zara)",
      "request": {
        "url": "http://localhost:8000/query_answer",
        "method": "POST",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n    \"user_name\": \"John Doe\",\n    \"question\": \"¿Quién es Zara?\"\n}"
        }
      }
    },
    {
      "name": "Query (Emma)",
      "request": {
        "url": "http://localhost:8000/query_answer",
        "method": "POST",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n    \"user_name\": \"Jane Smith\",\n    \"question\": \"What did Emma decide to do?\"\n}"
        }
      }
    },
    {
      "name": "Query (Magical Flower)",
      "request": {
        "url": "http://localhost:8000/query_answer",
        "method": "POST",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n    \"user_name\": \"Alice Wonder\",\n    \"question\": \"What is the name of the magical flower?\"\n}"
        }
      }
    }
  ]
}
```

4. Haz clic en "Import" para añadir la colección a tu espacio de trabajo de Postman.

5. En la colección importada, encontrarás tres solicitudes predefinidas:
* Query (Zara): Pregunta sobre Zara
* Query (Emma): Pregunta sobre Emma
* Query (Magical Flower): Pregunta sobre la flor mágica

6. Asegúrate de que tu API esté en funcionamiento localmente en http://localhost:8000.

7. Puedes ejecutar cada solicitud individualmente haciendo clic en "Send", o ejecutar toda la colección haciendo clic derecho en la colección y seleccionando "Run collection".

8. Revisa las respuestas para asegurarte de que la API está respondiendo correctamente a las preguntas.

## Licencia

TBD
