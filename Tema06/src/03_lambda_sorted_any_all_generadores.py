"""
Tema 6 - Elementos de programación funcional
Laboratorio 3: lambda, sorted(key=...), any(), all() y expresiones generadoras.

Objetivo:
    Usar lambdas breves cuando aportan claridad.
    Ordenar colecciones con una función de criterio.
    Validar colecciones con any() y all().
    Entender que una expresión generadora produce valores bajo demanda.
"""

print("=== 1. lambda: función anónima breve ===")

servicios = ["ssh", "nginx", "postgresql", "api"]

longitudes = list(map(lambda servicio: len(servicio), servicios))
print("Longitudes:", longitudes)

sin_api = list(filter(lambda servicio: servicio != "api", servicios))
print("Servicios excepto api:", sin_api)


print("\n=== 2. Cuándo usar def en lugar de lambda ===")

def describir_puerto(puerto):
    """Devuelve una descripción breve de un puerto."""
    if puerto in (80, 443):
        return f"{puerto}: web"
    return f"{puerto}: otro"

puertos = [22, 80, 443, 8080]
descripciones = list(map(describir_puerto, puertos))

print(descripciones)


print("\n=== 3. sorted(key=...): ordenar con una función ===")

servicios = [
    {"nombre": "ssh", "puerto": 22},
    {"nombre": "api", "puerto": 8080},
    {"nombre": "nginx", "puerto": 443},
    {"nombre": "rdp", "puerto": 3389},
]

ordenados_por_puerto = sorted(servicios, key=lambda servicio: servicio["puerto"])

print("Ordenados por puerto:")
for servicio in ordenados_por_puerto:
    print(servicio)


print("\n=== 4. Ordenar por nombre usando una función definida ===")

def obtener_nombre(servicio):
    """Devuelve el nombre de un servicio representado como diccionario."""
    return servicio["nombre"]

ordenados_por_nombre = sorted(servicios, key=obtener_nombre)

print("Ordenados por nombre:")
for servicio in ordenados_por_nombre:
    print(servicio)


print("\n=== 5. any() y all() ===")

puertos = [22, 443, 8080]

hay_puerto_alto = any(puerto > 1024 for puerto in puertos)
todos_validos = all(1 <= puerto <= 65535 for puerto in puertos)

print("Hay puerto alto:", hay_puerto_alto)
print("Todos los puertos son válidos:", todos_validos)


print("\n=== 6. Expresiones generadoras ===")

logs = ["OK ssh", "ERROR api", "ERROR nginx"]

errores = (
    linea for linea in logs
    if linea.startswith("ERROR")
)

print("Objeto generador:", errores)

for error in errores:
    print("Error detectado:", error)


print("\n=== 7. El generador también se consume ===")

errores = (
    linea for linea in logs
    if linea.startswith("ERROR")
)

print("Primera lectura:", list(errores))
print("Segunda lectura:", list(errores))
print("La segunda lectura está vacía porque el generador ya se recorrió.")
