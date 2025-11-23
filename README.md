Autor Santiago farfan
# 🤖 Generador de Mensajes de Commit con IA

Este es un proyecto de herramienta de línea de comandos (CLI) que utiliza un LLM (a través de la API de Google Gemini) para generar automáticamente mensajes de commit siguiendo el estándar de **Conventional Commits**.

El proyecto está completamente **dockerizado**, garantizando un entorno de desarrollo reproducible y limpio. Además, su arquitectura sigue los **principios de diseño SOLID** para un código mantenible y escalable.

## ✨ Características Principales

-   **Generación Inteligente**: Analiza los cambios en el "staging area" de Git (`git diff --staged`).
-   **Estándar Profesional**: Genera mensajes que cumplen con la especificación de Conventional Commits.
-   **Entorno Aislado**: Se ejecuta 100% dentro de un contenedor Docker. ¡No necesitas instalar Python ni dependencias en tu máquina!
-   **Código Limpio**: Estructurado con el Principio de Responsabilidad Única, Principio Abierto/Cerrado y de Inversión de Dependencias.

## 🚀 Requisitos Previos

-   [Docker](https://www.docker.com/get-started) y [Docker Compose](https://docs.docker.com/compose/install/) instalados.
-   Una clave de API de [Google AI Studio (Gemini)](https://aistudio.google.com/app/apikey).

## ⚙️ Configuración

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/farfansilvasantiagojose-sketch/ai-commit-generator.git
    cd cd ai-commit-generator
    ```

2.  **Crea tu archivo de entorno:**
    En la raíz del proyecto, crea un archivo llamado `.env`.

3.  **Añade tu API Key de Google:**
    Abre el archivo `.env` y añade tu clave secreta de Google Gemini y la configuración de GitPython:
    ```env
    GOOGLE_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxxxxx
    GIT_PYTHON_REFRESH=quiet
    ```

4.  **Construye la imagen de Docker:**
    Este comando leerá el `Dockerfile` y `requirements.txt` para construir el entorno de la aplicación. Solo necesitas hacerlo la primera vez o cuando cambies las dependencias.
    ```bash
    docker-compose build
    ```

## 🛠️ Cómo Usarlo

El flujo de trabajo es simple:

1.  **Realiza cambios en tu código** como lo harías normalmente.

2.  **Añade tus cambios al "staging area" de Git:**
    ```bash
    # Añadir un archivo específico
    git add nombre_del_archivo.py

    # O añadir todos los cambios
    git add .
    ```

3.  **Ejecuta la herramienta:**
    Usa el siguiente comando para que la IA genere el mensaje de commit:
    ```bash
    docker-compose run --rm app python src/main.py
    ```
La herramienta analizará los cambios y te mostrará un mensaje de commit sugerido en la terminal.

## 🏛️ Arquitectura (Principios SOLID)

El código está estructurado para ser mantenible y fácil de entender:

-   `src/services/git_service.py`: Tiene la **única responsabilidad** de interactuar con Git.
-   `src/services/llm_service.py`: Tiene la **única responsabilidad** de comunicarse con el LLM. Utiliza una clase base abstracta para que sea **abierto a extensión** (se podría volver a añadir soporte para OpenAI) pero **cerrado a modificación**.
-   `src/main.py`: Es el orquestador que depende de las **abstracciones** de los servicios, no de sus implementaciones concretas.