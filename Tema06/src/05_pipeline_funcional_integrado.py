"""
Tema 6 - Elementos de programación funcional
Laboratorio 5: ejercicio final integrado.

Objetivo:
    Combinar varias operaciones funcionales en un flujo sencillo:
    limpieza, transformación, filtrado, ordenación, validación y resumen.

Contexto:
    Se parte de líneas de texto que simulan datos recibidos de un inventario.
"""

from functools import reduce

print("=== 1. Datos de entrada ===")

# Formato esperado de cada línea:
# nombre_servicio;puerto;estado
lineas = [
    " SSH ; 22 ; activo ",
    " nginx ; 443 ; activo ",
    " api ; 8080 ; detenido ",
    " backup ; 70000 ; activo ",
    " rdp ; 3389 ; activo ",
    " ntp ; 123 ; activo ",
]

print("Datos originales:")
for linea in lineas:
    print(repr(linea))


print("\n=== 2. Funciones pequeñas para cada paso ===")

def limpiar_linea(linea):
    """Elimina espacios sobrantes de la línea completa."""
    return linea.strip()

def dividir_linea(linea):
    """
    Divide una línea en campos.

    Returns:
        Tupla con nombre, puerto como texto y estado.
    """
    nombre, puerto, estado = linea.split(";")
    return nombre.strip().lower(), puerto.strip(), estado.strip().lower()

def construir_servicio(campos):
    """
    Convierte una tupla de campos en un diccionario de servicio.

    El puerto se convierte a entero. En este ejemplo los datos son controlados.
    """
    nombre, puerto, estado = campos
    return {
        "nombre": nombre,
        "puerto": int(puerto),
        "activo": estado == "activo",
    }

def puerto_valido(servicio):
    """Devuelve True si el puerto del servicio está en el rango válido."""
    return 1 <= servicio["puerto"] <= 65535

def servicio_activo(servicio):
    """Devuelve True si el servicio está marcado como activo."""
    return servicio["activo"]

def describir_servicio(servicio):
    """Devuelve una cadena legible para el reporte."""
    return f'{servicio["nombre"]}:{servicio["puerto"]}'

print("Funciones auxiliares definidas.")


print("\n=== 3. Limpiar y convertir los datos ===")

limpias = list(map(limpiar_linea, lineas))
campos = list(map(dividir_linea, limpias))
servicios = list(map(construir_servicio, campos))

print("Líneas limpias:", limpias)
print("Campos:", campos)
print("Servicios:", servicios)


print("\n=== 4. Filtrar servicios activos y puertos válidos ===")

activos = list(filter(servicio_activo, servicios))
activos_validos = list(filter(puerto_valido, activos))

print("Servicios activos:", activos)
print("Servicios activos con puerto válido:", activos_validos)


print("\n=== 5. Ordenar y construir reporte ===")

ordenados = sorted(activos_validos, key=lambda servicio: servicio["puerto"])
reporte = list(map(describir_servicio, ordenados))

print("Reporte:")
for linea in reporte:
    print("-", linea)


print("\n=== 6. Validaciones con any() y all() ===")

hay_puertos_altos = any(servicio["puerto"] > 1024 for servicio in activos_validos)
todos_validos = all(puerto_valido(servicio) for servicio in activos_validos)

print("Hay puertos altos:", hay_puertos_altos)
print("Todos los activos filtrados tienen puertos válidos:", todos_validos)


print("\n=== 7. Resumen con reduce() ===")

def contar_por_estado(conteo, servicio):
    """Acumula cuántos servicios hay por estado lógico."""
    estado = "activo" if servicio["activo"] else "detenido"

    if estado not in conteo:
        conteo[estado] = 0

    conteo[estado] += 1
    return conteo

resumen_estados = reduce(contar_por_estado, servicios, {})

print("Resumen de estados:", resumen_estados)


print("\n=== 8. Resultado final ===")

print(f"Total de líneas recibidas: {len(lineas)}")
print(f"Total de servicios interpretados: {len(servicios)}")
print(f"Activos con puerto válido: {len(activos_validos)}")
print("Servicios listos para reporte:", reporte)
