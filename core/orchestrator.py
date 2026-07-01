from agents.code_generator import CodeGeneratorAgent
from agents.code_analyzer import CodeAnalyzerAgent
from agents.security_agent import SecurityAgent
from agents.fixer_agent import FixerAgent

class AntigravityOrchestrator:
    def __init__(self):
        self.generator = CodeGeneratorAgent()
        self.analyzer = CodeAnalyzerAgent()
        self.security = SecurityAgent()
        self.fixer = FixerAgent()

    def run(self, task: str):
        print("🧠 Generando código...")
        code = self.generator.run(task)

        print("🔍 Analizando código...")
        analysis = self.analyzer.run(code)

        print("🛡️ Revisando seguridad...")
        security = self.security.run(code)

        print("🔧 Corrigiendo código...")
        fixed_code = self.fixer.run(code, analysis, security)

        return {
            "original_code": code,
            "analysis": analysis,
            "security": security,
            "fixed_code": fixed_code
        }