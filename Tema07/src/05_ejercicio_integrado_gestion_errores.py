"""
Tema 7 - Gestión de errores
Laboratorio 5: ejercicio final integrado.

Objetivo:
    Combinar validación, try/except, else, finally, raise, excepción
    personalizada y diagnóstico controlado en un flujo pequeño de TI.

Contexto:
    Se procesan entradas de servicios con formato nombre;puerto;estado.
    Algunos registros contienen datos incorrectos y deben separarse sin
    detener todo el proceso.
"""

print("=== 1. Datos de entrada ===")

lineas = [
    "ssh;22;activo",
    "nginx;443;activo",
    "api;no_numero;activo",
    "backup;70000;activo",
    "rdp;3389;detenido",
    "malformada",
]

for linea in lineas:
    print(linea)


print("\n=== 2. Excepción personalizada ===")

class ServicioDetenidoError(Exception):
    """Error de dominio: el servicio está registrado, pero no está activo."""
    pass


print("Excepción personalizada definida.")


print("\n=== 3. Funciones de validación ===")

def validar_puerto(puerto):
    """Valida el rango de un puerto."""
    if not 1 <= puerto <= 65535:
        raise ValueError("Puerto fuera de rango")
    return puerto


def interpretar_linea(linea):
    """
    Convierte una línea de inventario en un diccionario.

    Raises:
        ValueError: si el formato no es correcto o el puerto no es válido.
    """
    partes = linea.split(";")

    if len(partes) != 3:
        raise ValueError("Formato incorrecto")

    nombre, puerto_txt, estado = partes
    nombre = nombre.strip().lower()
    estado = estado.strip().lower()

    puerto = validar_puerto(int(puerto_txt))

    return {
        "nombre": nombre,
        "puerto": puerto,
        "activo": estado == "activo",
    }


def comprobar_disponible(servicio):
    """
    Comprueba si un servicio está activo.

    Raises:
        ServicioDetenidoError: si el servicio está detenido.
    """
    if not servicio["activo"]:
        raise ServicioDetenidoError(f'{servicio["nombre"]} está detenido')
    return servicio


print("Funciones definidas.")


print("\n=== 4. Procesar registros con control de errores ===")

servicios_validos = []
rechazados = []
servicios_detenidos = []

for linea in lineas:
    recurso_abierto = False

    try:
        recurso_abierto = True
        servicio = interpretar_linea(linea)
        servicio = comprobar_disponible(servicio)

    except ServicioDetenidoError as error:
        servicios_detenidos.append((linea, str(error)))

    except ValueError as error:
        rechazados.append((linea, str(error)))

    else:
        servicios_validos.append(servicio)

    finally:
        recurso_abierto = False


print("Servicios válidos:", servicios_validos)
print("Servicios detenidos:", servicios_detenidos)
print("Registros rechazados:", rechazados)


print("\n=== 5. Reporte final ===")

for servicio in servicios_validos:
    print(f'{servicio["nombre"]}:{servicio["puerto"]} -> OK')

print("Total válidos:", len(servicios_validos))
print("Total detenidos:", len(servicios_detenidos))
print("Total rechazados:", len(rechazados))
