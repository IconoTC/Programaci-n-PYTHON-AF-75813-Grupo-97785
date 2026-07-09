"""
Tema 8 - Operaciones de entrada-salida
Laboratorio 3: operaciones con CSV.

Objetivo:
    Escribir y leer CSV con writer, DictWriter, reader y DictReader.
    Normalizar datos desde data/servicios3.csv.
"""
import csv
from pathlib import Path

carpeta = Path("Tema08/data")
carpeta.mkdir(parents=True, exist_ok=True)

print("=== 1. Escribir CSV con csv.writer ===")
ruta_csv1 = carpeta / "servicios1.csv"
with open(ruta_csv1, "w", newline="", encoding="utf-8") as filecsv:
    escritor = csv.writer(filecsv, delimiter=",")
    escritor.writerow(["servicio", "puerto", "estado"])
    escritor.writerow(["ssh", 22, "OK"])
    escritor.writerow(["http", 80, "OK"])
    escritor.writerow(["https", 443, "OK"])
print("CSV creado:", ruta_csv1)

print("\n=== 2. Escribir CSV con csv.DictWriter ===")
ruta_csv2 = carpeta / "servicios2.csv"
campos = ["servicio", "puerto", "estado"]
filas = [
    {"servicio": "ssh", "puerto": 22, "estado": "OK"},
    {"servicio": "http", "puerto": 80, "estado": "OK"},
    {"servicio": "postgresql", "puerto": 5432, "estado": "OK"},
]
with open(ruta_csv2, "w", newline="", encoding="utf-8") as filecsv:
    escritor = csv.DictWriter(filecsv, fieldnames=campos, delimiter=",")
    escritor.writeheader()
    escritor.writerows(filas)
print("CSV creado:", ruta_csv2)

print("\n=== 3. Leer CSV con csv.reader ===")
with open(ruta_csv1, "r", newline="", encoding="utf-8") as filecsv:
    lector = csv.reader(filecsv, delimiter=",")
    cabecera = next(lector)
    print("Cabecera:", cabecera)
    for fila in lector:
        servicio, puerto, estado = fila
        print(f"Servicio: {servicio} -> {puerto}: {estado}")

print("\n=== 4. Leer CSV con csv.DictReader ===")
with open(ruta_csv2, "r", newline="", encoding="utf-8") as filecsv:
    lector = csv.DictReader(filecsv, delimiter=",")
    for fila in lector:
        puerto = int(fila["puerto"])
        print(f"Servicio: {fila['servicio']} -> Puerto {puerto} [{fila['estado']}]")

print("\n=== 5. Normalizar datos desde servicios3.csv ===")
ruta_csv3 = carpeta / "servicios3.csv"
servicios_validos = []
servicios_rechazados = []

try:
    with open(ruta_csv3, "r", newline="", encoding="utf-8") as filecsv:
        lector = csv.DictReader(filecsv, delimiter=",")
        for fila in lector:
            servicio = fila["servicio"].strip().lower()
            puerto_txt = fila["puerto"].strip()
            estado = fila["estado"].strip().upper()
            try:
                puerto = int(puerto_txt)
            except ValueError:
                servicios_rechazados.append({"servicio": servicio, "puerto": puerto_txt, "motivo": "puerto no numérico"})
            else:
                servicios_validos.append({"servicio": servicio, "puerto": puerto, "estado": estado})
except FileNotFoundError:
    print(f"[CRÍTICO] No existe el fichero esperado: {ruta_csv3}")

print("Servicios válidos normalizados:")
for servicio in servicios_validos:
    print(servicio)
print("Servicios rechazados:")
for servicio in servicios_rechazados:
    print(servicio)

print("\n=== 6. Guardar CSV normalizado ===")
ruta_normalizada = carpeta / "servicios3_normalizado.csv"
with open(ruta_normalizada, "w", newline="", encoding="utf-8") as filecsv:
    campos = ["servicio", "puerto", "estado"]
    escritor = csv.DictWriter(filecsv, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(servicios_validos)
print("CSV normalizado guardado en:", ruta_normalizada)
