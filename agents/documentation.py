"""
=========================================================
Antigravity AI
Documentation Agent
=========================================================

Genera documentación profesional para proyectos.

Funciones:

- README.md
- Documentación técnica
- API Docs
- Comentarios
- Docstrings
- Changelog
- Guía de instalación

Autor: ISAI
"""

from core.base_agent import BaseAgent
from core.prompts import DOCUMENTATION_PROMPT


class DocumentationAgent(BaseAgent):
    """
    Agente encargado de generar documentación.
    """

    def __init__(self):
        super().__init__(
            name="Documentation",
            description="Genera documentación profesional."
        )

    # =====================================================
    # README
    # =====================================================

    def run(
        self,
        project_name: str,
        code: str
    ) -> str:
        """
        Genera un README completo.
        """

        prompt = f"""
{DOCUMENTATION_PROMPT}

Proyecto:

{project_name}

Código:

```python
{code}