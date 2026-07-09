"""
Tema 9 - Módulos
Laboratorio 7: ejemplo integrado de paquete propio.

Estructura:
    Tema09/
    └── src/
        ├── 07_paquete_soporte_ti_demo.py
        └── soporte_ti/
            ├── __init__.py
            ├── red.py
            └── reportes.py

Objetivo:
    Usar un paquete propio con varios módulos internos.
"""

from soporte_ti import __version__
from soporte_ti import red
from soporte_ti import reportes


def main():
    """Ejecuta el ejemplo integrado del paquete soporte_ti."""
    print("=== 1. Información del paquete ===")
    print("Paquete soporte_ti versión:", __version__)

    print("\n=== 2. Datos de servicios ===")
    servicios = [
        {"nombre": " SSH ", "ip": "10.0.0.10", "puerto": 22},
        {"nombre": "NGINX", "ip": "10.0.0.20", "puerto": 443},
        {"nombre": "api", "ip": "ip_invalida", "puerto": 8080},
        {"nombre": "backup", "ip": "10.0.0.40", "puerto": 70000},
    ]

    for servicio in servicios:
        print(servicio)

    print("\n=== 3. Comprobar servicios con soporte_ti.red ===")
    resultados = red.comprobar(servicios)

    for resultado in resultados:
        print(resultado)

    print("\n=== 4. Generar resumen con soporte_ti.reportes ===")
    resumen = reportes.generar_resumen(resultados)
    print(resumen)


if __name__ == "__main__":
    main()
