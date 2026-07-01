"""
=========================================================
Antigravity AI
Base Agent
=========================================================
"""

from core.gemini_client import GeminiClient


class BaseAgent:
    """
    Clase base para todos los agentes.
    """

    def __init__(
        self,
        name: str,
        description: str,
        model: str = "gemini-2.5-flash"
    ):

        self.name = name
        self.description = description
        self.llm = GeminiClient(model=model)

    # =====================================================
    # GENERATE
    # =====================================================

    def generate(self, prompt: str, temperature: float = 0.2):
        """
        Genera una respuesta usando Gemini.
        Devuelve None si ocurre un error.
        """

        try:
            response = self.llm.generate(
                prompt=prompt,
                temperature=temperature
            )

            if not response:
                return None

            # Si Gemini devolvió un mensaje de error
            if isinstance(response, str) and response.startswith("Error"):
                return None

            return response.strip()

        except Exception as e:
            print(f"[{self.name}] Error generate: {e}")
            return None

    # =====================================================
    # CHAT
    # =====================================================

    def chat(self, messages: list, temperature: float = 0.2):

        try:
            response = self.llm.chat(
                messages=messages,
                temperature=temperature
            )

            if not response:
                return None

            if isinstance(response, str) and response.startswith("Error"):
                return None

            return response.strip()

        except Exception as e:
            print(f"[{self.name}] Error chat: {e}")
            return None

    # =====================================================
    # STREAM
    # =====================================================

    def stream(self, prompt: str, temperature: float = 0.2):
        """
        Streaming de respuesta.
        """

        try:
            return self.llm.stream(
                prompt=prompt,
                temperature=temperature
            )

        except Exception as e:
            print(f"[{self.name}] Error stream: {e}")
            return None

    # =====================================================
    # FILES
    # =====================================================

    def read_file(self, path: str):

        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()

        except Exception as e:
            print(f"[{self.name}] Error leyendo archivo: {e}")
            return None

    def write_file(self, path: str, content: str):

        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            return True

        except Exception as e:
            print(f"[{self.name}] Error escribiendo archivo: {e}")
            return False

    # =====================================================
    # INFO
    # =====================================================

    def info(self):

        return (
            f"Agent: {self.name}\n"
            f"Description: {self.description}\n"
            f"Model: {self.llm.model}"
        )