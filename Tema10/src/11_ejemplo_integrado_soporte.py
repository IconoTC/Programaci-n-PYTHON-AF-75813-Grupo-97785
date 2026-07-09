"""
Tema 10 - Biblioteca estándar
Laboratorio 15: ejemplo práctico integrado.

Objetivo:
    Combinar varios módulos estándar en un script de soporte:
        - platform, sys y os: contexto de ejecución.
        - pathlib: rutas del proyecto.
        - json: salida estructurada.
        - logging: registro operativo.
        - datetime: marcas de tiempo.
        - collections.Counter: resumen de estados.
        - hashlib: huella del reporte generado.
        - shutil: copia de respaldo del JSON.
"""

import os
import sys
import json
import shutil
import hashlib
import logging
import platform
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter


base_dir = Path(__file__).resolve().parent.parent
data_dir = base_dir / "data"
output_dir = base_dir / "output"
backup_dir = base_dir / "backup"
log_dir = base_dir / "logs"

for directorio in (data_dir, output_dir, backup_dir, log_dir):
    directorio.mkdir(parents=True, exist_ok=True)

log_file = log_dir / "operacion_integrada.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True,
)


def obtener_contexto():
    """Devuelve información básica del entorno de ejecución."""
    return {
        "python": sys.version.split()[0],
        "ejecutable": sys.executable,
        "sistema": platform.system(),
        "release": platform.release(),
        "maquina": platform.machine(),
        "usuario": os.environ.get("USER") or os.environ.get("USERNAME") or "desconocido",
        "directorio_actual": os.getcwd(),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


def puerto_valido(puerto):
    """Valida un puerto TCP/UDP."""
    return 1 <= puerto <= 65535


def normalizar_servicios(servicios):
    """Normaliza registros de servicio y añade estado de validación."""
    normalizados = []

    for servicio in servicios:
        nombre = servicio["nombre"].strip().lower()
        puerto = servicio["puerto"]
        activo = servicio["activo"]

        if activo and puerto_valido(puerto):
            estado = "OK"
        elif not puerto_valido(puerto):
            estado = "PUERTO_INVALIDO"
        else:
            estado = "DETENIDO"

        normalizados.append({
            "nombre": nombre,
            "host": servicio["host"],
            "puerto": puerto,
            "activo": activo,
            "estado": estado,
        })

    return normalizados


def calcular_huella(ruta):
    """Calcula SHA-256 del fichero generado."""
    contenido = ruta.read_bytes()
    return hashlib.sha256(contenido).hexdigest()


def main():
    """Ejecuta la operación integrada."""
    logging.info("Inicio de operación integrada.")

    servicios = [
        {"nombre": " SSH ", "host": "srv-web-01", "puerto": 22, "activo": True},
        {"nombre": "NGINX", "host": "srv-web-01", "puerto": 443, "activo": True},
        {"nombre": "api", "host": "srv-app-01", "puerto": 8080, "activo": False},
        {"nombre": "backup", "host": "srv-bkp-01", "puerto": 70000, "activo": True},
    ]

    contexto = obtener_contexto()
    registros = normalizar_servicios(servicios)
    resumen = Counter(registro["estado"] for registro in registros)

    salida = {
        "contexto": contexto,
        "total_servicios": len(registros),
        "resumen_estados": dict(resumen),
        "servicios": registros,
    }

    ruta_json = output_dir / "reporte_soporte.json"
    ruta_json.write_text(json.dumps(salida, indent=4, ensure_ascii=False), encoding="utf-8")

    huella = calcular_huella(ruta_json)
    copia = backup_dir / "reporte_soporte.json"
    shutil.copy2(ruta_json, copia)

    logging.info("Reporte generado: %s", ruta_json)
    logging.info("Backup generado: %s", copia)
    logging.info("SHA-256 del reporte: %s", huella)
    logging.info("Fin de operación integrada.")

    print("=== Reporte integrado generado ===")
    print("JSON     :", ruta_json)
    print("Backup   :", copia)
    print("Log      :", log_file)
    print("SHA-256  :", huella)
    print("Resumen  :", dict(resumen))


if __name__ == "__main__":
    main()
