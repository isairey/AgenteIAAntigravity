"""
=========================================================
Antigravity AI
Security Agent
=========================================================

Analiza el código desde el punto de vista de seguridad.

Detecta:

- SQL Injection
- XSS
- CSRF
- Command Injection
- Path Traversal
- Hardcoded Secrets
- API Keys
- Credenciales
- JWT inseguros
- Errores de autenticación
- Errores de autorización
- OWASP Top 10

Autor: ISAI
"""

from core.base_agent import BaseAgent
from core.prompts import SECURITY_PROMPT


class SecurityAgent(BaseAgent):
    """
    Agente encargado de revisar la seguridad del código.
    """

    def __init__(self):
        super().__init__(
            name="Security",
            description="Analiza vulnerabilidades de seguridad."
        )

    # =====================================================
    # Análisis principal
    # =====================================================

    def run(self, code: str) -> str:
        """
        Analiza un bloque de código.

        Args:
            code: Código fuente.

        Returns:
            Reporte de seguridad.
        """

        prompt = f"""
{SECURITY_PROMPT}

Analiza el siguiente código.

```python
{code}