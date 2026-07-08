"""
Tema 7 - Gestión de errores
Laboratorio 4: relanzar excepciones, excepciones personalizadas y traceback.

Objetivo:
    Añadir contexto a errores sin ocultarlos, crear una excepción propia
    sencilla y usar traceback para diagnóstico técnico.
"""

import traceback

print("=== 1. Re-lanzar una excepción ===")

def convertir_puerto(valor):
    """
    Convierte un texto a entero.

    Si falla, añade contexto y relanza la excepción original.
    """
    try:
        return int(valor)
    except ValueError:
        print(f"Fallo al convertir el puerto: {valor}")
        raise


print(convertir_puerto("22"))

try:
    convertir_puerto("ssh")
except ValueError as error:
    print("El llamador recibe el error relanzado:", error)


print("\n=== 2. Excepción personalizada ===")

class ServicioNoDisponibleError(Exception):
    """Error propio del dominio: un servicio esperado no está disponible."""
    pass


def comprobar_servicio(nombre, activo):
    """
    Comprueba si un servicio está activo.

    Raises:
        ServicioNoDisponibleError: si el servicio no está activo.
    """
    if not activo:
        raise ServicioNoDisponibleError(f"{nombre} no está activo")
    return "OK"


try:
    estado = comprobar_servicio("api", False)
except ServicioNoDisponibleError as error:
    print("Incidencia de servicio.")
    print("Detalle:", error)
else:
    print(estado)


print("\n=== 3. Traceback para diagnóstico ===")

try:
    int("ssh")
except ValueError as error:
    print("Error controlado:", error)
    print("Traceback técnico:")
    traceback.print_exc()


print("\n=== 4. Documentar errores en docstrings ===")

def obtener_puerto(config, servicio):
    """Devuelve el puerto de un servicio.

    Args:
        config: diccionario con servicios y puertos.
        servicio: nombre del servicio buscado.

    Returns:
        Puerto asociado al servicio.

    Raises:
        KeyError: si el servicio no existe.
    """
    return config[servicio]


puertos = {"ssh": 22}

print(obtener_puerto.__doc__)
print("Puerto ssh:", obtener_puerto(puertos, "ssh"))

try:
    print(obtener_puerto(puertos, "api"))
except KeyError as error:
    print("Servicio no definido en configuración:", error)
