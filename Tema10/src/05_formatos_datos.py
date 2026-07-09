"""
Tema 10 - Biblioteca estándar
Laboratorio 7: formatos de datos con csv, json, configparser y tomllib.

Objetivo:
    Crear y leer formatos habituales de intercambio y configuración sin usar
    paquetes externos.
"""

import csv
import json
import configparser
import tomllib
from pathlib import Path


base_dir = Path(__file__).resolve().parent.parent
data_dir = base_dir / "data"
data_dir.mkdir(parents=True, exist_ok=True)

print("=== 1. CSV: escribir y leer datos tabulares ===")
ruta_csv = data_dir / "servicios.csv"
filas = [
    {"servicio": "ssh", "puerto": 22, "estado": "OK"},
    {"servicio": "nginx", "puerto": 443, "estado": "OK"},
    {"servicio": "api", "puerto": 8080, "estado": "ERROR"},
]

with open(ruta_csv, "w", newline="", encoding="utf-8") as fichero:
    escritor = csv.DictWriter(fichero, fieldnames=["servicio", "puerto", "estado"])
    escritor.writeheader()
    escritor.writerows(filas)

with open(ruta_csv, "r", newline="", encoding="utf-8") as fichero:
    lector = csv.DictReader(fichero)
    for fila in lector:
        print(f"{fila['servicio']} -> {fila['puerto']} [{fila['estado']}]")

print("\n=== 2. JSON: escribir y leer datos estructurados ===")
ruta_json = data_dir / "servicios.json"
ruta_json.write_text(json.dumps(filas, indent=4, ensure_ascii=False), encoding="utf-8")

servicios = json.loads(ruta_json.read_text(encoding="utf-8"))
print("Servicios cargados desde JSON:", len(servicios))

print("\n=== 3. INI con configparser ===")
ruta_ini = data_dir / "database.ini"
ruta_ini.write_text(
    "[mysqld]\n"
    "host = localhost\n"
    "port = 3306\n"
    "user = soporte\n",
    encoding="utf-8",
)

config_ini = configparser.ConfigParser()
config_ini.read(ruta_ini, encoding="utf-8")
print("Puerto extraído de INI:", config_ini["mysqld"]["port"])

print("\n=== 4. TOML con tomllib ===")
ruta_toml = data_dir / "app_config.toml"
ruta_toml.write_text(
    "[server]\n"
    "host = '127.0.0.1'\n"
    "port = 8000\n"
    "debug_mode = true\n",
    encoding="utf-8",
)

with open(ruta_toml, "rb") as fichero:
    config_toml = tomllib.load(fichero)

print("Modo debug de TOML:", config_toml["server"]["debug_mode"])
