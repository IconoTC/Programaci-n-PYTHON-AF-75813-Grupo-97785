"""
Tema 3 - Funciones
Laboratorio 2: parámetros, argumentos y return.

Objetivo:
    Diferenciar parámetros y argumentos.
    Entender que return devuelve un resultado reutilizable, mientras que print()
    solo muestra información por pantalla.
"""


def calcular_iva(base, porcentaje):
    """
    Calcula el importe del IVA aplicado sobre una base.

    Args:
        base: Importe base.
        porcentaje: Porcentaje de IVA.

    Returns:
        Importe del impuesto calculado.
    """
    impuesto = base * porcentaje / 100
    return impuesto


def calcular_descuento(precio, descuento):
    """
    Calcula el precio final aplicando un porcentaje de descuento.

    Args:
        precio: Precio inicial.
        descuento: Porcentaje de descuento.

    Returns:
        Precio después de aplicar el descuento.
    """
    return precio - (precio * descuento / 100)


def registrar_evento(texto):
    """
    Muestra un evento por pantalla.

    Esta función no devuelve ningún resultado explícito.
    Python devolverá None automáticamente.
    """
    print(f"EVENTO: {texto}")


# Los valores 100 y 21 son argumentos.
# base y porcentaje son parámetros definidos en la cabecera de la función.
iva = calcular_iva(100, 21)
print(f"IVA calculado: {iva:.2f} €")

precio_final = calcular_descuento(80, 15)
print(f"Precio final: {precio_final:.2f} €")

# Esta función solo imprime. No devuelve un valor reutilizable.
resultado = registrar_evento("reinicio programado")
print("Valor devuelto por registrar_evento:", resultado)
