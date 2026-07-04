#### Bucles if
# Ejemplo: Validación de rango de temperatura operativa de un servidor (Rango: 18°C a 27°C)
# El sistema debe alertar si la temperatura está fuera de los límites permitidos

grados = int(input("Ingrese temperatura del nodo (18-27): "))

# Ejemplo 1: Estructura de condicionales anidados
print ("Ejemplo 1 de if")
if grados < 18:
    print("Alerta: Temperatura demasiado baja")
else: 
    if grados > 27:
        print("Alerta: Riesgo de sobrecalentamiento")
    else:
        print("Estado del sistema: Óptimo")

# Ejemplo 2: Estructura estándar con elif (La más recomendada por legibilidad)
print ("Ejemplo 2 de if")
if grados < 18:
    print("Alerta: Temperatura demasiado baja")
elif grados > 27:
    print("Alerta: Riesgo de sobrecalentamiento")
else:
    print("Estado del sistema: Óptimo")
     
# Ejemplo 3: Sintaxis abreviada en una sola línea (Short Hand)
print ("Ejemplo 3 de if")
if grados < 18: print("Alerta: Temperatura demasiado baja")  
elif grados > 27: print("Alerta: Riesgo de sobrecalentamiento")
else: print("Estado del sistema: Óptimo")

#### Bucles match case
# Clasificación de prioridad de tickets de soporte
# El usuario introduce un código de criticidad (b, m, a, u)
# Se muestra el nivel de respuesta del equipo técnico

codigo = input("Prioridad del ticket [B]aja, [M]edia, [A]lta, [U]rgente: ").lower()

match codigo:
    case 'b':
        print("Prioridad: BAJA. Respuesta en 48 horas.")
    case 'm':
        print("Prioridad: MEDIA. Respuesta en 24 horas.")
    case 'a':
        print("Prioridad: ALTA. Respuesta en 4 horas.")
    case 'u':
        print("Prioridad: CRÍTICA. Respuesta inmediata.")
    # Ejemplo de agrupación: si el usuario usa códigos numéricos
    case '1' | '2' | '3':
        print("Código numérico detectado. Por favor, use letras.")
    case _:
        print("Código de prioridad no reconocido.")