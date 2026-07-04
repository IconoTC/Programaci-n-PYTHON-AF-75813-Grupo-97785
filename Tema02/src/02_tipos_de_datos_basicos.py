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
