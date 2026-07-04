"""
Tema 3 - Funciones
Laboratorio 7: anotaciones de tipo, docstrings y buenas prácticas.

Objetivo:
    Documentar funciones con docstrings.
    Usar anotaciones de tipo para hacer el código más claro.
    Aplicar funciones pequeñas con responsabilidad concreta.
"""


def calcular_porcentaje(valor: float, total: float) -> float:
    """
    Devuelve el porcentaje que representa valor sobre total.

    Args:
        valor: Parte que se quiere comparar.
        total: Valor total de referencia.

    Returns:
        Porcentaje calculado.

    Nota:
        Este ejemplo no gestiona división por cero. La gestión formal
        de errores se trabajará en el tema correspondiente.
    """
    return valor * 100 / total


def es_puerto_valido(puerto: int) -> bool:
    """
    Comprueba si un puerto TCP/UDP está en el rango válido.

    Args:
        puerto: Número de puerto.

    Returns:
        True si el puerto está entre 1 y 65535. False en caso contrario.
    """
    return 1 <= puerto <= 65535


def generar_mensaje_puerto(puerto: int) -> str:
    """
    Genera un mensaje de validación para un puerto.

    Args:
        puerto: Número de puerto.

    Returns:
        Mensaje de validación.
    """
    if es_puerto_valido(puerto):
        return f"Puerto {puerto} válido"
    return f"Puerto {puerto} fuera de rango"


print(f"Porcentaje: {calcular_porcentaje(45, 200):.2f}%")
print(calcular_porcentaje.__doc__)

for puerto in [22, 443, 70000, 0]:
    print(generar_mensaje_puerto(puerto))
