"""
=========================================================
Antigravity AI
Code Generator Agent
=========================================================

Genera proyectos completos utilizando Google Gemini.

Responsabilidades:

- Generar código
- Crear proyectos completos
- Crear clases
- Crear funciones
- Crear APIs
- Crear documentación
- Refactorizar código
- Explicar código

Autor: ISAI
"""

from core.base_agent import BaseAgent
from core.prompts import CODE_GENERATOR_PROMPT


class CodeGeneratorAgent(BaseAgent):
    """
    Agente encargado de generar código utilizando Gemini.
    """

    def __init__(self):
        super().__init__(
            name="Code Generator",
            description="Genera código profesional."
        )

    # =====================================================
    # Utilidad privada
    # =====================================================

    def _execute(self, prompt: str) -> str:
        """
        Envía el prompt al modelo y valida la respuesta.
        """

        response = self.generate(prompt)

        if response is None:
            return "Error: Gemini no devolvió respuesta."

        response = str(response).strip()

        if response == "":
            return "Error: Respuesta vacía."

        return response

    # =====================================================
    # Generación principal
    # =====================================================

    def run(self, request: str) -> str:
        """
        Genera código a partir de una solicitud.
        """

        prompt = f"""
{CODE_GENERATOR_PROMPT}

Solicitud:

{request}

Instrucciones:

- Genera una solución profesional.
- Usa buenas prácticas.
- Sigue SOLID.
- Sigue Clean Code.
- Agrega comentarios únicamente cuando sean necesarios.
- Si son varios archivos, indica el nombre antes de cada uno.
- Devuelve únicamente el código generado.
"""

        return self._execute(prompt)

    # =====================================================
    # Proyecto completo
    # =====================================================

    def generate_project(self, description: str) -> str:

        prompt = f"""
Genera un proyecto profesional.

Descripción:

{description}

Incluye:

- Arquitectura
- Carpetas
- Archivos
- Código completo
- README
- Dependencias

Devuelve el proyecto completo.
"""

        return self._execute(prompt)

    # =====================================================
    # Clase
    # =====================================================

    def generate_class(self, description: str) -> str:

        prompt = f"""
Genera una clase.

Descripción:

{description}

Debe incluir:

- Constructor
- Métodos
- Tipado
- Docstrings
- Buenas prácticas

Devuelve únicamente el código.
"""

        return self._execute(prompt)

    # =====================================================
    # Función
    # =====================================================

    def generate_function(self, description: str) -> str:

        prompt = f"""
Genera una función.

Descripción:

{description}

Debe incluir:

- Tipado
- Docstring
- Validaciones
- Manejo de errores

Devuelve únicamente el código.
"""

        return self._execute(prompt)

    # =====================================================
    # API
    # =====================================================

    def generate_api(self, description: str) -> str:

        prompt = f"""
Genera una API profesional con FastAPI.

Descripción:

{description}

Incluye:

- Endpoints
- Modelos Pydantic
- Validaciones
- Manejo de errores
- Organización por módulos

Devuelve únicamente el código.
"""

        return self._execute(prompt)

    # =====================================================
    # Base de datos
    # =====================================================

    def generate_database(self, description: str) -> str:

        prompt = f"""
Diseña una base de datos.

Descripción:

{description}

Incluye:

- Tablas
- Relaciones
- Índices
- Restricciones
- Buenas prácticas

Devuelve SQL o modelos ORM.
"""

        return self._execute(prompt)

    # =====================================================
    # Refactor
    # =====================================================

def refactor(self, code: str) -> str:
    """
    Refactoriza código existente.
    """

    prompt = f"""
Refactoriza el siguiente código:

{code}

Aplica:

- Clean Code.
- Principios SOLID.
- Mejora el rendimiento.
- Elimina código duplicado.
- Corrige malas prácticas.
- Mantén la misma funcionalidad.

Devuelve únicamente el código refactorizado.
"""

    return self._execute(prompt)