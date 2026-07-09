"""
Tema 10 - Biblioteca estándar
Laboratorio 6: procesos externos con subprocess.

Objetivo:
    Ejecutar comandos del sistema usando una lista de argumentos, capturar
    stdout/stderr y revisar el código de retorno.
"""

import subprocess


def ejecutar_comando(comando):
    """Ejecuta un comando externo y muestra salida controlada."""
    print("Comando:", " ".join(comando))

    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True,
        check=False,
    )

    print("Código de retorno:", resultado.returncode)

    if resultado.stdout:
        print("--- stdout ---")
        print(resultado.stdout.strip())

    if resultado.stderr:
        print("--- stderr ---")
        print(resultado.stderr.strip())

    return resultado.returncode


print("=== 1. Comprobar espacio en disco ===")
ejecutar_comando(["df", "-h", "/"])

print("\n=== 2. Comando con código de retorno distinto de cero ===")
# El comando false existe en sistemas Unix/Linux y devuelve código 1.
# Sirve para demostrar un fallo controlado sin depender de un ejecutable inexistente.
ejecutar_comando(["false"])
