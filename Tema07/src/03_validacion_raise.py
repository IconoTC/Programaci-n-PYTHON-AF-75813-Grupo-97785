"""
Tema 7 - Gestión de errores
Laboratorio 3: validar antes, capturar después y lanzar excepciones con raise.

Objetivo:
    Comparar LBYL y EAFP, usar raise para indicar estados inválidos y validar
    datos dentro de funciones.
"""

print("=== 1. LBYL: comprobar antes de operar ===")

puertos = {"ssh": 22, "nginx": 443}
servicio = "api"

if servicio in puertos:
    print(puertos[servicio])
else:
    print("Servicio no registrado.")


print("\n=== 2. EAFP: intentar y capturar si falla ===")

try:
    print(puertos[servicio])
except KeyError:
    print("Servicio no registrado.")


print("\n=== 3. Acceso seguro con get() ===")

print(puertos.get(servicio, "Servicio no registrado."))


print("\n=== 4. Lanzar excepciones con raise ===")

def validar_puerto(puerto):
    """
    Valida que un puerto esté en el rango permitido.

    Raises:
        ValueError: si el puerto está fuera de rango.
    """
    if not 1 <= puerto <= 65535:
        raise ValueError("Puerto fuera de rango")
    return puerto


print(validar_puerto(443))

# Descomenta para comprobar el error:
# print(validar_puerto(70000))


print("\n=== 5. Validación dentro de funciones ===")

def crear_endpoint(servicio: str, puerto: int) -> str:
    """
    Construye un endpoint servicio:puerto.

    Raises:
        ValueError: si el servicio está vacío o el puerto está fuera de rango.
    """
    if not servicio:
        raise ValueError("Servicio vacío")
    if not 1 <= puerto <= 65535:
        raise ValueError("Puerto fuera de rango")
    return f"{servicio}:{puerto}"


print(crear_endpoint("ssh", 22))

# Descomenta para comprobar los errores:
# print(crear_endpoint("", 22))
# print(crear_endpoint("ssh", 70000))


print("\n=== 6. Validación al procesar colecciones ===")

datos = ["22", "ssh", "443", "70000"]
validos = []
rechazados = []

for valor in datos:
    try:
        validos.append(validar_puerto(int(valor)))
    except ValueError as error:
        rechazados.append((valor, str(error)))

print("Válidos:", validos)
print("Rechazados:", rechazados)
