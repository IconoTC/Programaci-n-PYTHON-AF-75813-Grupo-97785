"""
Tema 5 - Colecciones de objetos
Laboratorio 2: listas multidimensionales.

Objetivo:
    Practicar listas que contienen otras listas y entender cuándo una tabla
    pequeña puede representarse con índices y cuándo sería más claro usar
    diccionarios.
"""

print("=== 1. Lista de listas como tabla sencilla ===")

estado_hosts = [
    ["srv01", "OK", 22],
    ["srv02", "FALLO", 80],
    ["srv03", "OK", 443],
]

# Acceso por fila y columna: [fila][columna]
print("Host de la primera fila:", estado_hosts[0][0])
print("Estado de la segunda fila:", estado_hosts[1][1])
print("Puerto de la tercera fila:", estado_hosts[2][2])

print("\n=== 2. Recorrer filas completas ===")

for fila in estado_hosts:
    host = fila[0]
    estado = fila[1]
    puerto = fila[2]
    print(f"{host} -> {estado}:{puerto}")

print("\n=== 3. Recorrer usando índices ===")

for indice_fila in range(len(estado_hosts)):
    print("Fila:", indice_fila)

    for indice_columna in range(len(estado_hosts[indice_fila])):
        print("  Valor:", estado_hosts[indice_fila][indice_columna])

print("\n=== 4. Matriz irregular ===")

# Las filas no tienen por qué tener todas la misma longitud.
# Esto puede ser útil, pero también puede complicar el código.
servicios_por_host = [
    ["srv01", "ssh", "nginx"],
    ["srv02", "ssh"],
    ["srv03", "ssh", "postgresql", "backup"],
]

for fila in servicios_por_host:
    host = fila[0]
    servicios = fila[1:]
    print(f"{host} tiene servicios: {servicios}")

print("\n=== 5. Alternativa más legible con diccionarios ===")

# Si los campos tienen nombre, suele ser más claro usar diccionarios.
inventario = [
    {"host": "srv01", "estado": "OK", "puerto": 22},
    {"host": "srv02", "estado": "FALLO", "puerto": 80},
    {"host": "srv03", "estado": "OK", "puerto": 443},
]

for equipo in inventario:
    print(f"{equipo['host']} -> {equipo['estado']}:{equipo['puerto']}")
