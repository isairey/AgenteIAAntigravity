from core.orchestrator import AntigravityOrchestrator

if __name__ == "__main__":
    system = AntigravityOrchestrator()

    task = "Crea una API en FastAPI que gestione usuarios con login y registro."

    result = system.run(task)

    print("\n===== CÓDIGO ORIGINAL =====\n")
    print(result["original_code"])

    print("\n===== ANÁLISIS =====\n")
    print(result["analysis"])

    print("\n===== SEGURIDAD =====\n")
    print(result["security"])

    print("\n===== CÓDIGO FINAL CORREGIDO =====\n")
    print(result["fixed_code"])