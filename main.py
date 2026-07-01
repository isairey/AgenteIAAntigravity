"""
=========================================================
Antigravity AI
Main Entry Point
=========================================================

Responsabilidad:

- Punto de entrada del sistema
- Ejecuta el Orchestrator
- Muestra resultados
- Controla flujo principal

Autor: ISAI
"""

import os
from dotenv import load_dotenv

from core.orchestrator import Orchestrator
from rich.console import Console


# =========================================================
# Cargar variables de entorno
# =========================================================

load_dotenv()


def main():
    """
    Ejecuta el sistema multiagente completo.
    """

    console = Console()

    # =====================================================
    # Banner inicial
    # =====================================================

    console.print("\n[bold cyan]==============================[/bold cyan]")
    console.print("[bold cyan]   🚀 ANTIGRAVITY AI START   [/bold cyan]")
    console.print("[bold cyan]==============================[/bold cyan]\n")

    # =====================================================
    # API KEY CHECK (IMPORTANTE)
    # =====================================================

    api_key = os.getenv("GOOGLE_API_KEY")  # 🔥 IMPORTANTE: usa solo una variable

    if not api_key:
        console.print("[bold red]❌ ERROR: No se encontró GOOGLE_API_KEY en .env[/bold red]")
        console.print("[yellow]💡 Agrega tu API key en el archivo .env[/yellow]\n")
        return

    # =====================================================
    # Crear Orchestrator
    # =====================================================

    try:
        orchestrator = Orchestrator()
    except Exception as e:
        console.print(f"[bold red]❌ Error inicializando Orchestrator: {e}[/bold red]")
        return

    # =====================================================
    # Input del usuario
    # =====================================================

    request = input("💡 Describe lo que quieres generar:\n> ")

    if not request or not request.strip():
        console.print("[bold red]❌ Error: solicitud vacía[/bold red]")
        return

    # =====================================================
    # Ejecutar sistema
    # =====================================================

    console.print("\n[bold yellow]⏳ Ejecutando pipeline multiagente...[/bold yellow]\n")

    try:
        result = orchestrator.run(request)

    except Exception as e:
        console.print(f"[bold red]❌ Error durante ejecución: {str(e)}[/bold red]")
        return

    # =====================================================
    # Seguridad contra None (MUY IMPORTANTE)
    # =====================================================

    def safe(key):
        return result.get(key) or "Sin datos"

    # =====================================================
    # Mostrar resultados
    # =====================================================

    console.print("\n[bold green]==============================[/bold green]")
    console.print("[bold green]        RESULTADOS           [/bold green]")
    console.print("[bold green]==============================[/bold green]\n")

    console.print("\n[bold cyan]📌 Código generado:[/bold cyan]\n")
    console.print(safe("code"))

    console.print("\n[bold cyan]🔍 Análisis:[/bold cyan]\n")
    console.print(safe("analysis"))

    console.print("\n[bold cyan]🔐 Seguridad:[/bold cyan]\n")
    console.print(safe("security"))

    console.print("\n[bold cyan]🐞 Debug:[/bold cyan]\n")
    console.print(safe("debug"))

    console.print("\n[bold cyan]🛠 Código corregido:[/bold cyan]\n")
    console.print(safe("fixed_code"))

    console.print("\n[bold cyan]🧪 Tests:[/bold cyan]\n")
    console.print(safe("tests"))

    console.print("\n[bold cyan]⭐ Review:[/bold cyan]\n")
    console.print(safe("review"))

    console.print("\n[bold cyan]📄 Documentación:[/bold cyan]\n")
    console.print(safe("documentation"))

    console.print("\n[bold magenta]⏱ Tiempo de ejecución:[/bold magenta]")
    console.print(f"{result.get('execution_time', 0):.2f} segundos")

    console.print("\n[bold green]✅ Proceso finalizado[/bold green]\n")


# =========================================================
# Entry point
# =========================================================

if __name__ == "__main__":
    main()