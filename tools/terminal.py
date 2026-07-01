"""
=========================================================
Antigravity AI
Terminal Tool
=========================================================

Responsabilidad:

- Ejecutar comandos del sistema
- Capturar output de consola
- Usado por agentes para automatización
- Build / run / test / install dependencies

⚠️ IMPORTANTE:
Este módulo ejecuta comandos reales del sistema.

Autor: ISAI
"""

import subprocess
from typing import Optional


class Terminal:
    """
    Ejecuta comandos en la terminal.
    """

    def __init__(self, working_dir: str = "."):

        self.working_dir = working_dir

    # =====================================================
    # Ejecutar comando
    # =====================================================

    def run(
        self,
        command: str,
        timeout: Optional[int] = 60
    ) -> str:
        """
        Ejecuta un comando en la terminal.

        Args:
            command: comando a ejecutar
            timeout: tiempo máximo de ejecución
        """

        try:
            result = subprocess.run(
                command,
                cwd=self.working_dir,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout
            )

            output = result.stdout.strip()
            error = result.stderr.strip()

            if result.returncode != 0:
                return f"[ERROR]\n{error}"

            return output if output else "[OK] Comando ejecutado sin salida"

        except subprocess.TimeoutExpired:
            return "[TIMEOUT] El comando tardó demasiado"

        except Exception as e:
            return f"[EXCEPTION] {str(e)}"

    # =====================================================
    # Ejecutar múltiples comandos
    # =====================================================

    def run_batch(
        self,
        commands: list,
        stop_on_error: bool = False
    ) -> list:
        """
        Ejecuta una lista de comandos.
        """

        results = []

        for cmd in commands:

            result = self.run(cmd)
            results.append({
                "command": cmd,
                "result": result
            })

            if stop_on_error and "[ERROR]" in result:
                break

        return results

    # =====================================================
    # Instalar dependencias
    # =====================================================

    def install(
        self,
        package: str
    ) -> str:
        """
        Instala un paquete con pip.
        """

        return self.run(f"pip install {package}")

    # =====================================================
    # Ejecutar tests
    # =====================================================

    def run_tests(self, test_command: str = "pytest") -> str:
        """
        Ejecuta tests del proyecto.
        """

        return self.run(test_command)

    # =====================================================
    # Levantar servidor
    # =====================================================

    def start_server(self, command: str) -> str:
        """
        Inicia un servidor (FastAPI, Flask, etc).
        """

        return self.run(command)

    # =====================================================
    # Build proyecto
    # =====================================================

    def build(self, command: str = "build") -> str:
        """
        Ejecuta proceso de build.
        """

        return self.run(command)