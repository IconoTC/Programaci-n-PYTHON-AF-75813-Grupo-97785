"""
Módulo reportes del paquete soporte_ti.

Genera salidas legibles a partir de datos procesados por otros módulos.
"""


def generar_linea(resultado: dict) -> str:
    """Genera una línea de reporte para un resultado de comprobación."""
    estado_ip = "IP_OK" if resultado["ip_valida"] else "IP_ERROR"
    estado_puerto = "PUERTO_OK" if resultado["puerto_valido"] else "PUERTO_ERROR"

    return (
        f"{resultado['nombre']:<12} "
        f"{resultado['ip']:<15} "
        f"{resultado['puerto']:<6} "
        f"{estado_ip:<8} "
        f"{estado_puerto}"
    )


def generar_resumen(resultados: list[dict]) -> str:
    """Genera un resumen completo a partir de resultados validados."""
    lineas = [
        "SERVICIO     IP              PUERTO ESTADO_IP ESTADO_PUERTO",
        "-" * 62,
    ]

    for resultado in resultados:
        lineas.append(generar_linea(resultado))

    return "\n".join(lineas)
