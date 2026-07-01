"""
=========================================================
Antigravity AI
Orchestrator
=========================================================

Coordina todos los agentes del sistema.

Flujo recomendado:

Planner → Generator → Analyzer → Security → Debugger
→ Fixer → Tester → Reviewer → Documentation

Autor: ISAI
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
    Orquestador principal del sistema multiagente.
    """

    def __init__(self):

        self.console = Console()

        # ================================
        # Agentes
        # ================================

        self.generator = CodeGeneratorAgent()
        self.analyzer = AnalyzerAgent()
        self.security = SecurityAgent()
        self.debugger = DebuggerAgent()
        self.fixer = FixerAgent()
        self.tester = TesterAgent()
        self.reviewer = ReviewerAgent()
        self.documentation = DocumentationAgent()

        # ================================
        # Estado
        # ================================

        self.code = ""
        self.analysis = ""
        self.security_report = ""
        self.debug_report = ""
        self.fixed_code = ""
        self.test_report = ""
        self.review = ""

    # =====================================================
    # Ejecutar pipeline completo
    # =====================================================

    def run(self, request: str) -> dict:
        """
        Ejecuta todo el flujo de agentes.
        """

        start_time = time.time()

        self.console.print("\n[bold cyan]🚀 Generando código...[/bold cyan]")
        self.code = self.generator.run(request)

        self.console.print("\n[bold cyan]🔍 Analizando código...[/bold cyan]")
        self.analysis = self.analyzer.run(self.code)

        self.console.print("\n[bold cyan]🔐 Analizando seguridad...[/bold cyan]")
        self.security_report = self.security.run(self.code)

        self.console.print("\n[bold cyan]🐞 Depurando código...[/bold cyan]")
        self.debug_report = self.debugger.run(self.code)

        self.console.print("\n[bold cyan]🛠 Corrigiendo código...[/bold cyan]")
        self.fixed_code = self.fixer.run(
            self.code,
            self.analysis,
            self.security_report,
            self.debug_report
        )

        self.console.print("\n[bold cyan]🧪 Generando tests...[/bold cyan]")
        self.test_report = self.tester.run(self.fixed_code)

        self.console.print("\n[bold cyan]⭐ Revisando calidad...[/bold cyan]")
        self.review = self.reviewer.run(self.fixed_code)

        self.console.print("\n[bold cyan]📄 Generando documentación...[/bold cyan]")
        docs = self.documentation.run(
            "Proyecto generado por Antigravity AI",
            self.fixed_code
        )

        end_time = time.time()

        return {
            "code": self.code,
            "analysis": self.analysis,
            "security": self.security_report,
            "debug": self.debug_report,
            "fixed_code": self.fixed_code,
            "tests": self.test_report,
            "review": self.review,
            "documentation": docs,
            "execution_time": end_time - start_time
        }

    # =====================================================
    # Ejecutar solo generación
    # =====================================================

    def generate_only(self, request: str) -> str:
        return self.generator.run(request)

    # =====================================================
    # Ejecutar solo análisis
    # =====================================================

    def analyze_only(self, code: str) -> str:
        return self.analyzer.run(code)

    # =====================================================
    # Ejecutar solo seguridad
    # =====================================================

    def security_only(self, code: str) -> str:
        return self.security.run(code)

    # =====================================================
    # Ejecutar solo debug
    # =====================================================

    def debug_only(self, code: str) -> str:
        return self.debugger.run(code)

    # =====================================================
    # Ejecutar solo fixer
    # =====================================================

    def fix_only(self, code: str) -> str:
        return self.fixer.run(code)

    # =====================================================
    # Ejecutar solo tests
    # =====================================================

    def test_only(self, code: str) -> str:
        return self.tester.run(code)

    # =====================================================
    # Ejecutar solo review
    # =====================================================

    def review_only(self, code: str) -> str:
        return self.reviewer.run(code)

    # =====================================================
    # Ejecutar solo documentación
    # =====================================================

    def docs_only(self, code: str) -> str:
        return self.documentation.run(
            "Proyecto",
            code
        )