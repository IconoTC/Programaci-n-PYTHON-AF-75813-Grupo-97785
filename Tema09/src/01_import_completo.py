"""
Tema 9 - Módulos
Laboratorio 1: importar un módulo completo.

Objetivo:
    Importar el módulo validaciones completo y acceder a sus recursos usando
    la sintaxis modulo.recurso.
"""

import validaciones

puerto = 443

if validaciones.puerto_valido(puerto):
    print("Puerto correcto")

servicio = validaciones.normalizar_servicio(" SsH ")
print("Servicio normalizado:", servicio)

estado = " ok "
print("Estado válido:", validaciones.estado_valido(estado))
