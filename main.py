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

from core.orchestrator import Orchestrator
from rich.console import Console


def main():
    """
    Ejecuta el sistema multiagente completo.
    """

    console = Console()

    console.print("\n[bold cyan]==============================[/bold cyan]")
    console.print("[bold cyan]   🚀 ANTIGRAVITY AI START   [/bold cyan]")
    console.print("[bold cyan]==============================[/bold cyan]\n")

    # =====================================================
    # Crear Orchestrator
    # =====================================================

    orchestrator = Orchestrator()

    # =====================================================
    # Input del usuario
    # =====================================================

    request = input("💡 Describe lo que quieres generar:\n> ")

    # =====================================================
    # Ejecutar sistema completo
    # =====================================================

    console.print("\n[bold yellow]⏳ Ejecutando pipeline multiagente...[/bold yellow]\n")

    result = orchestrator.run(request)

    # =====================================================
    # Mostrar resultados
    # =====================================================

    console.print("\n[bold green]==============================[/bold green]")
    console.print("[bold green]        RESULTADOS           [/bold green]")
    console.print("[bold green]==============================[/bold green]\n")

    console.print("\n[bold cyan]📌 Código generado:[/bold cyan]\n")
    console.print(result["code"])

    console.print("\n[bold cyan]🔍 Análisis:[/bold cyan]\n")
    console.print(result["analysis"])

    console.print("\n[bold cyan]🔐 Seguridad:[/bold cyan]\n")
    console.print(result["security"])

    console.print("\n[bold cyan]🐞 Debug:[/bold cyan]\n")
    console.print(result["debug"])

    console.print("\n[bold cyan]🛠 Código corregido:[/bold cyan]\n")
    console.print(result["fixed_code"])

    console.print("\n[bold cyan]🧪 Tests:[/bold cyan]\n")
    console.print(result["tests"])

    console.print("\n[bold cyan]⭐ Review:[/bold cyan]\n")
    console.print(result["review"])

    console.print("\n[bold cyan]📄 Documentación:[/bold cyan]\n")
    console.print(result["documentation"])

    console.print("\n[bold magenta]⏱ Tiempo de ejecución:[/bold magenta]")
    console.print(f"{result['execution_time']:.2f} segundos")

    console.print("\n[bold green]✅ Proceso finalizado[/bold green]\n")


# =========================================================
# Entry point
# =========================================================

if __name__ == "__main__":
    main()