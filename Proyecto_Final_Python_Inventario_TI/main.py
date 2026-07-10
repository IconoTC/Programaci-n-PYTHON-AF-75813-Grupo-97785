"""Punto de entrada del proyecto final de Programación Python."""

from pathlib import Path
import argparse
import logging

from inventario_ti.analisis import enriquecer_equipos, filtrar_pendientes, obtener_resumen
from inventario_ti.io_datos import cargar_equipos, cargar_politica, guardar_json, guardar_texto
from inventario_ti.reportes import generar_informe

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
SALIDA_DIR = BASE_DIR / "salida"


def configurar_logging():
    """Configura el fichero de log de la ejecución."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=LOG_DIR / "proyecto.log",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        encoding="utf-8",
    )


def crear_parser():
    """Define los argumentos de línea de comandos del programa."""
    parser = argparse.ArgumentParser(description="Diagnóstico de inventario TI")
    parser.add_argument("--datos", default="datos/equipos.csv", help="Ruta del CSV de inventario")
    parser.add_argument("--politica", default="datos/politica_servicios.json", help="Ruta del JSON de política")
    return parser


def ejecutar(ruta_datos, ruta_politica):
    """Ejecuta el flujo completo de carga, análisis y generación de salidas."""
    logging.info("Inicio del proyecto final")

    politica = cargar_politica(ruta_politica)
    equipos = cargar_equipos(ruta_datos)
    logging.info("Equipos cargados: %s", len(equipos))

    equipos_enriquecidos = enriquecer_equipos(equipos, politica)
    resumen = obtener_resumen(equipos_enriquecidos)
    pendientes = filtrar_pendientes(equipos_enriquecidos)

    informe = generar_informe(resumen, pendientes)
    guardar_texto(SALIDA_DIR / "informe.txt", informe)
    guardar_json(SALIDA_DIR / "resumen.json", resumen)
    guardar_json(SALIDA_DIR / "equipos_clasificados.json", equipos_enriquecidos)

    logging.info("Informe generado en %s", SALIDA_DIR / "informe.txt")
    logging.info("Resumen generado en %s", SALIDA_DIR / "resumen.json")
    logging.info("Fin del proyecto final")

    return resumen, pendientes


def main():
    """Función principal invocada desde terminal."""
    configurar_logging()
    parser = crear_parser()
    args = parser.parse_args()

    try:
        resumen, pendientes = ejecutar(args.datos, args.politica)
    except (FileNotFoundError, ValueError) as error:
        logging.exception("Error controlado durante la ejecución")
        print(f"Error: {error}")
        return 1

    print("Proyecto ejecutado correctamente.")
    print(f"Total de equipos: {resumen['total_equipos']}")
    print(f"Equipos pendientes: {len(pendientes)}")
    print(f"Informe: {SALIDA_DIR / 'informe.txt'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
