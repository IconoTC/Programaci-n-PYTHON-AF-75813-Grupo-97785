"""
Tema 3 - Funciones
Laboratorio 6: *args, **kwargs y orden recomendado de parámetros.

Objetivo:
    Usar número variable de argumentos posicionales con *args.
    Usar número variable de argumentos con nombre con **kwargs.
    Revisar el orden recomendado cuando se combinan parámetros.
"""


def totalizar_consumo(*medidas):
    """
    Suma un número variable de medidas.

    Args:
        *medidas: Valores numéricos de consumo o medición.

    Returns:
        Suma total de las medidas recibidas.
    """
    total = 0
    for valor in medidas:
        total += valor
    return total


def describir_recurso(nombre, **atributos):
    """
    Muestra información variable de un recurso.

    Args:
        nombre: Nombre del recurso.
        **atributos: Pares clave=valor con metadatos del recurso.

    Returns:
        None. La función muestra la información por pantalla.
    """
    print(f"Recurso: {nombre}")
    for clave, valor in atributos.items():
        print(f"- {clave}: {valor}")


def registrar_metricas(servicio, *valores, unidad="ms", **etiquetas):
    """
    Registra métricas de un servicio usando parámetros combinados.

    Args:
        servicio: Nombre del servicio.
        *valores: Mediciones recibidas.
        unidad: Unidad de las mediciones.
        **etiquetas: Metadatos adicionales.

    Returns:
        Diccionario con los datos agrupados.
    """
    return {
        "servicio": servicio,
        "valores": valores,
        "unidad": unidad,
        "etiquetas": etiquetas,
    }


print("Total de consumo:", totalizar_consumo(12, 15, 9))
print("Total sin medidas:", totalizar_consumo())

describir_recurso("srv01", cpu=4, memoria="16GB", entorno="prod")

metricas = registrar_metricas("api", 12, 15, 9, unidad="ms", zona="dmz", entorno="prod")
print(metricas)
