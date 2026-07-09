"""
Tema 9 - Módulos
Módulo de validaciones reutilizables.

Este fichero actúa como módulo propio. No está pensado para ejecutarse como
script principal, sino para ser importado desde otros ficheros.
"""


def puerto_valido(puerto: int) -> bool:
    """Devuelve True si el puerto está dentro del rango TCP/UDP válido."""
    return 1 <= puerto <= 65535


def normalizar_servicio(nombre: str) -> str:
    """Elimina espacios sobrantes y convierte el servicio a minúsculas."""
    return nombre.strip().lower()


def estado_valido(estado: str) -> bool:
    """Comprueba si el estado pertenece a los valores esperados."""
    return estado.strip().upper() in ("OK", "ERROR", "DETENIDO")
