"""
=========================================================
Antigravity AI
Debugger Agent
=========================================================

Analiza código para encontrar errores, excepciones,
problemas de lógica y oportunidades de mejora.

Responsabilidades:

- Detectar errores de sintaxis
- Detectar errores de ejecución
- Encontrar código muerto
- Detectar imports innecesarios
- Detectar variables sin usar
- Detectar excepciones potenciales
- Sugerir correcciones

Autor: ISAI
"""

from core.base_agent import BaseAgent
from core.prompts import DEBUGGER_PROMPT


class DebuggerAgent(BaseAgent):
    """
    Agente encargado de depurar código.
    """

    def __init__(self):
        super().__init__(
            name="Debugger",
            description="Analiza y corrige errores del código."
        )

    # =====================================================
    # Depuración principal
    # =====================================================

    def run(self, code: str) -> str:
        """
        Analiza el código y genera un reporte.
        """

        prompt = f"""
{DEBUGGER_PROMPT}

Analiza cuidadosamente el siguiente código.

```python
{code}