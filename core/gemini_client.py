"""
=========================================================
Antigravity AI
Gemini Client (Google GenAI SDK)
=========================================================

Cliente oficial para Google Gemini.

Usa:
- google-genai (SDK nuevo)
- Gemini 2.5 Flash / Pro

Responsabilidad:
- Enviar prompts
- Recibir respuestas
- Manejar errores
- Configuración centralizada

Autor: ISAI
"""

import os
from typing import Optional

from google import genai
from google.genai import types


class GeminiClient:
    """
    Cliente principal para Google Gemini API.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gemini-2.5-flash"
    ):

        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model = model

        if not self.api_key:
            raise ValueError("❌ GEMINI_API_KEY no encontrada en variables de entorno")

        # Cliente oficial
        self.client = genai.Client(api_key=self.api_key)

    # =====================================================
    # Generación básica
    # =====================================================

    def generate(self, prompt: str, temperature: float = 0.2) -> str:
        """
        Envía un prompt a Gemini y devuelve la respuesta.
        """

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=temperature,
                    max_output_tokens=8192
                )
            )

            return response.text or ""

        except Exception as e:
            return f"Error Gemini API: {str(e)}"

    # =====================================================
    # Chat estructurado (multi-turn)
    # =====================================================

    def chat(self, messages: list, temperature: float = 0.2) -> str:
        """
        Chat con historial.
        """

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=messages,
                config=types.GenerateContentConfig(
                    temperature=temperature,
                    max_output_tokens=8192
                )
            )

            return response.text or ""

        except Exception as e:
            return f"Error Gemini Chat: {str(e)}"

    # =====================================================
    # Streaming (opcional)
    # =====================================================

    def stream(self, prompt: str, temperature: float = 0.2):
        """
        Respuesta en streaming.
        """

        try:
            for chunk in self.client.models.generate_content_stream(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=temperature
                )
            ):
                if chunk.text:
                    yield chunk.text

        except Exception as e:
            yield f"Error Stream: {str(e)}"

    # =====================================================
    # Utilidad: cambiar modelo
    # =====================================================

    def set_model(self, model: str):
        """
        Cambia el modelo dinámicamente.
        """
        self.model = model