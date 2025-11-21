import os
from abc import ABC, abstractmethod
import google.generativeai as genai


# --- Definición de la Abstracción (La "Interfaz") ---
# ESTA PARTE NO CAMBIA NADA
class BaseLLMService(ABC):
    """
    Clase base abstracta (como un contrato o una plantilla)
    para cualquier servicio de LLM que queramos implementar.
    Define qué métodos DEBEN tener todas las clases hijas.
    """

    @abstractmethod
    def generate_commit_message(self, diff: str) -> str:
        """
        Genera un mensaje de commit a partir de un diff de código.
        """
        pass


# --- Implementación Concreta para Google Gemini (¡LA NUEVA CLASE!) ---
class GoogleLLMService(BaseLLMService):
    """
    Una implementación de BaseLLMService que usa la API de Google Gemini.
    """

    def __init__(self):
        # Cargar la clave de API desde las variables de entorno
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("La variable de entorno GOOGLE_API_KEY no está configurada.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('models/gemini-pro-latest')

    def generate_commit_message(self, diff: str) -> str:
        """
        Usa el modelo gemini-pro para generar un mensaje de commit
        siguiendo el estándar de Conventional Commits.
        """
        prompt = f"""
        Basado en el siguiente 'diff' de código, genera un mensaje de commit conciso y descriptivo
        en español, siguiendo estrictamente el estándar de Conventional Commits.

        El formato debe ser:
        <tipo>(<ámbito opcional>): <descripción corta en imperativo>

        [línea en blanco]

        <cuerpo opcional explicando el 'qué' y el 'porqué'>

        Tipos permitidos: feat, fix, docs, style, refactor, test, chore.

        Ejemplo de un buen commit:
        feat(api): añadir endpoint para registro de usuarios

        Se ha creado el endpoint POST /users para permitir el registro de nuevos
        usuarios. Se valida el email y la contraseña.

        Aquí está el diff:
        ---
        {diff}
        ---
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            # La API de Google puede devolver errores más complejos, los mostramos
            return f"Error al contactar la API de Google: {e}"

# --- Antigua Implementación de OpenAI (Opcional: la puedes borrar o dejar) ---
# La dejaremos aquí para demostrar que el código es extensible.
# from openai import OpenAI
# class OpenAILLMService(BaseLLMService):
#     ... (todo el código antiguo de OpenAI)