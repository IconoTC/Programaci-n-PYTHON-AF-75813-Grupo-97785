"""
Tema 3 - Funciones
Laboratorio 1: definición básica con def y llamada a funciones.

Objetivo:
    Entender que definir una función no la ejecuta.
    La función solo se ejecuta cuando se invoca usando su nombre y paréntesis.
"""


def saludar_operador():
    """Muestra un mensaje básico de inicio de sesión de soporte."""
    mensaje = "Sesión de soporte iniciada"
    print(mensaje)


def mostrar_estado(servicio):
    """Muestra por pantalla el nombre de un servicio que se está comprobando."""
    print(f"Comprobando servicio: {servicio}")


def estado_cpu(uso):
    """
    Clasifica el uso de CPU en un estado operativo.

    Args:
        uso: Porcentaje de uso de CPU.

    Returns:
        Una cadena con el estado NORMAL, ALTO o CRÍTICO.
    """
    if uso >= 90:
        return "CRÍTICO"
    if uso >= 70:
        return "ALTO"
    return "NORMAL"


# Definir las funciones anteriores no ejecuta nada por sí mismo.
# A partir de aquí empiezan las llamadas reales.
saludar_operador()

mostrar_estado("ssh")
mostrar_estado("httpd")
mostrar_estado("backup")

uso_actual = 82
print(f"Uso de CPU {uso_actual}% -> {estado_cpu(uso_actual)}")
