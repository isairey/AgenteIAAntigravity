"""
=========================================================
Antigravity AI
Analyzer Agent
=========================================================

Agente encargado de analizar código fuente.

Responsabilidades:

- Detectar bugs
- Evaluar arquitectura
- Revisar Clean Code
- Revisar SOLID
- Analizar rendimiento
- Detectar código duplicado
- Detectar malas prácticas

Autor: ISAI
"""

from core.base_agent import BaseAgent
from core.prompts import ANALYZER_PROMPT


class AnalyzerAgent(BaseAgent):
    """
    Agente principal de análisis de código.
    """

    def __init__(self):
        super().__init__(
            name="Analyzer",
            description="Analiza calidad, arquitectura y errores del código."
        )

    # =====================================================
    # Análisis principal
    # =====================================================

    def run(self, code: str) -> str:
        """
        Ejecuta el análisis completo del código.
        """

        if not code.strip():
            return "No se proporcionó código para analizar."

        prompt = f"""
{ANALYZER_PROMPT}

Analiza el siguiente código fuente:

{code}

Realiza un análisis profesional que incluya:

1. Bugs encontrados.
2. Problemas de arquitectura.
3. Violaciones a SOLID.
4. Problemas de Clean Code.
5. Complejidad del código.
6. Rendimiento.
7. Posibles mejoras.
8. Conclusión general.

Devuelve únicamente el análisis.
"""

        return self.generate(prompt)