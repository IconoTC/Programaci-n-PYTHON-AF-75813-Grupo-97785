"""Funciones de análisis del inventario."""

from collections import Counter

from .validaciones import validar_equipo


def clasificar_equipo(equipo, politica):
    """Clasifica un equipo como NORMAL, REVISAR o CRITICO."""
    umbrales = politica.get("umbrales", {})
    metricas = equipo.metricas()

    if equipo.estado == "ERROR":
        return "CRITICO"

    if (
        metricas["cpu"] >= umbrales.get("cpu_critico", 85)
        or metricas["memoria"] >= umbrales.get("memoria_critico", 90)
        or metricas["disco"] >= umbrales.get("disco_critico", 90)
    ):
        return "CRITICO"

    if equipo.estado == "AVISO":
        return "REVISAR"

    if (
        metricas["cpu"] >= umbrales.get("cpu_aviso", 70)
        or metricas["memoria"] >= umbrales.get("memoria_aviso", 80)
        or metricas["disco"] >= umbrales.get("disco_aviso", 80)
    ):
        return "REVISAR"

    return "NORMAL"


def enriquecer_equipos(equipos, politica):
    """Añade clasificación e incidencias a cada equipo sin modificar el objeto original."""
    resultado = []

    for equipo in equipos:
        incidencias = validar_equipo(equipo, politica)
        clasificacion = clasificar_equipo(equipo, politica)
        datos = equipo.como_diccionario()
        datos["clasificacion"] = "REVISAR" if incidencias and clasificacion == "NORMAL" else clasificacion
        datos["incidencias"] = incidencias
        resultado.append(datos)

    return resultado


def obtener_resumen(equipos_enriquecidos):
    """Calcula contadores útiles para el informe final."""
    total = len(equipos_enriquecidos)
    estados = Counter(equipo["estado"] for equipo in equipos_enriquecidos)
    entornos = Counter(equipo["entorno"] for equipo in equipos_enriquecidos)
    clasificaciones = Counter(equipo["clasificacion"] for equipo in equipos_enriquecidos)
    servicios = sorted({equipo["servicio"] for equipo in equipos_enriquecidos})
    responsables = sorted({equipo["responsable"] for equipo in equipos_enriquecidos})

    return {
        "total_equipos": total,
        "estados": dict(estados),
        "entornos": dict(entornos),
        "clasificaciones": dict(clasificaciones),
        "servicios_unicos": servicios,
        "responsables": responsables,
    }


def filtrar_pendientes(equipos_enriquecidos):
    """Devuelve equipos que requieren revisión o atención crítica."""
    return [
        equipo for equipo in equipos_enriquecidos
        if equipo["clasificacion"] in ("REVISAR", "CRITICO")
    ]
