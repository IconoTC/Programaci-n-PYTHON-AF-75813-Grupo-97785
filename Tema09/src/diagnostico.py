"""
Tema 9 - Módulos
Módulo de diagnóstico.

Este ejemplo documenta el uso de if __name__ == "__main__".
"""


def comprobar() -> str:
    """Devuelve un mensaje sencillo de diagnóstico."""
    return "sistema operativo OK"


def obtener_estado_servicios() -> list[dict]:
    """Devuelve una lista simulada de servicios."""
    return [
        {"nombre": "ssh", "estado": "OK"},
        {"nombre": "nginx", "estado": "OK"},
        {"nombre": "api", "estado": "ERROR"},
    ]


def resumen_servicios(servicios: list[dict]) -> str:
    """Genera un resumen simple de servicios."""
    total = len(servicios)
    errores = 0

    for servicio in servicios:
        if servicio["estado"] == "ERROR":
            errores += 1

    return f"Servicios revisados: {total}. Servicios con error: {errores}"


# Este bloque solo se ejecuta si lanzamos:
# python diagnostico.py
#
# No se ejecuta cuando otro script hace import diagnostico.
if __name__ == "__main__":
    print("Iniciando diagnóstico")
    print(comprobar())

    servicios = obtener_estado_servicios()
    print(resumen_servicios(servicios))
