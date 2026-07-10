"""Funciones de normalización y validación de datos."""


def normalizar_texto(valor):
    """Devuelve una cadena sin espacios sobrantes."""
    return str(valor).strip()


def normalizar_servicio(valor):
    """Normaliza el nombre de un servicio para comparar de forma consistente."""
    return normalizar_texto(valor).lower()


def normalizar_estado(valor):
    """Normaliza un estado operativo a mayúsculas."""
    return normalizar_texto(valor).upper()


def convertir_entero(valor, campo):
    """Convierte un valor a entero y añade contexto si falla."""
    try:
        return int(valor)
    except ValueError as error:
        raise ValueError(f"El campo {campo!r} debe ser numérico: {valor!r}") from error


def puerto_valido(puerto):
    """Comprueba si un puerto está dentro del rango TCP/UDP válido."""
    return 1 <= puerto <= 65535


def ip_basica_valida(ip):
    """Valida una dirección IPv4 con una comprobación básica suficiente para el curso."""
    partes = str(ip).split(".")
    if len(partes) != 4:
        return False

    for parte in partes:
        if not parte.isdigit():
            return False
        numero = int(parte)
        if numero < 0 or numero > 255:
            return False

    return True


def validar_estado(estado, estados_validos):
    """Comprueba si el estado pertenece a la política del proyecto."""
    return estado in estados_validos


def validar_equipo(equipo, politica):
    """Devuelve una lista de incidencias de validación para un equipo."""
    incidencias = []
    estados_validos = politica.get("estados_validos", [])
    puertos_esperados = politica.get("puertos_esperados", {})

    if not ip_basica_valida(equipo.ip):
        incidencias.append("IP con formato no válido")

    if not puerto_valido(equipo.puerto):
        incidencias.append("Puerto fuera de rango")

    if not validar_estado(equipo.estado, estados_validos):
        incidencias.append("Estado no reconocido")

    puertos_servicio = puertos_esperados.get(equipo.servicio, [])
    if puertos_servicio and equipo.puerto not in puertos_servicio:
        incidencias.append("Puerto no esperado para el servicio")

    return incidencias
