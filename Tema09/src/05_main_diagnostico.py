"""
Tema 9 - Módulos
Laboratorio 5: importar un módulo con bloque __main__.

Objetivo:
    Comprobar que el bloque if __name__ == "__main__"
    no se ejecuta cuando el fichero se importa como módulo.
"""

import diagnostico

print("Comprobación:", diagnostico.comprobar())

servicios = diagnostico.obtener_estado_servicios()
print("Servicios:", servicios)

resumen = diagnostico.resumen_servicios(servicios)
print("Resumen:", resumen)
