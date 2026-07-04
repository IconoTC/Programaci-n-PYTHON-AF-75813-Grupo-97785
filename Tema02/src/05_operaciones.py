# Operaciones aritméticas básicas
unidades = 9
cajas = 4
print("Suma total:", unidades + cajas) # Operación de adición
print("Diferencia:", unidades - cajas) # Operación de sustracción
print("Producto:", unidades * cajas) # Operación de multiplicación
print("Cociente decimal:", unidades / cajas) # División con resultado float
print("Cociente entero:", unidades // cajas) # División descartando decimales
print("Resto de división entero:", unidades % cajas) # Operación de módulo
print("Exponencial:", unidades ** cajas) # Elevación a la potencia

# Operadores de asignación compuesta
stock = 20
print("Stock:", stock)
stock += 10   # Equivale a stock = stock + 10
print("Stock:", stock)
stock *= 10   # Equivale a stock = stock * 10
print("Stock:", stock)

# Operadores relacionales (Comparación)
print("¿Es mayor?:", stock > unidades) # True
print("¿Es mayor o igual?:", stock >= 50) # False
print("¿Es idéntico valor?:", stock == 30) # True
print("¿Es valor distinto?:", stock != 10) # True

# Operadores lógicos
print("Uso de and:", stock > 0 and unidades == 9) # True si ambas se cumplen
print("Uso de and:", stock < 0 and unidades == 9) # False
print("Uso de or:", stock < 0 or unidades > 5) # True si una se cumple
print("Uso de comparacion sin not:", unidades == 5) # False
print("Uso de comparacion con not:", not unidades == 5) # Invierte el resultado a True

# Operadores de identidad (is, is not)
# Validan si las variables apuntan a la misma ubicación de memoria
a = 100
b = 100
print("¿Mismo objeto numérico?:", a is b) # True por optimización de Python
ciudad1 = "Madrid"
ciudad2 = "Madrid"
print("¿Mismo objeto string?:", ciudad1 is ciudad2) # True

# Las listas, aunque tengan igual contenido, son objetos distintos en memoria
carrito_a = ['Monitor', 'Teclado']
carrito_b = ['Monitor', 'Teclado']
print("¿Misma ubicación de lista?:", carrito_a is carrito_b) # False
print("¿Ubicaciones diferentes?:", carrito_a is not carrito_b) # True

# Operadores de pertenencia (in, not in)
usuarios_pro = ['Admin', 'Editor']
print("¿Socio en lista?:", 'Socio' in usuarios_pro) # False
print("¿Socio fuera de lista?:", 'Socio' not in usuarios_pro) # True
print("¿Admin en lista?:", 'Admin' in usuarios_pro) # True

# Aplicación en secuencias de texto (strings)
print("¿Existe 'x' en 'Texto'?:", 'x' in 'Texto') # True
print("¿Existe 'z' en 'Texto'?:", 'z' in 'Texto') # False
print("¿No existe 'z' en 'Texto'?:", 'z' not in 'Texto') # True

# Operador de comparación en cadenada
puntuacion = 85
print("¿Está en rango 0-100?:", 0 <= puntuacion <= 100) # True