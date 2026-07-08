"""
Tema 7 - Gestión de errores
Laboratorio 2: orden de captura, else y finally.

Objetivo:
    Practicar el orden de los bloques except y usar else/finally para separar
    operación peligrosa, camino correcto y limpieza final.
"""

print("=== 1. Captura específica y orden de bloques ===")

dividendo = "10"
divisor = "2"

# Cambia divisor por "0" para provocar ZeroDivisionError.
# Cambia divisor por "dos" para provocar ValueError.
# Comenta la conversión int(divisor) para provocar TypeError en la división.
try:
    dividendo = int(dividendo)
    divisor = int(divisor)
    resultado = dividendo / divisor
    print("Resultado:", resultado)
except ValueError:
    print("Conversión inválida.")
except TypeError:
    print("El divisor no es numérico.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except Exception as error:
    print("Error general no previsto:", type(error).__name__, error)


print("\n=== 2. Captura genérica al final ===")

valor = "abc"

try:
    numero = int(valor)
    print(numero)
except ValueError:
    print("ValueError capturado de forma específica.")
except Exception:
    print("Captura general.")


print("\n=== 3. try/except/else ===")

valor = "443"

try:
    puerto = int(valor)
except ValueError:
    print("Puerto no válido.")
else:
    print(f"Puerto aceptado: {puerto}")


print("\n=== 4. finally para limpieza final ===")

valor = "22"
conexion_abierta = False

try:
    conexion_abierta = True
    print("Conexión abierta:", conexion_abierta)
    puerto = int(valor)
    print("Puerto convertido:", puerto)
except ValueError:
    print("Puerto no válido.")
else:
    print("Operación terminada correctamente.")
finally:
    conexion_abierta = False
    print("Conexión abierta:", conexion_abierta)


print("\n=== 5. Ejemplo con error y finally ===")

valor = "ssh"
recurso_abierto = False

try:
    recurso_abierto = True
    print("Recurso abierto:", recurso_abierto)
    puerto = int(valor)
    print("Puerto convertido:", puerto)
except ValueError as error:
    print("Error al convertir el puerto:", error)
finally:
    recurso_abierto = False
    print("Recurso abierto:", recurso_abierto)
