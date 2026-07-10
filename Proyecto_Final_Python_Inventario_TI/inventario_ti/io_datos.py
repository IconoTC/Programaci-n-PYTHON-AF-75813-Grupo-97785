"""Entrada y salida de datos del proyecto."""

from pathlib import Path
import csv
import json

from .modelos import Equipo
from .validaciones import (
    convertir_entero,
    normalizar_estado,
    normalizar_servicio,
    normalizar_texto,
)


def cargar_politica(ruta):
    """Carga el fichero JSON con la política de validación y umbrales."""
    ruta = Path(ruta)
    try:
        with ruta.open("r", encoding="utf-8") as fichero:
            return json.load(fichero)
    except FileNotFoundError as error:
        raise FileNotFoundError(f"No se encontró el fichero de política: {ruta}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"El fichero de política no contiene JSON válido: {ruta}") from error


def _equipo_desde_fila(fila, numero_linea):
    """Convierte una fila CSV en una instancia de Equipo."""
    campos_obligatorios = [
        "id", "nombre", "tipo", "sistema", "ip", "servicio", "puerto",
        "estado", "cpu", "memoria", "disco", "entorno", "responsable",
    ]

    for campo in campos_obligatorios:
        if campo not in fila or fila[campo] == "":
            raise ValueError(f"Línea {numero_linea}: falta el campo obligatorio {campo!r}")

    return Equipo(
        identificador=convertir_entero(fila["id"], "id"),
        nombre=normalizar_texto(fila["nombre"]),
        tipo=normalizar_texto(fila["tipo"]).lower(),
        sistema=normalizar_texto(fila["sistema"]),
        ip=normalizar_texto(fila["ip"]),
        servicio=normalizar_servicio(fila["servicio"]),
        puerto=convertir_entero(fila["puerto"], "puerto"),
        estado=normalizar_estado(fila["estado"]),
        cpu=convertir_entero(fila["cpu"], "cpu"),
        memoria=convertir_entero(fila["memoria"], "memoria"),
        disco=convertir_entero(fila["disco"], "disco"),
        entorno=normalizar_texto(fila["entorno"]).lower(),
        responsable=normalizar_texto(fila["responsable"]),
    )


def cargar_equipos(ruta_csv):
    """Carga el inventario CSV y devuelve una lista de objetos Equipo."""
    ruta_csv = Path(ruta_csv)
    equipos = []

    try:
        with ruta_csv.open("r", encoding="utf-8", newline="") as fichero:
            lector = csv.DictReader(fichero)
            for numero_linea, fila in enumerate(lector, start=2):
                equipos.append(_equipo_desde_fila(fila, numero_linea))
    except FileNotFoundError as error:
        raise FileNotFoundError(f"No se encontró el fichero CSV: {ruta_csv}") from error

    return equipos


def guardar_json(ruta, datos):
    """Guarda datos serializables en JSON con indentación legible."""
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with ruta.open("w", encoding="utf-8") as fichero:
        json.dump(datos, fichero, ensure_ascii=False, indent=2)


def guardar_texto(ruta, texto):
    """Guarda un texto en disco creando antes el directorio destino."""
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto, encoding="utf-8")
