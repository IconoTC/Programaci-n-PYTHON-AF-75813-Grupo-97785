"""
Tema 8 - Operaciones de entrada-salida
Laboratorio 1: operaciones previas con pathlib.Path.

Objetivo:
    Practicar creación de rutas, comprobaciones, creación de directorios,
    lectura/escritura simple, renombrado, eliminación y búsqueda por patrón.
"""
from pathlib import Path

print("=== 1. Crear rutas con Path ===")
carpeta = Path("Tema08/data")
ruta = carpeta / "pathlib_demo.txt"
print("Carpeta relativa:", carpeta)
print("Ruta relativa:", ruta)
print("Ruta absoluta:", ruta.resolve())

print("\n=== 2. Crear directorio si no existe ===")
carpeta.mkdir(parents=True, exist_ok=True)
print("Carpeta existe:", carpeta.exists())
print("Carpeta es directorio:", carpeta.is_dir())
print("Fichero existe antes de escribir:", ruta.exists())

print("\n=== 3. Escribir y leer texto con métodos de Path ===")
ruta.write_text("ssh:22\nnginx:443\n", encoding="utf-8")
print("Fichero existe después de escribir:", ruta.exists())
print("Es fichero:", ruta.is_file())
print("Extensión:", ruta.suffix)
print("Contenido:")
print(ruta.read_text(encoding="utf-8").strip())

print("\n=== 4. Cambiar nombre con with_name() y rename() ===")
nueva_ruta = ruta.with_name("pathlib_demo_renamed.txt")
if nueva_ruta.exists():
    nueva_ruta.unlink()
ruta.rename(nueva_ruta)
print("Ruta original existe:", ruta.exists())
print("Ruta renombrada existe:", nueva_ruta.exists())

print("\n=== 5. Limpiar fichero temporal ===")
if nueva_ruta.exists():
    nueva_ruta.unlink()
print("Ruta renombrada existe tras unlink:", nueva_ruta.exists())

print("\n=== 6. Listar ficheros CSV del directorio data ===")
for fichero in carpeta.glob("*.csv"):
    print("CSV encontrado:", fichero.name)
