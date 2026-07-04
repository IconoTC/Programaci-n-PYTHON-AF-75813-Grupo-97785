import math  # Importación del módulo para operaciones matemáticas avanzadas como potencias

# numeros enteros <class 'int'>
stock_portatiles = 15
# Stock_portatiles = 20 Python es case sensitive; esta sería una variable distinta
stock_monitores = 7
total_equipos = stock_portatiles + stock_monitores
print("Tipo de total_equipos:", type(total_equipos))
print(total_equipos)
# Ejemplo concatenando cadenas. total_equipos debe transformarse a str para poder concatenar
# El error sería -> TypeError: can only concatenate str (not "int") to str
print("Total productos: " + str(total_equipos))   
# Ejemplo imprimiendo cadena y numero. la coma (,) permite imprimir varios tipos de valores 
print("Total productos:", total_equipos)


# numeros reales <class 'float'>
precio_teclado = 25.99
iva_aplicado = 1.21
precio_final = precio_teclado * iva_aplicado
print("Tipo de precio_final:", type(precio_final))
   # print("Coste total:", precio_final) # IndentationError: error por espacio innecesario
print("Coste total:", precio_final)


# booleanos: True o False <class 'bool'>
envio_gratis = False
print("¿Tiene envío gratuito?", envio_gratis)
print("Tipo de envio_gratis:", type(envio_gratis))


# cadenas de texto <class 'str'>
# se pueden utilizar comillas dobles o simples
marca = "Logitech"
modelo = 'G-Pro'
print(marca, modelo)
print(marca + " " + modelo)
print("Tipo de marca:", type(marca))

# --- Conversión de texto a números enteros ---
valor_leido = input("Introduce la cantidad de productos (numero entero): ")
# Verificamos el tipo inicial (siempre será 'str' al usar input)
print("Tipo antes de la conversión:", type(valor_leido))
cantidad = int(valor_leido) # Transformación a entero (falla si hay decimales o letras)
print("Tipo tras conversión:", type(cantidad))
precio_unidad = int(input("Introduce el precio (numero entero): ")) # Convertimos en la asignacion
total_compra = cantidad * precio_unidad # Nota: Introducir '15.5' o 'diez' lanzará un ValueError
print("Coste total entero:", total_compra)

# --- Conversión de texto a números decimales (float) ---
distancia = float(input("Introduce la distancia en km: "))
# Ejemplo con math.pow (potencia) y math.pi (constante pi) para un cálculo hipotético de curvatura
resultado_con_math_pow = math.pi * math.pow(distancia, 2)
# Ejemplo con el operador exponente (**)
resultado_con_operador = math.pi * distancia ** 2  # Aquí usamos ** en lugar de math.pow
print("Resultado con math.pow:", resultado_con_math_pow)
print("Resultado con operador **:", resultado_con_operador)
# Ejemplo con redondeo a 3 decimales
print("Resultado redondeado:", round(resultado_con_operador, 3))

# --- Conversión a valores lógicos (booleanos) ---
# En números: 0 es False, cualquier otro valor es True
activado = 0 
print("¿Está el sistema activo?:", bool(activado))
activado = 1 
print("¿Está el sistema activo?:", bool(activado))

# Ejemplo extra: Conversión de cadenas a bool
# ¡Cuidado! Cualquier cadena no vacía, incluso "0" o "False", devuelve True
estado_texto = "False"
print("Resultado booleano de la cadena 'False':", bool(estado_texto)) 


# --- Conversión a cadenas de texto (string) ---
# Útil para concatenar números con otros textos sin errores
puntuacion = 95
print("Tipo antes de conversión:", type(puntuacion)) # Devuelve int
mensaje_final = "Tu nota es: " + str(puntuacion)
print(mensaje_final)

# Combinar variables numéricas como si fueran texto
print("Concatenación visual:", str(cantidad) + str(precio_unidad))