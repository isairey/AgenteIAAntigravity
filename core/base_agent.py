"""
=========================================================
Antigravity AI
Base Agent
=========================================================

Clase base para todos los agentes del sistema.

Responsabilidad:

- Conectar con GeminiClient
- Proveer utilidades comunes
- Manejo de archivos
- Interfaz estándar para agentes

Todos los agentes heredan de aquí.

Autor: ISAI
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

        # Cliente Gemini compartido
        self.llm = GeminiClient(model=model)

    # =====================================================
    # Generación principal
    # =====================================================

    def generate(self, prompt: str, temperature: float = 0.2) -> str:
        """
        Genera respuesta usando Gemini.
        """

        return self.llm.generate(
            prompt=prompt,
            temperature=temperature
        )

    # =====================================================
    # Chat multi-turn
    # =====================================================

    def chat(self, messages: list, temperature: float = 0.2) -> str:
        """
        Chat con historial.
        """

        return self.llm.chat(
            messages=messages,
            temperature=temperature
        )

    # =====================================================
    # Streaming
    # =====================================================

    def stream(self, prompt: str, temperature: float = 0.2):
        """
        Streaming de respuesta.
        """

        return self.llm.stream(
            prompt=prompt,
            temperature=temperature
        )

    # =====================================================
    # Utilidad: leer archivo
    # =====================================================

    def read_file(self, path: str) -> str:
        """
        Lee un archivo de texto.
        """

        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()

        except Exception as e:
            return f"Error leyendo archivo: {str(e)}"

    # =====================================================
    # Utilidad: escribir archivo
    # =====================================================

    def write_file(self, path: str, content: str) -> None:
        """
        Escribe contenido en un archivo.
        """

        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

        except Exception as e:
            print(f"Error escribiendo archivo: {str(e)}")

    # =====================================================
    # Info del agente
    # =====================================================

    def info(self) -> str:
        """
        Devuelve información del agente.
        """

        return f"""
Agent: {self.name}
Description: {self.description}
Model: {self.llm.model}
"""