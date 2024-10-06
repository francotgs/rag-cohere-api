# RAG API

Esta es una API que implementa una solución de **Retrieval Augmented Generation (RAG)** utilizando **FastAPI**, **LangChain** y **ChromaDB**.

La aplicación se puede ejecutar tanto localmente como dentro de un contenedor Docker.

- [Requisitos](#requisitos)
- [Instalación y ejecución en local](#instalaci-n-y-ejecuci-n-en-local)
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
* Soporta consultas en múltiples idiomas.
* El proyecto sigue una arquitectura limpia con separación de responsabilidades.
* Se utiliza logging para el seguimiento de errores y eventos importantes.
* Los servicios de embeddings, LLM y base de datos vectorial están separados para mayor modularidad.

## Licencia

TBD
