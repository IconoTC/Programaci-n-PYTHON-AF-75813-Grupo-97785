"""
Tema 10 - Biblioteca estándar
Laboratorio 4: rutas y ficheros con pathlib, shutil y glob.

Objetivo:
    Crear ficheros de configuración, copiarlos a una carpeta de backup
    y localizar ficheros por patrón.
"""

from pathlib import Path
import shutil
import glob


base_dir = Path(__file__).resolve().parent.parent
data_dir = base_dir / "data"
backup_dir = base_dir / "backup"

print("=== 1. Preparar directorios ===")
data_dir.mkdir(parents=True, exist_ok=True)
backup_dir.mkdir(parents=True, exist_ok=True)
print("Data  :", data_dir)
print("Backup:", backup_dir)

print("\n=== 2. Crear ficheros JSON de ejemplo ===")
(data_dir / "config1.json").write_text('{"servicio": "ssh", "estado": "activo"}\n', encoding="utf-8")
(data_dir / "config2.json").write_text('{"servicio": "nginx", "estado": "activo"}\n', encoding="utf-8")
(data_dir / "notas.txt").write_text("Fichero auxiliar\n", encoding="utf-8")
print("Ficheros creados en:", data_dir)

print("\n=== 3. Copiar el directorio data a backup/data_copia ===")
destino_copia = backup_dir / "data_copia"
shutil.copytree(data_dir, destino_copia, dirs_exist_ok=True)
print("Copia creada en:", destino_copia)

print("\n=== 4. Buscar ficheros JSON con glob ===")
patron = str(destino_copia / "*.json")
archivos = glob.glob(patron)

for archivo in archivos:
    print("JSON respaldado:", archivo)
