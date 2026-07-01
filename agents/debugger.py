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

        if not code.strip():
            return "No se proporcionó código para depurar."

        prompt = f"""
{DEBUGGER_PROMPT}

Analiza cuidadosamente el siguiente código fuente:

{code}

Realiza una depuración completa e identifica:

1. Errores de sintaxis.
2. Posibles excepciones en tiempo de ejecución.
3. Variables sin utilizar.
4. Imports innecesarios.
5. Código muerto.
6. Problemas de lógica.
7. Posibles optimizaciones.
8. Recomendaciones para corregir los errores.

Devuelve únicamente el reporte de depuración.
"""

        return self.generate(prompt)