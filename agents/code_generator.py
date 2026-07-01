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
    Agente encargado de generar código.
    """

    def __init__(self):
        super().__init__(
            name="Code Generator",
            description="Genera código profesional."
        )

    # =====================================================
    # Generación principal
    # =====================================================

    def run(
        self,
        request: str
    ) -> str:
        """
        Genera código a partir de una petición.
        """

        prompt = f"""
{CODE_GENERATOR_PROMPT}

Solicitud:

{request}

Instrucciones:

- Genera código limpio.
- Usa buenas prácticas.
- Sigue SOLID.
- Usa Clean Code.
- Agrega comentarios únicamente cuando sean necesarios.
- Devuelve únicamente el código.
"""

        return self.generate(prompt)

    # =====================================================
    # Proyecto completo
    # =====================================================

    def generate_project(
        self,
        description: str
    ) -> str:

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

Devuelve todo el proyecto.
"""

        return self.generate(prompt)

    # =====================================================
    # Clase
    # =====================================================

    def generate_class(
        self,
        description: str
    ) -> str:

        prompt = f"""
Genera una clase en Python.

Descripción:

{description}

Debe incluir:

- Constructor
- Métodos
- Docstrings
- Tipado
- Buenas prácticas

Devuelve únicamente el código.
"""

        return self.generate(prompt)

    # =====================================================
    # Función
    # =====================================================

    def generate_function(
        self,
        description: str
    ) -> str:

        prompt = f"""
Genera una función en Python.

Descripción:

{description}

Debe incluir:

- Tipado
- Docstring
- Validaciones
- Manejo de errores

Devuelve únicamente el código.
"""

        return self.generate(prompt)

    # =====================================================
    # API FastAPI
    # =====================================================

    def generate_api(
        self,
        description: str
    ) -> str:

        prompt = f"""
Genera una API con FastAPI.

Descripción:

{description}

Incluye:

- Endpoints
- Validaciones
- Modelos Pydantic
- Manejo de errores

Devuelve únicamente el código.
"""

        return self.generate(prompt)

    # =====================================================
    # Base de datos
    # =====================================================

    def generate_database(
        self,
        description: str
    ) -> str:

        prompt = f"""
Diseña la base de datos.

Descripción:

{description}

Incluye:

- Tablas
- Relaciones
- Índices
- Buenas prácticas

Devuelve SQL o modelos ORM.
"""

        return self.generate(prompt)

    # =====================================================
    # Refactor
    # =====================================================

    def refactor(
        self,
        code: str
    ) -> str:

        prompt = f"""
Refactoriza el siguiente código.

```python
{code}