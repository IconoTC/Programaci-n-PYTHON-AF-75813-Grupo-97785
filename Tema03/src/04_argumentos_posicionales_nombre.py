"""
Tema 3 - Funciones
Laboratorio 4: argumentos posicionales y argumentos con nombre.

Objetivo:
    Ver cómo el orden afecta a los argumentos posicionales.
    Usar argumentos con nombre para mejorar la legibilidad de las llamadas.
"""


def crear_usuario(nombre, grupo, activo):
    """
    Construye una descripción simple de usuario.

    Args:
        nombre: Nombre del usuario.
        grupo: Grupo asignado.
        activo: Estado lógico del usuario.

    Returns:
        Cadena descriptiva del usuario.
    """
    return f"{nombre} -> {grupo} -> activo={activo}"


def programar_tarea(nombre, hora, habilitada):
    """
    Construye una descripción de una tarea planificada.

    Args:
        nombre: Nombre de la tarea.
        hora: Hora de ejecución.
        habilitada: Estado de activación.

    Returns:
        Cadena con la planificación.
    """
    return f"{nombre} a las {hora}, habilitada={habilitada}"


# Argumentos posicionales: se asignan por orden.
print(crear_usuario("ana", "operadores", True))

# Este ejemplo no falla, pero el resultado no tiene sentido porque el orden es incorrecto.
print(crear_usuario("operadores", "ana", True))

# Argumentos con nombre: la llamada deja claro qué valor va a cada parámetro.
print(programar_tarea(nombre="backup", hora="02:00", habilitada=True))

# Con argumentos con nombre se puede cambiar el orden de la llamada.
print(programar_tarea(habilitada=False, hora="03:00", nombre="limpieza"))
