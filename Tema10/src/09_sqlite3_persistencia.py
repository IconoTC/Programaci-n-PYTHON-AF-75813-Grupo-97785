"""
Tema 10 - Biblioteca estándar
Laboratorio 11: persistencia ligera con sqlite3.

Objetivo:
    Crear una base SQLite local, insertar registros y consultarlos con SQL.
"""

import sqlite3
from pathlib import Path


base_dir = Path(__file__).resolve().parent.parent
data_dir = base_dir / "data"
data_dir.mkdir(parents=True, exist_ok=True)
db_file = data_dir / "inventario.db"

print("=== Crear o abrir base SQLite ===")
bd = sqlite3.connect(db_file)

bd.execute("""
CREATE TABLE IF NOT EXISTS nodos (
    host TEXT,
    ip TEXT,
    rol TEXT
)
""")

# Limpiamos la tabla para que el script sea reproducible.
bd.execute("DELETE FROM nodos")

datos = [
    ("web-01", "10.0.1.10", "frontend"),
    ("db-01", "10.0.1.20", "backend"),
    ("cache-01", "10.0.1.30", "redis"),
]

bd.executemany("INSERT INTO nodos VALUES (?, ?, ?)", datos)
bd.commit()

print("Registros insertados:", len(datos))

print("\n=== Consultar nodos backend ===")
for fila in bd.execute("SELECT host, ip FROM nodos WHERE rol = ?", ("backend",)):
    print(f"Servidor crítico: {fila[0]} localizado en {fila[1]}")

bd.close()
print("Base de datos:", db_file)
