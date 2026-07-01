from core.llm_client import ask_llm

class CodeGeneratorAgent:
    def run(self, task: str):
        prompt = f"""
        Genera código limpio, optimizado y funcional para la siguiente tarea:

        {task}

        Devuelve solo el código.
        """
        return ask_llm(prompt)