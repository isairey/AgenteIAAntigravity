"""
=========================================================
Antigravity AI
Orchestrator (PRO FIX v2)
=========================================================
"""

import time
from rich.console import Console

from agents.code_generator import CodeGeneratorAgent
from agents.analyzer import AnalyzerAgent
from agents.security import SecurityAgent
from agents.debugger import DebuggerAgent
from agents.fixer import FixerAgent
from agents.tester import TesterAgent
from agents.reviewer import ReviewerAgent
from agents.documentation import DocumentationAgent


class Orchestrator:
    """
    Orquestador robusto del sistema multiagente.
    """

    def __init__(self):
        self.console = Console()

        self.generator = CodeGeneratorAgent()
        self.analyzer = AnalyzerAgent()
        self.security = SecurityAgent()
        self.debugger = DebuggerAgent()
        self.fixer = FixerAgent()
        self.tester = TesterAgent()
        self.reviewer = ReviewerAgent()
        self.documentation = DocumentationAgent()

    # =====================================================
    # VALIDACIÓN DE RESPUESTAS
    # =====================================================

    def is_invalid(self, result: str) -> bool:
        """
        Detecta respuestas inválidas del LLM.
        """
        if not result:
            return True

        bad_signals = [
            "Error Gemini API",
            "Error Stream",
            "None",
            "Sin respuesta",
            "FALLÓ GENERACIÓN"
        ]

        return any(sig in result for sig in bad_signals)

    # =====================================================
    # SAFE RUN MEJORADO
    # =====================================================

    def safe_run(self, func, *args):
        """
        Ejecuta agentes sin romper pipeline.
        """

        try:
            result = func(*args)

            if self.is_invalid(result):
                return "FALLÓ AGENTE"

            return str(result)

        except Exception as e:
            return f"ERROR AGENTE: {str(e)}"

    # =====================================================
    # PIPELINE PRINCIPAL
    # =====================================================

    def run(self, request: str) -> dict:

        start_time = time.time()

        # =================================================
        # 1. GENERACIÓN (CRÍTICO)
        # =================================================
        self.console.print("\n[bold cyan]🚀 Generando código...[/bold cyan]")
        code = self.safe_run(self.generator.run, request)

        if self.is_invalid(code):
            self.console.print("\n[bold red]❌ Error crítico en generación. Abortando pipeline.[/bold red]")
            return {
                "code": code,
                "analysis": "ABORTADO",
                "security": "ABORTADO",
                "debug": "ABORTADO",
                "fixed_code": "ABORTADO",
                "tests": "ABORTADO",
                "review": "ABORTADO",
                "documentation": "ABORTADO",
                "execution_time": 0
            }

        # =================================================
        # 2. ANALISIS
        # =================================================
        self.console.print("\n[bold cyan]🔍 Analizando código...[/bold cyan]")
        analysis = self.safe_run(self.analyzer.run, code)

        self.console.print("\n[bold cyan]🔐 Analizando seguridad...[/bold cyan]")
        security = self.safe_run(self.security.run, code)

        self.console.print("\n[bold cyan]🐞 Depurando código...[/bold cyan]")
        debug = self.safe_run(self.debugger.run, code)

        # =================================================
        # 3. FIXER
        # =================================================
        self.console.print("\n[bold cyan]🛠 Corrigiendo código...[/bold cyan]")
        fixed_code = self.safe_run(
            self.fixer.run,
            code,
            analysis,
            security,
            debug
        )

        # fallback si falla fixer
        if self.is_invalid(fixed_code):
            fixed_code = code

        # =================================================
        # 4. TESTS + REVIEW
        # =================================================
        self.console.print("\n[bold cyan]🧪 Generando tests...[/bold cyan]")
        tests = self.safe_run(self.tester.run, fixed_code)

        self.console.print("\n[bold cyan]⭐ Revisando calidad...[/bold cyan]")
        review = self.safe_run(self.reviewer.run, fixed_code)

        # =================================================
        # 5. DOCS
        # =================================================
        self.console.print("\n[bold cyan]📄 Generando documentación...[/bold cyan]")
        docs = self.safe_run(
            self.documentation.run,
            "Proyecto generado por Antigravity AI",
            fixed_code
        )

        end_time = time.time()

        return {
            "code": code,
            "analysis": analysis,
            "security": security,
            "debug": debug,
            "fixed_code": fixed_code,
            "tests": tests,
            "review": review,
            "documentation": docs,
            "execution_time": end_time - start_time
        }

    # =====================================================
    # HELPERS
    # =====================================================

    def generate_only(self, request: str) -> str:
        return self.safe_run(self.generator.run, request)

    def analyze_only(self, code: str) -> str:
        return self.safe_run(self.analyzer.run, code)

    def security_only(self, code: str) -> str:
        return self.safe_run(self.security.run, code)

    def debug_only(self, code: str) -> str:
        return self.safe_run(self.debugger.run, code)

    def fix_only(self, code: str) -> str:
        return self.safe_run(self.fixer.run, code)

    def test_only(self, code: str) -> str:
        return self.safe_run(self.tester.run, code)

    def review_only(self, code: str) -> str:
        return self.safe_run(self.reviewer.run, code)

    def docs_only(self, code: str) -> str:
        return self.safe_run(
            self.documentation.run,
            "Proyecto",
            code
        )