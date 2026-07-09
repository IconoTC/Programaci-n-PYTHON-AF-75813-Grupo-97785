"""
Tema 10 - Biblioteca estándar
Laboratorio 12: HTTP básico con urllib.

Objetivo:
    Realizar una petición HTTP sencilla controlando timeout y errores.

Nota:
    Este ejemplo requiere salida a Internet. Si el laboratorio no tiene conexión,
    debe fallar de forma controlada.
"""

from urllib.request import urlopen
from urllib.error import URLError
import json


url = "https://api.ipify.org?format=json"

print("=== Petición HTTP básica ===")
print("URL:", url)

try:
    with urlopen(url, timeout=5) as respuesta:
        datos = json.load(respuesta)
        print("Conexión exitosa.")
        print("IP pública detectada:", datos["ip"])
except URLError as error:
    print("No se pudo conectar con la API.")
    print("Motivo:", error.reason)
except TimeoutError:
    print("La petición superó el tiempo de espera.")
