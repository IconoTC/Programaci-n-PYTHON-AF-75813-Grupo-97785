"""
Tema 9 - Módulos
Laboratorio 6: errores frecuentes al importar.

Objetivo:
    Identificar errores comunes de importación sin romper el laboratorio.
"""

print("=== Error 1: recurso inexistente ===")

try:
    from validaciones import validar_ip
except ImportError as error:
    print("ImportError controlado:")
    print(error)

print("\n=== Error 2: módulo inexistente ===")

try:
    import modulo_que_no_existe
except ModuleNotFoundError as error:
    print("ModuleNotFoundError controlado:")
    print(error)

print("\n=== Diagnóstico recomendado ===")
print("- Comprobar el nombre del fichero .py")
print("- Comprobar que estamos ejecutando desde el directorio correcto")
print("- Revisar si el recurso existe dentro del módulo")
print("- Evitar nombres de fichero como random.py, json.py o sys.py")
print("- Revisar si dos módulos se importan entre sí")
