from core.llm_client import ask_llm

class SecurityAgent:
    def run(self, code: str):
        prompt = f"""
        Revisa el siguiente código desde el punto de vista de seguridad.
        Detecta:
        - vulnerabilidades
        - inyecciones posibles
        - malas prácticas de seguridad

        Código:
        {code}
        """
        return ask_llm(prompt)