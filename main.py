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
    # Verificar API KEY antes de iniciar
    # =====================================================

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        console.print("[bold red]❌ ERROR: No se encontró GEMINI_API_KEY en .env[/bold red]")
        console.print("[yellow]💡 Agrega tu API key en el archivo .env[/yellow]\n")
        return

    # =====================================================
    # Crear Orchestrator
    # =====================================================

    orchestrator = Orchestrator()

    # =====================================================
    # Input del usuario
    # =====================================================

    request = input("💡 Describe lo que quieres generar:\n> ")

    if not request.strip():
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
    # Mostrar resultados
    # =====================================================

    console.print("\n[bold green]==============================[/bold green]")
    console.print("[bold green]        RESULTADOS           [/bold green]")
    console.print("[bold green]==============================[/bold green]\n")

    console.print("\n[bold cyan]📌 Código generado:[/bold cyan]\n")
    console.print(result.get("code", ""))

    console.print("\n[bold cyan]🔍 Análisis:[/bold cyan]\n")
    console.print(result.get("analysis", ""))

    console.print("\n[bold cyan]🔐 Seguridad:[/bold cyan]\n")
    console.print(result.get("security", ""))

    console.print("\n[bold cyan]🐞 Debug:[/bold cyan]\n")
    console.print(result.get("debug", ""))

    console.print("\n[bold cyan]🛠 Código corregido:[/bold cyan]\n")
    console.print(result.get("fixed_code", ""))

    console.print("\n[bold cyan]🧪 Tests:[/bold cyan]\n")
    console.print(result.get("tests", ""))

    console.print("\n[bold cyan]⭐ Review:[/bold cyan]\n")
    console.print(result.get("review", ""))

    console.print("\n[bold cyan]📄 Documentación:[/bold cyan]\n")
    console.print(result.get("documentation", ""))

    console.print("\n[bold magenta]⏱ Tiempo de ejecución:[/bold magenta]")
    console.print(f"{result.get('execution_time', 0):.2f} segundos")

    console.print("\n[bold green]✅ Proceso finalizado[/bold green]\n")


# =========================================================
# Entry point
# =========================================================

if __name__ == "__main__":
    main()