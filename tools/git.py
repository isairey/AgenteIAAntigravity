"""
=========================================================
Antigravity AI
Git Manager Tool
=========================================================

Responsabilidad:

- Manejo básico de Git
- Auto commits del sistema multiagente
- Versionado de código generado
- Snapshots del proyecto

Autor: ISAI
"""

import subprocess
from datetime import datetime
from typing import Optional


class GitManager:
    """
    Herramienta para manejar Git automáticamente.
    """

    def __init__(self, repo_path: str = "."):

        self.repo_path = repo_path

    # =====================================================
    # Ejecutar comando git
    # =====================================================

    def run_git_command(self, command: list) -> str:
        """
        Ejecuta comandos de git.
        """

        try:
            result = subprocess.run(
                ["git"] + command,
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                return result.stderr

            return result.stdout.strip()

        except Exception as e:
            return f"Git error: {str(e)}"

    # =====================================================
    # Inicializar repo
    # =====================================================

    def init(self) -> str:
        """
        Inicializa repositorio git.
        """

        return self.run_git_command(["init"])

    # =====================================================
    # Estado del repo
    # =====================================================

    def status(self) -> str:
        """
        Ver estado del repositorio.
        """

        return self.run_git_command(["status"])

    # =====================================================
    # Agregar archivos
    # =====================================================

    def add_all(self) -> str:
        """
        Agrega todos los archivos.
        """

        return self.run_git_command(["add", "."])

    # =====================================================
    # Commit automático
    # =====================================================

    def commit(self, message: Optional[str] = None) -> str:
        """
        Hace commit con mensaje automático.
        """

        if not message:
            message = f"Auto commit - Antigravity AI - {datetime.now()}"

        return self.run_git_command(["commit", "-m", message])

    # =====================================================
    # Push
    # =====================================================

    def push(self, branch: str = "main") -> str:
        """
        Hace push al repositorio.
        """

        return self.run_git_command(["push", "origin", branch])

    # =====================================================
    # Pull
    # =====================================================

    def pull(self, branch: str = "main") -> str:
        """
        Hace pull del repositorio.
        """

        return self.run_git_command(["pull", "origin", branch])

    # =====================================================
    # Crear snapshot
    # =====================================================

    def snapshot(self, tag: Optional[str] = None) -> str:
        """
        Crea un snapshot del estado actual.
        """

        if not tag:
            tag = f"snapshot-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

        return self.run_git_command(["tag", tag])

    # =====================================================
    # Commit completo automático
    # =====================================================

    def auto_commit(self, message: str = None) -> str:
        """
        Flujo completo:
        add → commit
        """

        self.add_all()
        return self.commit(message)

    # =====================================================
    # Logs de commits
    # =====================================================

    def log(self, limit: int = 5) -> str:
        """
        Muestra historial de commits.
        """

        return self.run_git_command(["log", f"-{limit}", "--oneline"])