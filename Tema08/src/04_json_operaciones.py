"""
Tema 8 - Operaciones de entrada-salida
Laboratorio 4: operaciones con JSON.

Objetivo:
    Escribir y leer datos estructurados con json.dump() y json.load().
"""
import json
from pathlib import Path

carpeta = Path("Tema08/data")
carpeta.mkdir(parents=True, exist_ok=True)
ruta_json = carpeta / "servicios1.json"

print("=== 1. Crear datos estructurados en Python ===")
servicios = [
    {"servicio": "ssh", "puerto": 22, "estado": "OK"},
    {"servicio": "http", "puerto": 80, "estado": "OK"},
    {"servicio": "https", "puerto": 443, "estado": "ERROR"},
]
print(servicios)

print("\n=== 2. Escribir JSON con json.dump() ===")
try:
    with open(ruta_json, "w", encoding="utf-8") as filejson:
        json.dump(servicios, filejson, indent=4, ensure_ascii=False)
except OSError as error:
    print("[ERROR] No se pudo escribir el archivo:", error)
else:
    print("Fichero guardado en:", ruta_json)

print("\n=== 3. Leer JSON con json.load() ===")
try:
    with open(ruta_json, "r", encoding="utf-8") as filejson:
        datos = json.load(filejson)
    for fila in datos:
        print(f"Servicio: {fila['servicio']} -> Puerto: {fila['puerto']} [{fila['estado']}]")
except FileNotFoundError:
    print(f"[CRÍTICO] El archivo no existe: {ruta_json}")
except json.JSONDecodeError:
    print("[CRÍTICO] El archivo JSON está corrupto o tiene errores.")

print("\n=== 4. Crear JSON de configuración ===")
config = {
    "aplicacion": "monitor-servicios",
    "entorno": "laboratorio",
    "reintentos": 3,
    "alertas": {"email": True, "canal": "soporte"},
}
ruta_config = carpeta / "configuracion.json"
with open(ruta_config, "w", encoding="utf-8") as filejson:
    json.dump(config, filejson, indent=4, ensure_ascii=False)
print("Configuración guardada:", ruta_config)

print("\n=== 5. Leer configuración y usar valores ===")
with open(ruta_config, "r", encoding="utf-8") as filejson:
    config_leida = json.load(filejson)
print("Aplicación:", config_leida["aplicacion"])
print("Canal de alertas:", config_leida["alertas"]["canal"])
