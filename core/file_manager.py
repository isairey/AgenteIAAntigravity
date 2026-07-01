"""
=========================================================
Antigravity AI
File Manager
=========================================================

Responsabilidad:

- Manejo centralizado de archivos
- Lectura y escritura segura
- Creación de carpetas
- Guardado de outputs de agentes
- Utilidades de paths

Autor: ISAI
"""

from pathlib import Path
from typing import List


class FileManager:
    """
    Gestor de archivos del sistema Antigravity AI.
    """

    def __init__(self, base_path: str = "workspace"):

        self.base_path = Path(base_path)

        # Crear carpeta base si no existe
        self.base_path.mkdir(parents=True, exist_ok=True)

    # =====================================================
    # Leer archivo
    # =====================================================

    def read(self, path: str) -> str:
        """
        Lee un archivo.
        """

        full_path = self.base_path / path

        try:
            return full_path.read_text(encoding="utf-8")

        except Exception as e:
            return f"Error leyendo archivo: {str(e)}"

    # =====================================================
    # Escribir archivo
    # =====================================================

    def write(self, path: str, content: str) -> str:
        """
        Escribe contenido en un archivo.
        """

        full_path = self.base_path / path

        try:
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content, encoding="utf-8")

            return str(full_path)

        except Exception as e:
            return f"Error escribiendo archivo: {str(e)}"

    # =====================================================
    # Verificar existencia
    # =====================================================

    def exists(self, path: str) -> bool:
        """
        Verifica si un archivo existe.
        """

        full_path = self.base_path / path
        return full_path.exists()

    # =====================================================
    # Listar archivos
    # =====================================================

    def list_files(self, folder: str = "") -> List[str]:
        """
        Lista archivos en un directorio.
        """

        full_path = self.base_path / folder

        if not full_path.exists():
            return []

        return [
            str(f.relative_to(self.base_path))
            for f in full_path.rglob("*")
            if f.is_file()
        ]

    # =====================================================
    # Eliminar archivo
    # =====================================================

    def delete(self, path: str) -> bool:
        """
        Elimina un archivo.
        """

        full_path = self.base_path / path

        try:
            if full_path.exists():
                full_path.unlink()
                return True
            return False

        except Exception:
            return False

    # =====================================================
    # Guardar output de agente
    # =====================================================

    def save_agent_output(
        self,
        agent_name: str,
        content: str,
        filename: str
    ) -> str:
        """
        Guarda la salida de un agente.
        """

        path = f"outputs/{agent_name}/{filename}"

        return self.write(path, content)

    # =====================================================
    # Crear carpeta
    # =====================================================

    def create_folder(self, path: str) -> str:
        """
        Crea una carpeta.
        """

        full_path = self.base_path / path

        try:
            full_path.mkdir(parents=True, exist_ok=True)
            return str(full_path)

        except Exception as e:
            return f"Error creando carpeta: {str(e)}"

    # =====================================================
    # Obtener ruta absoluta
    # =====================================================

    def abs_path(self, path: str) -> str:
        """
        Devuelve ruta absoluta.
        """

        return str((self.base_path / path).resolve())