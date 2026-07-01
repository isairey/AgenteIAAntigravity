"""
=========================================================
Antigravity AI
Gemini Client (Google GenAI SDK)
=========================================================
"""

import os
from typing import Optional

from google import genai
from google.genai import types


class GeminiClient:
    """
    Cliente estable para Google Gemini API.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gemini-2.5-flash"
    ):

        # =====================================================
        # API KEY (FIX IMPORTANTE)
        # =====================================================

        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        self.model = model

        if not self.api_key:
            raise ValueError(
                "❌ GOOGLE_API_KEY no encontrada en variables de entorno"
            )

        # Cliente oficial Google GenAI
        self.client = genai.Client(api_key=self.api_key)

    # =====================================================
    # SAFE GENERATE (🔥 FIX CRÍTICO)
    # =====================================================

    def generate(self, prompt: str, temperature: float = 0.2) -> str:
        """
        Generación segura con manejo real de errores.
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

            # =================================================
            # VALIDACIÓN REAL DE RESPUESTA
            # =================================================

            if not response:
                return "Sin respuesta de Gemini"

            if not hasattr(response, "text"):
                return "Respuesta inválida de Gemini"

            if response.text is None:
                return "Respuesta vacía de Gemini"

            return str(response.text)

        except Exception as e:
            return f"Error Gemini API (generate): {str(e)}"

    # =====================================================
    # CHAT
    # =====================================================

    def chat(self, messages: list, temperature: float = 0.2) -> str:
        """
        Chat con historial seguro.
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

            if not response or not hasattr(response, "text"):
                return "Sin respuesta de Gemini Chat"

            return str(response.text)

        except Exception as e:
            return f"Error Gemini API (chat): {str(e)}"

    # =====================================================
    # STREAM
    # =====================================================

    def stream(self, prompt: str, temperature: float = 0.2):
        """
        Streaming seguro.
        """

        try:
            for chunk in self.client.models.generate_content_stream(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=temperature
                )
            ):
                if chunk and hasattr(chunk, "text") and chunk.text:
                    yield chunk.text

        except Exception as e:
            yield f"Error Stream: {str(e)}"

    # =====================================================
    # CAMBIAR MODELO
    # =====================================================

    def set_model(self, model: str):
        self.model = model