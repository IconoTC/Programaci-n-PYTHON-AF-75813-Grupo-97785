# Bucles for con lista
# Lista de componentes de hardware
componentes = ['CPU', 'GPU', 'RAM', 'SSD', 'PSU']
print("Lista de componentes:", componentes)
# Recorrido simple de los elementos de la lista
print("Presentacion en una linea")
for item in componentes:
    print(item, end=" ")
print()
print("Presentacion con salto de linea")
for item in componentes:
    print(item)
# Ejemplo adicional: Uso de la funcion enumerate para obtener índice y valor a la vez
print("Listado con enumeración:")
for indice, nombre in enumerate(componentes):
    print(f"ID {indice} -> {nombre}")
# Acceso a elementos de la lista mediante su índice
# Ejemplo con formatted string: la f""..." indica que entre las comillas, las llaves son variables (Python 3.6+)
print("Listado con formatted string:")
for i in range(len(componentes)):  # Rango dinámico basado en la longitud de la lista
    print(f"Posición {i}: {componentes[i]}") 
# Ejemplo sin formatted string: Hay que concatenar y queda más engorroso
print("Listado concatenando cadenas:")
for i in range(len(componentes)):  
    print("Posición " + str(i) + ": " + componentes[i]) 
print()
# Bucles for con Rangos
# range([inicio,]fin[,paso]) - Recordatorio: el valor de fin no se incluye
print("Rangos")
# Generar una secuencia del 0 al 9
for valor in range(10):   # Inicia en 0 y llega hasta n-1
    print(valor, end=" ")
print()

# Generar una secuencia del 5 al 15
for valor in range(5, 16):   # Inicia en 5 y llega hasta 15
    print(valor, end=" ")
print()

# Números pares del 10 al 20
for valor in range(10, 21, 2):   
    print(valor, end=" ")
print()

# Cuenta atrás del 5 al 1
for valor in range(5, 0, -1):   
    print(valor, end=" ")
print()

# Valores descendentes de 3 en 3 desde 15 hasta 0
for valor in range(15, -1, -3):   
    print(valor, end=" ")
print()
print()
# Ejemplo: Calcular el total de ventas en posiciones impares
ventas = [120, 450, 300, 210, 580, 600, 150]
total_impares = 0

# Version 1: Usando condicional dentro del bucle
for i in range(len(ventas)):
    if i % 2 != 0:
        total_impares += ventas[i]
print("Total acumulado (índices impares):", total_impares)

# Version 2: Usando el parámetro 'step' del range para saltar de 2 en 2
total_impares = 0
for i in range(1, len(ventas), 2):
    total_impares += ventas[i]
print("Total acumulado (optimizado):", total_impares)