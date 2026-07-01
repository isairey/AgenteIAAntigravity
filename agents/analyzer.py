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

        prompt = f"""
{ANALYZER_PROMPT}

Analiza el siguiente código:

```python
{code}