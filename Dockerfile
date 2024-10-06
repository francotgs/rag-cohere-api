# Imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Configurar el PYTHONPATH para que incluya el directorio /app
ENV PYTHONPATH=/app

# Copiar los archivos requirements.txt al contenedor
COPY requirements.txt .

# Actualizar pip e instalar dependencias
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
