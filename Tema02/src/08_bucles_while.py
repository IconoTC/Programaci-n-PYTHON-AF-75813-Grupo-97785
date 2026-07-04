# Ejemplo 1: Validación de acceso mediante código de seguridad
# El usuario debe introducir el código "admin123"
# Límite de 3 intentos disponibles
# Se usa 'break' para terminar el bucle

intentos_realizados = 0
max_intentos = 3

while intentos_realizados < max_intentos:
    acceso = input("Introduce código de acceso: ")
    
    if acceso == "admin123":
        print("Acceso concedido al sistema.")
        break  # Finaliza el bucle de inmediato al acertar
    
    # Si no acierta, calculamos y mostramos los intentos restantes
    intentos_realizados += 1
    intentos_restantes = max_intentos - intentos_realizados
    
    if intentos_restantes > 0:
        print(f"Código erróneo. Le quedan {intentos_restantes} intentos.")
    else:
        print("Acceso bloqueado. Agotó todos los intentos.")

# Ejemplo 2: usando 'continue'
# Este bucle muestra números del 1 al 5 saltándose el 3
print("\nEjemplo de control de iteraciones:")
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue  # Salta el resto de esta iteración y vuelve arriba
    print(f"Procesando paso: {contador}")