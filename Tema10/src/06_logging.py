"""
Tema 10 - Biblioteca estándar
Laboratorio 8: registros operativos con logging.

Objetivo:
    Registrar información técnica en un fichero log y mostrar al usuario
    mensajes controlados por pantalla.
"""

from pathlib import Path
import logging


base_dir = Path(__file__).resolve().parent.parent
log_dir = base_dir / "logs"
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / "soporte.log"

# force=True permite reconfigurar logging si el script se relanza desde un entorno interactivo.
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True,
)

print("=== Registrar operación ===")
logging.info("Inicio de comprobación de infraestructura.")
logging.warning("Latencia alta detectada en el servicio API.")

try:
    raise ConnectionRefusedError("Conexión rechazada por el puerto 5432")
except ConnectionRefusedError as error:
    logging.error("Fallo en nodo srv-db-01: %s", error)
    print("Error: La base de datos no está disponible en este momento.")

print("Log generado en:", log_file)
print("Últimas líneas del log:")
print(log_file.read_text(encoding="utf-8").strip().splitlines()[-3:])
