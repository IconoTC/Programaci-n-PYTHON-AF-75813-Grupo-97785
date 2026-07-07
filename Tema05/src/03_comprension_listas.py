"""
Tema 5 - Colecciones de objetos
Laboratorio 3: comprensión de listas.

Objetivo:
    Crear listas nuevas a partir de otras colecciones con expresiones sencillas,
    manteniendo la legibilidad del código.
"""

print("=== 1. Normalizar datos con bucle tradicional ===")

servicios = [" SSH ", " NGINX ", " postgresql "]
normalizados = []

for servicio in servicios:
    normalizados.append(servicio.strip().lower())

print(normalizados)

print("\n=== 2. Normalizar datos con comprensión de listas ===")

servicios = [" SSH ", " NGINX ", " postgresql "]
normalizados = [servicio.strip().lower() for servicio in servicios]

print(normalizados)

print("\n=== 3. Filtrar datos con condición ===")

puertos = [22, 80, 443, 8080, 3306]
puertos_web = [puerto for puerto in puertos if puerto in (80, 443, 8080)]

print("Puertos web:", puertos_web)

print("\n=== 4. Transformar y filtrar al mismo tiempo ===")

logs = ["OK ssh", "ERROR nginx", "ERROR api", "OK backup"]

# Extraer el nombre del servicio solo de las líneas que empiezan por ERROR.
servicios_error = [linea.split()[1] for linea in logs if linea.startswith("ERROR")]

print("Servicios con error:", servicios_error)

print("\n=== 5. Comprensión sobre lista de objetos ===")

class Servicio:
    """Representa un servicio con nombre y estado."""

    def __init__(self, nombre, activo):
        self.nombre = nombre
        self.activo = activo


servicios = [
    Servicio("ssh", True),
    Servicio("api", False),
    Servicio("backup", True),
]

activos = [servicio.nombre for servicio in servicios if servicio.activo]
detenidos = [servicio.nombre for servicio in servicios if not servicio.activo]

print("Activos:", activos)
print("Detenidos:", detenidos)

print("\n=== 6. Criterio práctico ===")

# Si la expresión se vuelve difícil de leer, usa un bucle tradicional.
# Esta versión es explícita y puede ser más clara para depuración.
resultado = []

for linea in logs:
    if linea.startswith("ERROR"):
        partes = linea.split()
        resultado.append(partes[1].upper())

print(resultado)
