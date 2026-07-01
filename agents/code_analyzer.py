"""
=========================================================
Antigravity AI
Code Analyzer Agent
=========================================================

Analiza código fuente utilizando Google Gemini.

Responsabilidades:

- Revisar arquitectura
- Detectar bugs
- Detectar código duplicado
- Detectar malas prácticas
- Analizar rendimiento
- Analizar complejidad
- Revisar Clean Code
- Revisar SOLID

Autor: ISAI
"""

from core.base_agent import BaseAgent
from core.prompts import ANALYZER_PROMPT


class CodeAnalyzerAgent(BaseAgent):
    """
    Agente encargado de analizar código.
    """

    def __init__(self):
        super().__init__(
            name="Code Analyzer",
            description="Analiza la calidad del código."
        )

    # =====================================================
    # Análisis principal
    # =====================================================

    def run(self, code: str) -> str:
        """
        Analiza el código y genera un reporte.
        """

        if not code.strip():
            return "No se proporcionó código para analizar."

        prompt = f"""
{ANALYZER_PROMPT}

Analiza cuidadosamente el siguiente código fuente:

{code}

Genera un reporte profesional que incluya:

- Calidad del código.
- Bugs encontrados.
- Problemas de arquitectura.
- Violaciones a SOLID.
- Problemas de Clean Code.
- Complejidad.
- Rendimiento.
- Código duplicado.
- Posibles mejoras.

Devuelve únicamente el análisis.
"""

        return self.generate(prompt)