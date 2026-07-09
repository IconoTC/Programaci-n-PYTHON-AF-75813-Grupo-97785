"""
Tema 10 - Biblioteca estándar
Laboratorio 9: fechas, horas y zonas con datetime, zoneinfo y calendar.

Objetivo:
    Generar marcas de tiempo y calcular una ventana de mantenimiento.
"""

from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import calendar


print("=== Fecha y hora actual en UTC ===")
ahora_utc = datetime.now(timezone.utc)
print("UTC:", ahora_utc.isoformat(timespec="seconds"))

print("\n=== Calcular último día del mes ===")
anio = ahora_utc.year
mes = ahora_utc.month
_, ultimo_dia = calendar.monthrange(anio, mes)
print("Año:", anio)
print("Mes:", mes)
print("Último día:", ultimo_dia)

print("\n=== Ventana de mantenimiento en zona local ===")
zona_local = ZoneInfo("Europe/Madrid")
ejecucion_local = datetime(anio, mes, ultimo_dia, 22, 0, tzinfo=zona_local)
print("Planificación local:", ejecucion_local.isoformat(timespec="seconds"))
