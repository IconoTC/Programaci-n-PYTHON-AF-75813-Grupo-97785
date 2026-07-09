"""
Tema 9 - Módulos
Laboratorio 4: importar todo con *.

Objetivo:
    Mostrar que import * funciona, pero no es recomendable en código
    profesional porque oculta el origen de los nombres importados.
"""

# Evitar esta forma salvo casos muy justificados.
from validaciones import *

puerto = 443

if puerto_valido(puerto):
    print("Puerto correcto")

servicio = normalizar_servicio(" SsH ")
print("Servicio normalizado:", servicio)

estado = " error "
print("Estado válido:", estado_valido(estado))
