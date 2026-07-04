"""
Tema 3 - Funciones
Ejercicios adicionales para modificar y completar.

Objetivo:
    Practicar la creación de funciones pequeñas y reutilizables.
    Estos ejercicios pueden servir como base para laboratorios o notebooks.
"""


def normalizar_usuario(usuario: str) -> str:
    """
    Normaliza un nombre de usuario.

    Args:
        usuario: Texto introducido por el usuario.

    Returns:
        Usuario sin espacios laterales y en minúsculas.
    """
    return usuario.strip().lower()


def construir_nombre_servicio(nombre: str, entorno: str = "prod") -> str:
    """
    Construye un nombre estándar de servicio.

    Args:
        nombre: Nombre base del servicio.
        entorno: Entorno donde se ejecuta el servicio.

    Returns:
        Nombre normalizado con formato entorno-nombre.
    """
    return f"{entorno}-{nombre}".lower()


def media_valores(*valores: float) -> float | None:
    """
    Calcula la media de un número variable de valores.

    Args:
        *valores: Valores numéricos.

    Returns:
        Media aritmética o None si no hay valores.
    """
    if not valores:
        return None
    return sum(valores) / len(valores)


def resumen_servicio(nombre: str, activo: bool, *puertos: int, entorno: str = "prod") -> str:
    """
    Construye un resumen de servicio con puertos asociados.

    Args:
        nombre: Nombre del servicio.
        activo: Estado lógico del servicio.
        *puertos: Puertos asociados al servicio.
        entorno: Entorno de despliegue.

    Returns:
        Cadena resumen.
    """
    estado = "activo" if activo else "inactivo"
    if puertos:
        puertos_convertidos = []
        for puerto in puertos:
            puertos_convertidos.append(str(puerto))
            puertos_txt = ", ".join(puertos_convertidos)
    else:
            puertos_txt = "sin puertos"
    return f"{entorno}:{nombre} -> {estado} -> {puertos_txt}"


print(normalizar_usuario("  Admin.Sistemas  "))
print(construir_nombre_servicio("api"))
print(construir_nombre_servicio("api", entorno="dev"))
print(media_valores(10, 8, 9))
print(media_valores())
print(resumen_servicio("nginx", True, 80, 443, entorno="prod"))
