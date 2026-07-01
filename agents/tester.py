"""
=========================================================
Antigravity AI
Tester Agent
=========================================================

Genera pruebas unitarias para el código utilizando
Google Gemini.

Autor: ISAI
"""

from core.base_agent import BaseAgent
from core.prompts import TESTER_PROMPT


class TesterAgent(BaseAgent):
    """
    Agente encargado de generar pruebas unitarias.
    """

    def __init__(self):
        super().__init__(
            name="Tester",
            description="Genera pruebas unitarias para el código."
        )

    def run(self, code: str, framework: str = "pytest") -> str:
        """
        Genera pruebas unitarias.

        Args:
            code: Código fuente.
            framework: Framework de pruebas.

        Returns:
            Código de las pruebas.
        """

        if not code or not code.strip():
            return "No se proporcionó código para generar pruebas."

        prompt = f"""
{TESTER_PROMPT}

Framework:
{framework}

Código:

```text
{code}
```
"""