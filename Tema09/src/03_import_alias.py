"""
Tema 9 - Módulos
Laboratorio 3: importar con alias.

Objetivo:
    Usar alias tanto para un módulo completo como para un recurso concreto.
"""

print("=== Alias de módulo completo ===")

import validaciones as val

if val.puerto_valido(443):
    print("https válido")

print("Servicio:", val.normalizar_servicio(" NGINX "))

print("\n=== Alias de recurso concreto ===")

from validaciones import puerto_valido as valido

if valido(22):
    print("ssh válido")

# Esta línea generaría NameError porque no se importó el nombre original.
# print(puerto_valido(443))
