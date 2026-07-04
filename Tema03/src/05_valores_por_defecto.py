"""
Tema 3 - Funciones
Laboratorio 5: valores por defecto y cuidado con objetos mutables.

Objetivo:
    Usar parámetros con valores por defecto.
    Comprender por qué no conviene usar listas o diccionarios como valor por defecto.
"""


def crear_alerta(mensaje, nivel="INFO", notificar=False):
    """
    Crea un texto de alerta con nivel y opción de notificación.

    Args:
        mensaje: Texto principal de la alerta.
        nivel: Nivel de severidad. Por defecto, INFO.
        notificar: Indica si debe añadirse una marca de aviso.

    Returns:
        Texto de alerta formateado.
    """
    texto = f"[{nivel}] {mensaje}"
    if notificar:
        texto += " -> enviar aviso"
    return texto


print(crear_alerta("Servicio iniciado"))
print(crear_alerta("Disco lleno", nivel="CRITICO", notificar=True))


# Ejemplo mal construido: la lista por defecto se crea una sola vez
# al definir la función. Las llamadas posteriores pueden reutilizarla.
def agregar_evento_mal(evento, historial=[]):
    """
    Ejemplo no recomendado: usa una lista mutable como valor por defecto.

    Args:
        evento: Evento que se añadirá.
        historial: Lista de eventos.

    Returns:
        Lista de eventos acumulada de forma implícita.
    """
    historial.append(evento)
    return historial


print("Mal construido:")
print(agregar_evento_mal("arranque"))
print(agregar_evento_mal("parada"))
print(agregar_evento_mal("reinicio"))


# Forma recomendada: usar None y crear la lista dentro de la función
# si no se ha recibido una lista externa.
def agregar_evento(evento, historial=None):
    """
    Añade un evento a una lista recibida o crea una lista temporal.

    Args:
        evento: Evento que se añadirá.
        historial: Lista opcional de eventos.

    Returns:
        Lista con el evento añadido.
    """
    if historial is None:
        historial = []
    historial.append(evento)
    return historial


print("Bien construido, llamadas independientes:")
print(agregar_evento("arranque"))
print(agregar_evento("parada"))

print("Bien construido, historial externo controlado:")
historico_eventos = []
print(agregar_evento("arranque", historico_eventos))
print(agregar_evento("parada", historico_eventos))
