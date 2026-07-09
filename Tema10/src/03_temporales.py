"""
Tema 10 - Biblioteca estándar
Laboratorio 5: ficheros y directorios temporales con tempfile.

Objetivo:
    Crear un directorio temporal seguro para trabajo intermedio y comprobar
    que se limpia automáticamente al salir del contexto.
"""

import tempfile
from pathlib import Path


base_dir = Path(__file__).resolve().parent.parent
data_dir = base_dir / "data"
data_dir.mkdir(parents=True, exist_ok=True)

print("=== Crear directorio temporal controlado ===")
with tempfile.TemporaryDirectory(dir=data_dir) as tmp_dir:
    directorio = Path(tmp_dir)
    archivo = directorio / "dump_db.sql"

    print("Temporal creado:", directorio)
    archivo.write_text("SELECT * FROM usuarios;\n", encoding="utf-8")

    print("Archivo temporal:", archivo)
    print("Existe dentro del contexto:", archivo.exists())
    print("Contenido:", archivo.read_text(encoding="utf-8").strip())

print("\n=== Después del contexto ===")
print("El directorio temporal sigue existiendo:", directorio.exists())
