"""Generación de informes de salida."""

from datetime import datetime


def _lineas_contador(titulo, datos):
    """Construye líneas de texto para un diccionario de contadores."""
    lineas = [titulo]
    for clave, valor in sorted(datos.items()):
        lineas.append(f"  - {clave}: {valor}")
    return lineas


def generar_informe(resumen, equipos_pendientes):
    """Genera el informe final en formato de texto plano."""
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lineas = [
        "INFORME DE INVENTARIO TI",
        "=" * 26,
        f"Generado: {ahora}",
        "",
        f"Total de equipos: {resumen['total_equipos']}",
        "",
    ]

    lineas.extend(_lineas_contador("Estados:", resumen["estados"]))
    lineas.append("")
    lineas.extend(_lineas_contador("Entornos:", resumen["entornos"]))
    lineas.append("")
    lineas.extend(_lineas_contador("Clasificaciones:", resumen["clasificaciones"]))
    lineas.append("")
    lineas.append("Servicios únicos:")
    lineas.append("  " + ", ".join(resumen["servicios_unicos"]))
    lineas.append("")
    lineas.append("Equipos pendientes de revisión:")

    if not equipos_pendientes:
        lineas.append("  No hay equipos pendientes.")
    else:
        for equipo in equipos_pendientes:
            incidencias = "; ".join(equipo["incidencias"]) or "sin incidencias de validación"
            lineas.append(
                f"  - {equipo['nombre']} | {equipo['entorno']} | "
                f"{equipo['servicio']}:{equipo['puerto']} | "
                f"{equipo['clasificacion']} | {incidencias}"
            )

    return "\n".join(lineas) + "\n"
