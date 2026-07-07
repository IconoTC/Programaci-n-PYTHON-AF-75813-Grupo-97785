"""
Tema 5 - Colecciones de objetos
Laboratorio 4: tuplas.

Objetivo:
    Practicar tuplas como secuencias ordenadas e inmutables:
    creación, acceso, recorrido, desempaquetado, pertenencia y conversión.
"""

print("=== 1. Crear y consultar una tupla ===")

endpoint = ("srv-web-01", "10.0.0.20", 443)

print(endpoint)
print(type(endpoint))
print("Host:", endpoint[0])
print("IP:", endpoint[1])
print("Puerto:", endpoint[2])

print("\n=== 2. Tupla vacía y tupla de un solo elemento ===")

tupla_vacia_1 = ()
tupla_vacia_2 = tuple()

print(tupla_vacia_1, tupla_vacia_2)
print(type(tupla_vacia_1))

# La coma es obligatoria para una tupla de un solo elemento.
solo_uno = ("ssh",)
no_es_tupla = ("ssh")

print(solo_uno, type(solo_uno))
print(no_es_tupla, type(no_es_tupla))

print("\n=== 3. Desempaquetado ===")

host, ip, puerto = endpoint

print("Host:", host)
print("IP:", ip)
print("Puerto:", puerto)

print("\n=== 4. Recorrido y pertenencia ===")

puertos_estandar = (22, 80, 443, 5432)

print("Longitud:", len(puertos_estandar))
print("¿443 está permitido?", 443 in puertos_estandar)
print("Primeros dos puertos:", puertos_estandar[:2])

for puerto in puertos_estandar:
    print(f"Puerto permitido: {puerto}")

print("\n=== 5. count() e index() ===")

puertos_repetidos = (22, 80, 443, 80, 8080)

print("Apariciones de 80:", puertos_repetidos.count(80))

if 443 in puertos_repetidos:
    print("Índice de 443:", puertos_repetidos.index(443))

print("\n=== 6. Inmutabilidad ===")

# Las tuplas no permiten modificar, añadir ni eliminar posiciones.
# Descomenta para comprobar el TypeError:
# endpoint[2] = 8443

print("La tupla original sigue igual:", endpoint)

print("\n=== 7. Convertir entre lista y tupla ===")

# Si necesitamos modificar datos, podemos convertir temporalmente a lista.
endpoint_lista = list(endpoint)
endpoint_lista[2] = 8443
endpoint_modificado = tuple(endpoint_lista)

print("Original:", endpoint)
print("Modificado:", endpoint_modificado)

print("\n=== 8. Tuplas generadas a partir de iterables ===")

puertos = [22, 80, 443, 8080]

# Entre paréntesis se crea un generador, no una tupla.
generador = (puerto for puerto in puertos if puerto >= 100)
print("Tipo del generador:", type(generador))

puertos_altos = tuple(puerto for puerto in puertos if puerto >= 100)
print("Tupla generada:", puertos_altos)
