"""
Tema 8 - Operaciones de entrada-salida
Laboratorio 7: ejercicio integrado CSV a JSON.

Objetivo:
    Procesar un CSV de inventario de empresa, normalizar datos, validar
    puertos, separar registros rechazados y exportar el resultado a JSON.
"""
import csv
import json
from pathlib import Path

carpeta = Path("Tema08/data")
carpeta.mkdir(parents=True, exist_ok=True)
entrada_csv = carpeta / "inventario_empresa.csv"
salida_json = carpeta / "inventario_empresa_normalizado.json"
salida_rechazados = carpeta / "inventario_empresa_rechazados.csv"

print("=== 1. Comprobar fichero de entrada ===")
if not entrada_csv.exists():
    raise FileNotFoundError(f"No existe el fichero de entrada: {entrada_csv}")
print("Entrada:", entrada_csv)

print("\n=== 2. Funciones auxiliares ===")
def normalizar_texto(valor):
    """Limpia espacios y convierte texto a minúsculas."""
    return valor.strip().lower()

def validar_puerto(puerto_txt):
    """Convierte y valida un puerto."""
    puerto = int(puerto_txt)
    if not 1 <= puerto <= 65535:
        raise ValueError("Puerto fuera de rango")
    return puerto

def normalizar_fila(fila):
    """Normaliza una fila del CSV de inventario."""
    return {
        "departamento": normalizar_texto(fila["departamento"]),
        "servidor": normalizar_texto(fila["servidor"]),
        "servicio": normalizar_texto(fila["servicio"]),
        "puerto": validar_puerto(fila["puerto"].strip()),
        "estado": normalizar_texto(fila["estado"]),
        "criticidad": normalizar_texto(fila["criticidad"]),
    }

print("Funciones definidas.")

print("\n=== 3. Leer, normalizar y validar CSV ===")
registros_validos = []
registros_rechazados = []
with open(entrada_csv, "r", newline="", encoding="utf-8") as filecsv:
    lector = csv.DictReader(filecsv)
    for numero_linea, fila in enumerate(lector, start=2):
        try:
            normalizada = normalizar_fila(fila)
        except ValueError as error:
            rechazada = dict(fila)
            rechazada["linea"] = numero_linea
            rechazada["motivo"] = str(error)
            registros_rechazados.append(rechazada)
        else:
            registros_validos.append(normalizada)

print("Registros válidos:", len(registros_validos))
print("Registros rechazados:", len(registros_rechazados))

print("\n=== 4. Construir estructura JSON final ===")
salida = {
    "origen": str(entrada_csv),
    "total_validos": len(registros_validos),
    "total_rechazados": len(registros_rechazados),
    "servicios": registros_validos,
}
print(json.dumps(salida, indent=4, ensure_ascii=False))

print("\n=== 5. Escribir JSON normalizado ===")
with open(salida_json, "w", encoding="utf-8") as filejson:
    json.dump(salida, filejson, indent=4, ensure_ascii=False)
print("JSON generado:", salida_json)

print("\n=== 6. Escribir CSV de rechazados ===")
campos_rechazados = ["linea", "departamento", "servidor", "servicio", "puerto", "estado", "criticidad", "motivo"]
with open(salida_rechazados, "w", newline="", encoding="utf-8") as filecsv:
    escritor = csv.DictWriter(filecsv, fieldnames=campos_rechazados)
    escritor.writeheader()
    escritor.writerows(registros_rechazados)
print("CSV de rechazados generado:", salida_rechazados)

print("\n=== 7. Leer el JSON generado para comprobarlo ===")
with open(salida_json, "r", encoding="utf-8") as filejson:
    comprobacion = json.load(filejson)

for servicio in comprobacion["servicios"]:
    print(f"{servicio['servidor']} -> {servicio['servicio']}:{servicio['puerto']} [{servicio['estado']}]")
