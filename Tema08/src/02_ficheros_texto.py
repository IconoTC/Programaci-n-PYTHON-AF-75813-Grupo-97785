"""
Tema 8 - Operaciones de entrada-salida
Laboratorio 2: ficheros de texto.

Objetivo:
    Practicar open()/close(), with, escritura, append, lectura completa,
    readline(), readlines(), recorrido línea a línea, copia y seek().
"""
from pathlib import Path

carpeta = Path("Tema08/data")
carpeta.mkdir(parents=True, exist_ok=True)

print("=== 1. open() y close() explícitos ===")
ruta = carpeta / "texto_open_close.txt"
fichero = open(ruta, "w", encoding="utf-8")
fichero.write("Linea 1\n")
fichero.write("Linea 2\n")
fichero.write("Linea 3\n")
fichero.close()

fichero = open(ruta, "r", encoding="utf-8")
todo_el_texto = fichero.read()
fichero.close()
print(todo_el_texto.strip())

print("\n=== 2. Escritura recomendada con with ===")
ruta_servicios = carpeta / "servicios_texto.txt"
with open(ruta_servicios, "w", encoding="utf-8") as fichero:
    fichero.write(f"{'Servicio':<12} {'Puerto':>6} {'Estado':>8}\n")
    fichero.write(f"{'ssh':<12} {'22':>6} {'OK':>8}\n")
    fichero.write(f"{'https':<12} {'443':>6} {'OK':>8}\n")
    fichero.write(f"{'http':<12} {'80':>6} {'NA':>8}\n")

print("\n=== 3. Añadir contenido con modo a ===")
with open(ruta_servicios, "a", encoding="utf-8") as fichero:
    fichero.write(f"{'ntp':<12} {'123':>6} {'OK':>8}\n")
    fichero.write(f"{'dns':<12} {'53':>6} {'OK':>8}\n")

print("\n=== 4. read(): leer todo el fichero ===")
with open(ruta_servicios, "r", encoding="utf-8") as fichero:
    contenido = fichero.read()
print(contenido.strip())

print("\n=== 5. readline(): leer línea a línea manualmente ===")
with open(ruta_servicios, "r", encoding="utf-8") as fichero:
    cabecera = fichero.readline()
    primer_servicio = fichero.readline()
print("Cabecera:", cabecera.strip())
print("Primera línea:", primer_servicio.strip())

print("\n=== 6. readlines(): leer como lista de líneas ===")
with open(ruta_servicios, "r", encoding="utf-8") as fichero:
    lineas = fichero.readlines()
print("Total de líneas:", len(lineas))
print("Línea 2:", lineas[2].strip())

print("\n=== 7. Recorrido línea a línea ===")
with open(ruta_servicios, "r", encoding="utf-8") as fichero:
    for linea in fichero:
        print(linea.strip())

print("\n=== 8. Procesar líneas con split() ===")
with open(ruta_servicios, "r", encoding="utf-8") as fichero:
    _ = fichero.readline()
    for linea in fichero:
        servicio, puerto, estado = linea.split()
        print(f"{servicio}({puerto}) -> Estado: {estado}")

print("\n=== 9. Copiar fichero de texto ===")
destino = carpeta / "servicios_texto_copia.txt"
with open(ruta_servicios, "r", encoding="utf-8") as entrada, open(destino, "w", encoding="utf-8") as salida:
    for linea in entrada:
        salida.write(linea)
print("Copia creada:", destino)

print("\n=== 10. Reposicionar cursor con seek(0) ===")
with open(ruta_servicios, "r", encoding="utf-8") as fichero:
    primera_lectura = fichero.read()
    print("Primera lectura:")
    print(primera_lectura.strip())
    _ = fichero.seek(0)
    segunda_lectura = fichero.read()
    print("Segunda lectura:")
    print(segunda_lectura.strip())
