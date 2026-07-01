from core.llm_client import ask_llm

class CodeAnalyzerAgent:
    def run(self, code: str):
        prompt = f"""
        Analiza el siguiente código y detecta:
        - errores
        - malas prácticas
        - posibles bugs

        Código:
        {code}
        """
        return ask_llm(prompt)