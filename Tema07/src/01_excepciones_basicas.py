"""
Tema 7 - Gestión de errores
Laboratorio 1: excepciones básicas y errores frecuentes.

Objetivo:
    Diferenciar errores de ejecución habituales y aplicar try/except básico
    para controlar fallos previsibles sin ocultar problemas no relacionados.
"""

print("=== 1. Excepción no capturada: ejemplo comentado ===")

# Este código generaría ValueError porque "ssh" no puede convertirse a entero.
# Se deja comentado para que el script completo pueda ejecutarse.
#
# puerto = "ssh"
# numero = int(puerto)
# print(numero)

print("Ejemplo no capturado revisado en comentarios.")


print("\n=== 2. try/except básico ===")

valor = "ssh"

try:
    puerto = int(valor)
    print("Puerto convertido:", puerto)
except ValueError:
    print(f"No se puede convertir {valor!r} a número entero.")


print("\n=== 3. Capturar el objeto de excepción con as ===")

valor = "https"

try:
    puerto = int(valor)
    print("Puerto convertido:", puerto)
except ValueError as error:
    print("Puerto no válido.")
    print("Detalle técnico:", error)


print("\n=== 4. Excepciones frecuentes en estructuras de datos ===")

datos = {"ssh": 22}
servicios = ["ssh", "nginx"]

try:
    print("Puerto de api:", datos["api"])
except KeyError as error:
    print("Clave inexistente en diccionario:", error)

try:
    print("Servicio en posición 5:", servicios[5])
except IndexError as error:
    print("Índice fuera de rango:", error)


print("\n=== 5. División entre cero ===")

dividendo = 10
divisor = 0

try:
    resultado = dividendo / divisor
    print(resultado)
except ZeroDivisionError:
    print("No se puede dividir por cero.")


print("\n=== 6. Capturar varias excepciones juntas ===")

datos = ["22", "abc"]
indice = 2

try:
    puerto = int(datos[indice])
    print("Puerto:", puerto)
except (ValueError, IndexError) as error:
    print("No se pudo obtener el puerto.")
    print("Tipo:", type(error).__name__)
    print("Detalle:", error)


print("\n=== 7. Bloque try pequeño y centrado ===")

valor = "443"
puerto = None

try:
    puerto = int(valor)
except ValueError:
    print("Dato no convertible.")

if puerto is not None:
    print("Puerto convertido correctamente:", puerto)
