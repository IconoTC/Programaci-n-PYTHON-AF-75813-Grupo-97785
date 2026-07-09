"""
Tema 8 - Operaciones de entrada-salida
Laboratorio 6: ficheros binarios.

Objetivo:
    Leer y escribir bytes en modo binario. Insertar un mensaje al final de
    un fichero JPG y recuperarlo usando un marcador reconocible.

Requisitos:
    En Tema08/data debe existir el fichero gatito.jpg.
"""
from pathlib import Path

carpeta = Path("Tema08/data")
imagen_original = carpeta / "gatito.jpg"
imagen_modificada = carpeta / "gatito2.jpg"
marcador = "##INICIO##".encode("utf-8")
mensaje = "Marca de seguridad\nFichero procesado desde Python\n"

print("=== 1. Comprobar fichero binario de entrada ===")
if not imagen_original.exists():
    raise FileNotFoundError(f"No existe {imagen_original}. Copia gatito.jpg en la carpeta data.")
print("Imagen original:", imagen_original)
print("Tamaño original:", imagen_original.stat().st_size, "bytes")

print("\n=== 2. Leer bytes de la imagen original ===")
with open(imagen_original, "rb") as fichero:
    bytes_imagen = fichero.read()
print("Bytes leídos:", len(bytes_imagen))
print("Primeros 10 bytes:", bytes_imagen[:10])

print("\n=== 3. Insertar mensaje binario al final ===")
bytes_mensaje = mensaje.encode("utf-8")
with open(imagen_modificada, "wb") as fichero:
    fichero.write(bytes_imagen + marcador + bytes_mensaje)
print("Imagen modificada:", imagen_modificada)
print("Tamaño modificado:", imagen_modificada.stat().st_size, "bytes")

print("\n=== 4. Recuperar mensaje usando el marcador ===")
with open(imagen_modificada, "rb") as fichero:
    contenido_binario = fichero.read()
if marcador in contenido_binario:
    partes = contenido_binario.split(marcador, maxsplit=1)
    bytes_mensaje_puros = partes[1]
    mensaje_extraido = bytes_mensaje_puros.decode("utf-8")
    print("--- Mensaje oculto recuperado ---")
    print(mensaje_extraido)
else:
    print("No se encontró el marcador en el fichero.")

print("\n=== 5. Copia binaria simple por bloques ===")
copia = carpeta / "gatito_copia.jpg"
with open(imagen_original, "rb") as entrada, open(copia, "wb") as salida:
    while True:
        bloque = entrada.read(1024)
        if not bloque:
            break
        salida.write(bloque)
print("Copia creada:", copia)
print("Tamaño copia:", copia.stat().st_size, "bytes")
