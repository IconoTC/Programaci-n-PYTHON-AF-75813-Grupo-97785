"""
Tema 10 - Biblioteca estándar
Laboratorio 3: sistema y entorno con os, sys y platform.

Objetivo:
    Obtener contexto básico del entorno de ejecución sin instalar herramientas externas.
"""

import os
import sys
import platform


print("=== Información del intérprete Python ===")
print("Versión de Python:", sys.version.split()[0])
print("Ejecutable Python:", sys.executable)

print("\n=== Información del proceso y usuario ===")
print("Usuario:", os.environ.get("USER") or os.environ.get("USERNAME") or "desconocido")
print("PID actual:", os.getpid())
print("Directorio actual:", os.getcwd())

print("\n=== Información del sistema operativo ===")
print("Sistema:", platform.system())
print("Release:", platform.release())
print("Versión:", platform.version())
print("Máquina:", platform.machine())
