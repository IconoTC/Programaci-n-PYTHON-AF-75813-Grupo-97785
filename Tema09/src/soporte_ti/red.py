"""
Módulo red del paquete soporte_ti.

Contiene funciones de normalización y validación de servicios de red.
"""


def normalizar_servicio(nombre: str) -> str:
    """Normaliza nombres de servicio para comparación y reporte."""
    return nombre.strip().lower()


def validar_puerto(puerto: int) -> bool:
    """Devuelve True si el puerto está dentro del rango TCP/UDP válido."""
    return 1 <= puerto <= 65535


def validar_ip_simple(ip: str) -> bool:
    """
    Valida una dirección IPv4 de forma básica.

    Reglas:
        - Debe tener cuatro partes separadas por puntos.
        - Cada parte debe ser numérica.
        - Cada número debe estar entre 0 y 255.
    """
    partes = ip.split(".")

    if len(partes) != 4:
        return False

    for parte in partes:
        if not parte.isdigit():
            return False

        numero = int(parte)
        if numero < 0 or numero > 255:
            return False

    return True


def comprobar_servicio(servicio: dict) -> dict:
    """Normaliza y valida un registro de servicio."""
    nombre = normalizar_servicio(servicio["nombre"])
    ip = servicio["ip"]
    puerto = servicio["puerto"]

    return {
        "nombre": nombre,
        "ip": ip,
        "puerto": puerto,
        "ip_valida": validar_ip_simple(ip),
        "puerto_valido": validar_puerto(puerto),
    }


def comprobar(servicios: list[dict]) -> list[dict]:
    """Comprueba una lista de servicios y devuelve resultados normalizados."""
    resultados = []

    for servicio in servicios:
        resultado = comprobar_servicio(servicio)
        resultados.append(resultado)

    return resultados
