"""
Tema 6 - Elementos de programación funcional
Laboratorio 2: map() y filter().

Objetivo:
    Aplicar transformaciones con map() y filtros con filter().
    Observar que devuelven iterables y que normalmente los convertimos
    con list() o dict() para materializar los resultados.
"""

print("=== 1. map(): transformar cada elemento ===")

def normalizar_servicio(servicio):
    """Normaliza un nombre de servicio eliminando espacios y usando minúsculas."""
    return servicio.strip().lower()

servicios = [" SSH ", " NGINX ", " Api "]

normalizados_iterable = map(normalizar_servicio, servicios)
print("Objeto devuelto por map:", normalizados_iterable)

normalizados = list(normalizados_iterable)

print("Normalizados:", normalizados)
print("Original:", servicios)


print("\n=== 2. Evaluación perezosa: el iterable se consume ===")

servicios = ["ssh", "nginx", "api"]
resultado = map(str.upper, servicios)

print("Primera conversión:", list(resultado))
print("Segunda conversión:", list(resultado))
print("La segunda lista sale vacía porque el iterable ya se consumió.")


print("\n=== 3. map() con más de una colección ===")

def crear_endpoint(servicio, puerto):
    """Construye una cadena servicio:puerto."""
    return f"{servicio}:{puerto}"

servicios = ["ssh", "nginx", "postgresql"]
puertos = [22, 443, 5432]

endpoints = list(map(crear_endpoint, servicios, puertos))
print("Endpoints:", endpoints)


print("\n=== 4. filter(): seleccionar elementos ===")

def esta_activo(servicio):
    """Devuelve True si el servicio está activo."""
    return servicio["activo"]

servicios = [
    {"nombre": "ssh", "activo": True},
    {"nombre": "api", "activo": False},
    {"nombre": "http", "activo": False},
    {"nombre": "ntp", "activo": True},
]

activos = list(filter(esta_activo, servicios))
print("Servicios activos:", activos)


print("\n=== 5. filter() con diccionarios ===")

puertos = {
    "ssh": 22,
    "nginx": 443,
    "api": 8080,
    "rdp": 3389,
}

def es_puerto_estandar(item):
    """Devuelve True si el puerto del item es habitual o estándar en este ejemplo."""
    servicio, puerto = item
    return puerto in (22, 80, 443)

puertos_estandar = dict(filter(es_puerto_estandar, puertos.items()))
print("Puertos estándar:", puertos_estandar)


print("\n=== 6. Comprensión frente a map() y filter() ===")

servicios = [" SSH ", " Api ", " NGINX "]

# Comprensión clara: normalmente es más idiomática en Python.
limpios_1 = [servicio.strip().lower() for servicio in servicios]

# map() puede ser útil si ya tenemos funciones reutilizables.
limpios_2 = list(map(normalizar_servicio, servicios))

print("Comprensión:", limpios_1)
print("map():", limpios_2)


print("\n=== 7. Ejemplo adicional: filtrar líneas de log ===")

logs = [
    " OK ssh ",
    " ERROR api ",
    " ERROR nginx ",
    " OK backup ",
]

def es_error(linea):
    """Devuelve True si la línea de log corresponde a un error."""
    return linea.strip().startswith("ERROR")

errores = list(filter(es_error, logs))
errores_limpios = list(map(str.strip, errores))

print("Errores:", errores_limpios)
