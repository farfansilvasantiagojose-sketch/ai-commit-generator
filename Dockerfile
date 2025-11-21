# Paso 1: Usar una imagen base oficial de Python.
# "python:3.10-slim" es una versión ligera, ideal para producción.
FROM python:3.10-slim

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
WORKDIR /app

# Paso 3: Copiar el archivo de dependencias PRIMERO.
# Docker es inteligente. Si requirements.txt no cambia, reutilizará
# la capa cacheada del siguiente paso, haciendo las construcciones futuras más rápidas.
COPY requirements.txt .

# Paso 4: Instalar las dependencias de Python.
# --no-cache-dir evita guardar la caché de pip, manteniendo la imagen pequeña.
RUN pip install --no-cache-dir -r requirements.txt

# Paso 5: Copiar todo el código de nuestra carpeta local "src"
# a la carpeta "/app/src" dentro del contenedor.
COPY ./src ./src