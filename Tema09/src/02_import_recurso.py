"""
Tema 9 - Módulos
Laboratorio 2: importar recursos concretos.

Objetivo:
    Importar solo una función concreta desde un módulo.
"""

from validaciones import puerto_valido

if puerto_valido(22):
    print("ssh válido")

# Esta línea generaría NameError porque normalizar_servicio
# no se ha importado en este script.
# servicio = normalizar_servicio(" SsH ")
# print(servicio)
