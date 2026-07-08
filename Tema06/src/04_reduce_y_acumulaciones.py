"""
Tema 6 - Elementos de programación funcional
Laboratorio 4: reduce() y acumulaciones.

Objetivo:
    Entender reduce() como una forma de convertir una colección en un único resultado.
    Compararlo con alternativas más simples como sum(), min(), max() o un bucle.
"""

from functools import reduce

print("=== 1. reduce() para sumar valores ===")

medidas = [12, 18, 7, 20]

def acumular(total, valor):
    """
    Suma el valor actual al acumulador.

    Args:
        total: acumulador parcial.
        valor: siguiente elemento de la colección.

    Returns:
        Nuevo acumulador.
    """
    return total + valor

suma_reduce = reduce(acumular, medidas)
suma_sum = sum(medidas)

print("Suma con reduce:", suma_reduce)
print("Suma con sum:", suma_sum)


print("\n=== 2. reduce() para concatenar texto ===")

nombres = ["ssh", "rdp", "www", "ntp"]

def concatenar(acumulador, nombre):
    """Concatena nombres en mayúsculas separados por dos puntos."""
    return acumulador.upper() + " : " + nombre.upper()

cadena = reduce(concatenar, nombres)
print(cadena)


print("\n=== 3. reduce() con valor inicial ===")

puertos = [8080, 22, 8443, 443, 1024]

maximo = reduce(
    lambda acumulador, puerto: puerto if puerto > acumulador else acumulador,
    puertos,
    0,
)

print("Puerto máximo:", maximo)


print("\n=== 4. Colección vacía y valor inicial ===")

sin_puertos = []

maximo_vacio = reduce(
    lambda acumulador, puerto: puerto if puerto > acumulador else acumulador,
    sin_puertos,
    0,
)

print("Puerto máximo en lista vacía:", maximo_vacio)


print("\n=== 5. Alternativa más clara con max() ===")

maximo_directo = max(puertos)
print("Puerto máximo con max():", maximo_directo)


print("\n=== 6. Ejemplo adicional: resumen de estados ===")

estados = ["OK", "ERROR", "OK", "REVISAR", "ERROR"]

def contar_estados(conteo, estado):
    """
    Actualiza un diccionario contador.

    Este ejemplo modifica el acumulador, pero lo hace de forma explícita
    dentro de la función acumuladora.
    """
    if estado not in conteo:
        conteo[estado] = 0

    conteo[estado] += 1
    return conteo

conteo = reduce(contar_estados, estados, {})
print("Conteo de estados:", conteo)
