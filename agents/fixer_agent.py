from core.llm_client import ask_llm

class FixerAgent:
    def run(self, code: str, analysis: str, security: str):
        prompt = f"""
        Corrige el siguiente código tomando en cuenta:

        🔍 Análisis de errores:
        {analysis}

        🛡️ Seguridad:
        {security}

        Código original:
        {code}

        Devuelve SOLO el código corregido.
        """
        return ask_llm(prompt)