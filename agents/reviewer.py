"""
=========================================================
Antigravity AI
Reviewer Agent
=========================================================

Evalúa la calidad general del código generado.

Responsabilidades:

- Revisar arquitectura
- Revisar Clean Code
- Revisar SOLID
- Revisar rendimiento
- Revisar mantenibilidad
- Revisar seguridad
- Calificar el proyecto
- Decidir si el código debe regresar
  al Generator o al Fixer.

Autor: ISAI
"""

from core.base_agent import BaseAgent
from core.prompts import REVIEWER_PROMPT


class ReviewerAgent(BaseAgent):
    """
    Agente encargado de revisar el resultado final
    generado por los demás agentes.
    """

    def __init__(self):
        super().__init__(
            name="Reviewer",
            description="Revisa la calidad del proyecto."
        )

    # =====================================================
    # Revisión principal
    # =====================================================

    def run(self, code: str) -> str:
        """
        Revisa un proyecto completo.

        Args:
            code: Código fuente.

        Returns:
            Reporte de revisión.
        """

        prompt = f"""
{REVIEWER_PROMPT}

Analiza cuidadosamente el siguiente código.

```python
{code}