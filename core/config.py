"""
=========================================================
Antigravity AI
Configuración General del Sistema
=========================================================

Este módulo carga y valida toda la configuración
del proyecto desde el archivo .env.

Autor: ISAI
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# ------------------------------------------------------
# Directorio raíz del proyecto
# ------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------------------------
# Cargar .env
# ------------------------------------------------------

load_dotenv(ROOT_DIR / ".env")

# ======================================================
# Configuración General
# ======================================================

APP_NAME = os.getenv("APP_NAME", "Antigravity AI")

DEBUG = os.getenv("DEBUG", "True").lower() == "true"

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# ======================================================
# Gemini
# ======================================================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "gemini-2.5-flash"
)

TEMPERATURE = float(
    os.getenv(
        "TEMPERATURE",
        "0.2"
    )
)

TOP_P = float(
    os.getenv(
        "TOP_P",
        "0.95"
    )
)

TOP_K = int(
    os.getenv(
        "TOP_K",
        "40"
    )
)

MAX_OUTPUT_TOKENS = int(
    os.getenv(
        "MAX_OUTPUT_TOKENS",
        "8192"
    )
)

# ======================================================
# Memoria
# ======================================================

MEMORY_FILE = ROOT_DIR / os.getenv(
    "MEMORY_FILE",
    "memory/history.json"
)

# ======================================================
# Carpetas
# ======================================================

AGENTS_FOLDER = ROOT_DIR / "agents"

TOOLS_FOLDER = ROOT_DIR / "tools"

CORE_FOLDER = ROOT_DIR / "core"

MEMORY_FOLDER = ROOT_DIR / "memory"

LOGS_FOLDER = ROOT_DIR / "logs"

TESTS_FOLDER = ROOT_DIR / "tests"

# ======================================================
# Crear carpetas automáticamente
# ======================================================

for folder in [
    MEMORY_FOLDER,
    LOGS_FOLDER,
    TESTS_FOLDER,
]:
    folder.mkdir(
        exist_ok=True,
        parents=True
    )

# ======================================================
# Validaciones
# ======================================================

if not GOOGLE_API_KEY:
    raise RuntimeError(
        """
No se encontró GOOGLE_API_KEY.

Crea un archivo .env con:

GOOGLE_API_KEY=TU_API_KEY
MODEL_NAME=gemini-2.5-flash
"""
    )

# ======================================================
# Configuración del modelo
# ======================================================

MODEL_CONFIG = {
    "temperature": TEMPERATURE,
    "top_p": TOP_P,
    "top_k": TOP_K,
    "max_output_tokens": MAX_OUTPUT_TOKENS,
}

# ======================================================
# Funciones auxiliares
# ======================================================

def print_configuration():
    """
    Muestra toda la configuración cargada.
    """

    print("\n==============================")
    print(APP_NAME)
    print("==============================\n")

    print(f"Debug: {DEBUG}")
    print(f"Modelo: {MODEL_NAME}")
    print(f"Temperatura: {TEMPERATURE}")
    print(f"Top P: {TOP_P}")
    print(f"Top K: {TOP_K}")
    print(f"Max Tokens: {MAX_OUTPUT_TOKENS}")

    print()

    print(f"Memory: {MEMORY_FILE}")

    print(f"Agents: {AGENTS_FOLDER}")

    print(f"Tools: {TOOLS_FOLDER}")

    print("==============================\n")


def get_model_config():
    """
    Devuelve la configuración del modelo.
    """

    return MODEL_CONFIG.copy()


def is_debug():
    """
    Indica si la aplicación está en modo debug.
    """

    return DEBUG


def get_memory_file():
    """
    Ruta del archivo de memoria.
    """

    return MEMORY_FILE


def get_logs_folder():
    return LOGS_FOLDER


def get_tests_folder():
    return TESTS_FOLDER


def get_agents_folder():
    return AGENTS_FOLDER


def get_tools_folder():
    return TOOLS_FOLDER


def get_root_folder():
    return ROOT_DIR


def get_app_name():
    return APP_NAME