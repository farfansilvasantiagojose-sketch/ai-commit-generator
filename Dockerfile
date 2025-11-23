FROM python:3.10-slim

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
WORKDIR /app

# Copiar el archivo de dependencias.
COPY requirements.txt .

# Instalar las dependencias de Python.
# --no-cache-dir para evita guardar la caché de pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código de la carpeta local "src"
# a la carpeta "/app/src" dentro del contenedor.
COPY ./src ./src