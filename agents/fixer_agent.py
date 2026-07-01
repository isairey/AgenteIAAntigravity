"""
=========================================================
Antigravity AI
Fixer Agent
=========================================================

Corrige automáticamente el código utilizando los
reportes generados por los demás agentes.

Responsabilidades:

- Corregir bugs
- Mejorar rendimiento
- Aplicar Clean Code
- Aplicar SOLID
- Corregir problemas de seguridad
- Reducir complejidad
- Optimizar arquitectura

Autor: ISAI
"""

from core.base_agent import BaseAgent
from core.prompts import FIXER_PROMPT


class FixerAgent(BaseAgent):
    """
    Agente encargado de corregir código.
    """

    def __init__(self):
        super().__init__(
            name="Fixer",
            description="Corrige automáticamente el código."
        )

    # =====================================================
    # Corrección principal
    # =====================================================

    def run(
        self,
        code: str,
        analysis: str = "",
        security: str = "",
        debugger: str = ""
    ) -> str:
        """
        Corrige el código utilizando los reportes
        de los demás agentes.
        """

        prompt = f"""
{FIXER_PROMPT}

Código original:

```python
{code}