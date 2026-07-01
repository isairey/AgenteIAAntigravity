"""
=========================================================
Antigravity AI
Fixer Agent
=========================================================

Responsabilidad:

- Corrige código basado en análisis
- Aplica mejoras sugeridas
- Elimina bugs
- Refactoriza

Autor: ISAI
"""

from core.base_agent import BaseAgent


class FixerAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Fixer",
            description="Corrige y mejora código automáticamente."
        )

    def run(self, code: str, analysis: str, security: str, debug: str) -> str:

        prompt = f"""
Eres un experto en refactorización de código.

Corrige el siguiente código:

================ CODE ================
{code}

================ ANALYSIS ================
{analysis}

================ SECURITY ================
{security}

================ DEBUG ================
{debug}

INSTRUCCIONES:
- Corrige bugs
- Mejora seguridad
- Aplica Clean Code
- No cambies la lógica innecesariamente
- Devuelve SOLO código final
"""

        return self.generate(prompt)