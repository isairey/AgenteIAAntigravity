"""
=========================================================
Antigravity AI
Security Agent
=========================================================

Analiza el código desde el punto de vista de seguridad.

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

        if not code.strip():
            return "No se proporcionó código para analizar."

        prompt = f"""
{SECURITY_PROMPT}

Analiza el siguiente código fuente:

{code}

Busca específicamente:

- SQL Injection
- XSS
- CSRF
- Command Injection
- Path Traversal
- Hardcoded Secrets
- API Keys expuestas
- Credenciales embebidas
- JWT inseguros
- Problemas de autenticación
- Problemas de autorización
- Vulnerabilidades OWASP Top 10

Devuelve un reporte profesional indicando:

1. Vulnerabilidades encontradas.
2. Nivel de riesgo.
3. Recomendaciones.
4. Conclusión.

Devuelve únicamente el análisis.
"""

        return self.generate(prompt)